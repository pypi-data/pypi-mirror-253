# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details
from io import BytesIO

from lxml.etree import parse, tostring

from .base import TestBase

from ..soap import encapsulate, extract

class SoapTests(TestBase):
  def test_encapsulate(self):
    req = self.req
    self.assertEqual(
      extract(encapsulate(req)),
      tostring(parse(BytesIO(req.toxml("utf-8", root_only=True))),
               exclusive=True, method="c14n",
               )
      )
