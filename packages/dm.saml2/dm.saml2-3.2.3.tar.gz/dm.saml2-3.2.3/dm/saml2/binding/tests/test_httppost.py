# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details

from .base import TestBase

from ..httppost import encode, decode, as_form


class PostTests(TestBase):
  def test_req_without_relaystate(self):
    pd = encode(self.req)
    self.assertTrue("RelayState" not in pd)
    self.assertTrue("SAMLRequest" in pd)
    saml, rs = decode(pd)
    self.assertEqual(self.req.toxml("utf-8"), saml)
    self.assertIsNone(rs)

  def test_req_with_relaystate(self):
    pd = encode(self.req, "rs")
    self.assertTrue("RelayState" in pd)
    self.assertTrue("SAMLRequest" in pd)
    saml, rs = decode(pd)
    self.assertEqual(rs, "rs")

  def test_as_form(self):
    pd = encode(self.req)
    form = as_form(pd, "action", "submit", "name")
    
