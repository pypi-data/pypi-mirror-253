# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details

from unittest import TestCase

from ...pyxb.assertion import NameID, Assertion
from ...pyxb.protocol import AuthnRequest, Response

from .signature import SIGNATURE_ISSUER as issuer

class TestBase(TestCase):
  def setUp(self):
    req = self.req = AuthnRequest()
    req.Destination = "Destination"
    req.Issuer = NameID(issuer)
    resp = self.resp = Response()
    resp.Destination = req.Destination
    resp.Issuer = req.Issuer
    #resp.Assertion.append(Assertion(resp.Issuer))
    resp.set_success()

