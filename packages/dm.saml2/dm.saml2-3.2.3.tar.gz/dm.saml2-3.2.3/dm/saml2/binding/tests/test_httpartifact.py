# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details

from unittest import TestCase

from ..httpartifact import encode, parse, resolve
from ..util import Store, ArtifactManager

class ArtifactLayer(object):
  @classmethod
  def setUp(cls_):
    cls_.manager = ArtifactManager.from_uri(Store({}), "urn:artifact_manager")

  @classmethod
  def tearDown(cls_):
    cls_.manager = None


class TestHttpArtifact(TestCase):
  layer = ArtifactLayer

  def test_manager(self):
    m = self.layer.manager
    self.assertEqual(m.uri, "urn:artifact_manager")
    self.assertEqual(len(m.id), 20)
    self.assertIsInstance(m.id, bytes)

  def test_exchange(self):
    m = self.layer.manager
    params = encode("message", m)
    mid, epi, a, rs = parse(params)
    self.assertEqual(mid, m.id)
    self.assertEqual(epi, m.index)
    self.assertIsNone(rs)
    self.assertEqual(resolve(a, m), "message")
    self.assertRaises(KeyError, resolve, a, m)

  def test_relay_state(self):
    m = self.layer.manager
    params = encode("message", m, "relay_state")
    mid, epi, a, rs = parse(params)
    self.assertEqual(rs, "relay_state")
    
    
