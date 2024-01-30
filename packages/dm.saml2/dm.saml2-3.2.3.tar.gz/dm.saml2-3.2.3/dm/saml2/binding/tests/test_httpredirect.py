# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details

from ..httpredirect import encode, decode

from .base import TestBase
from .signature import SignatureLayer, SIGNATURE_ISSUER as issuer

class SimpleTests(TestBase):
  def test_req_without_relaystate(self):
    url = encode("", self.req)
    self.assertIsInstance(url, str)
    self.assertTrue("SAMLRequest" in url)
    self.assertTrue(url.startswith("?"))
    msg, rs = decode(url)
    self.assertIsNone(rs)
    self.assertEqual(msg, self.req.toxml("utf-8", root_only=True))

  def test_join(self):
    url = encode("abc", self.req)
    self.assertEqual(url[3], "?")
    url = encode("abc?x=1", self.req)
    self.assertEqual(url[7], "&")

  def test_req_with_relaystate(self):
    url = encode("", self.req, "RS")
    self.assertIsInstance(url, str)
    msg, rs = decode(url)
    self.assertEqual(rs, "RS")
    self.assertEqual(msg, self.req.toxml("utf-8", root_only=True))

  def test_resp(self):
    url = encode("", self.resp)
    self.assertIsInstance(url, str)
    self.assertTrue("SAMLResponse" in url)
    msg, rs = decode(url)
    self.assertIsNone(rs)
    self.assertEqual(msg, self.resp.toxml("utf-8", root_only=True))


class SignatureTests(TestBase):
  layer = SignatureLayer

  def test_redirect_signature(self):
    req = self.req
    req.request_signature()
    url = encode("", self.req)
    self.assertTrue("SigAlg" in url)
    self.assertTrue("Signature" in url)
    msg, rs = decode(url)
    self.assertTrue(msg.verified_signature())
    self.assertEqual(req.toxml(root_only=True), msg.toxml(root_only=True))

  def test_plain_signature(self):
    req = self.req
    req.request_signature()
    doc = req.toxml("utf-8")
    from dm.saml2.pyxb.protocol import CreateFromDocument
    r = CreateFromDocument(doc)
    self.assertTrue(r.verified_signature())
