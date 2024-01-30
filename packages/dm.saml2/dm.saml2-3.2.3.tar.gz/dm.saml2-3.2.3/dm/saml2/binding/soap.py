# Copyright (C) 2011-2019 by Dr. Dieter Maurer <dieter@handshake.de>
"""SAML2 SOAP binding."""

from logging import getLogger

from .compat import to_bytes

class BadMessage(Exception):
  """Indicate a bad soap message."""


logger = getLogger(__name__)


SOAP_ENV_TEMPLATE=b"""<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body>%s</SOAP-ENV:Body></SOAP-ENV:Envelope>""" 

# interestingly, the `Fault` children lack an XML namespace.
#  code taken from http://www.w3.org/TR/2000/NOTE-SOAP-20000508/#_Ref477795996
SOAP_FAULT_TEMPLATE="""<SOAP-ENV:Fault><faultcode>%s</faultcode><faultstring>%a</faultstring><detail><exception xmlns="urn:exception_info">%s</exception></detail></SOAP_ENV:Fault>""" 


def encapsulate(saml):
  """encapsulate *saml* with an SOAP envelope (reurning `bytes`)."""
  if hasattr(saml, "toxml"): saml = saml.toxml(root_only=True)
  saml = to_bytes(saml)
  return SOAP_ENV_TEMPLATE % saml



def extract(soap):
  """extract the saml message from the SOAP envelope *soap*."""
  # we use `lxml` for parsing as it is needed for signing as well
  from lxml.etree import fromstring, tostring
  r = fromstring(soap)
  body = None
  for child in r:
    if (child.tag or "").endswith("Body"): body = child; break
  # may raise `IndexError` when *soap* is not valid
  message = body[0]
  return tostring(message, exclusive=True, method="c14n",)
  


def http_post(transport, url, saml):
  """post *saml* message to *url* and return the *saml* response.

  *transport* is expected to have an `open` method with parameters *url*,
  *data* and *headers*. Note, that for real SAML2 compatibility, it must
  provide an HTTPS client certificate and verify the HTTPS server certificate.
  The result is expected to be similar to that of `urllib2.urlopen`;
  http errors are expected to raise an exception.
  """
  r = transport.open(
    url, encapsulate(saml),
    {"Cache-Control" : "no-cache, no-store",
     "Pragma" : "no-cache",
     "SOAPAction" : "http://www.oasis-open.org/committees/security",
     "Content-Type": "text/xml; charset=utf-8",
     }
    )
  return extract(r.read())
  
  
def http_request(soap, callback):
  """process *soap* request via *callback*.

  return a triple *body*, *headers*, *status* describing the result.

  Note, that if *status* is not 200, it might be necessary to
  abort a (potential) transaction.
  """
  try:
    result = callback(extract(soap), binding="SOAP")
  except Exception as e:
    logger.exception("processing %s failed", soap)
    # we do not distinguish between server and client errors
    # we always include `detail` (violating the SOAP 1.1 spec which
    #   request `detail` to be present only for `Body` processing problems
    result = SOAP_FAULT_TEMPLATE % (
      "SOAP-ENV:Server",
      "Server Error",
      "%s: %s" (e.__class__, e)
      )
    status = 500
  else: status = 200
  return (encapsulate(result),
          {"Cache-Control" : "no-cache, no-store, must-revalidate, private",
           "Pragma" : "no-cache"
           },
          status)
    
