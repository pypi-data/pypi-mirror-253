# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details
from os.path import dirname, join

from ...signature import default_sign_context, default_verify_context

SIGNATURE_ISSUER = "signature_issuer"

class SignatureLayer(object):
  ISSUER = SIGNATURE_ISSUER

  @classmethod
  def setUp(cls_):
    import dm.xmlsec.binding as xmlsec
    xmlsec.initialize() # Note: the `xmlsec` library may fail, if initialized twice
    res_base = join(dirname(xmlsec.__file__), "resources")
    default_sign_context.add_key(
      xmlsec.Key.load(join(res_base, "rsakey.pem"), xmlsec.KeyDataFormatPem, None),
      cls_.ISSUER
      )
    default_verify_context.add_key(
      xmlsec.Key.load(join(res_base, "rsapub.pem"), xmlsec.KeyDataFormatPem, None),
      cls_.ISSUER
      )

    
  @staticmethod
  def tearDown():
    # does not work -- bug in `ztest`? (lots of intervening `--default`)
    #raise NotImplementedError # continue in a separate thread
    pass
