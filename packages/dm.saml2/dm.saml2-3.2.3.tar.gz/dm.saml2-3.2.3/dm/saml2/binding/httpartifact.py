# Copyright (C) 2010-2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details
"""Support for the http artifact binding.

The artifact binding allows to transport a small reference to an
SAML2 message, called ``artifact`` via
via parameters in an HTTP ``GET`` or ``POST``
request.

The artifact can later be derefenced via the artifact resolution
protocol.

Artifact handling is supported by an ``ArtifactManager``,
defined in module ``util``.
"""
from sys import version_info
from base64 import b64encode, b64decode

from dm.saml2.uuid import UUID

from .compat import to_str, to_bytes

def encode(message, manager, relay_state=None):
  """encode *message* with help of *manager*; return a params dict.

  *message* is a ``PyXB`` binding of an SAML message.

  ``urllib.urlencode`` can be used to prepare the returned params
  for use as url parameters and the ``to_controls`` and ``to_form``
  functions in ``httppost`` to use them in a form.
  """
  params = {}
  if relay_state: params['RelayState'] = relay_state
  epi = manager.index
  EndpointIndex = (epi//256), (epi % 256)
  if version_info.major == 2: EndpointIndex = "".join(map(chr, EndpointIndex))
  else: EndpointIndex = bytes(EndpointIndex)
  TypeCode=b'\x00\x04'
  uuid = UUID(manager.store(message)).bytes + b'\0\0\0\0'
  RemainingArtifact = manager.id + uuid
  artifact = b64encode(TypeCode + EndpointIndex + RemainingArtifact)
  # strip whitespace
  artifact = b''.join(artifact.split())
  params['SAMLart'] = to_str(artifact)
  return params


def parse(params):
  """parse *params* into *SourceID* (`bytes`), *EndpointIndex* (`int`), *artifact* (`bytes`) and *relay_state* (`str` or `None`).

  Used by artifact receiver to obtain the information necessary
  for artifact resolution.
  """
  relay_state = params.get('RelayState')
  artifact = to_bytes(params['SAMLart'])
  return parse_artifact(artifact)[:2] + (artifact, relay_state)


def parse_artifact(artifact):
  """parse artifact into *SourceID* (`bytes`), *EndpointIndex* (`int`) and *MessageHandle* (`bytes`)."""
  artifact = b64decode(artifact)
  if artifact[:2] != b'\x00\x04':
    raise NotImplementedError('unsupported artifact type: %s' % artifact[:2])
  EndpointIndex = to_int(artifact[2])*256 + to_int(artifact[3])
  SourceID = artifact[4:24]
  MessageHandle = artifact[24:]
  return SourceID, EndpointIndex, MessageHandle


def resolve(artifact, manager):
  """resolve *artifact* into associated SAML2 message using *manager*.

  Raise ``KeyError`` in case of resolution problems.
  The ``KeyError`` may be the subtype ``dm.saml2.binding.util.TimeoutError``
  to indicate that the artifact could be resolved but had timed out.
  """
  handle = parse_artifact(artifact)[2]
  uuid = str(UUID(bytes=handle[:16]))
  return manager.retrieve(uuid)


def to_int(v):
  return v if isinstance(v, int) else ord(v)
