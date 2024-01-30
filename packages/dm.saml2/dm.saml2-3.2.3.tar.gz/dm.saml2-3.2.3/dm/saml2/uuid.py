"""id generation for saml2."""
from __future__ import absolute_import

from uuid import uuid4, UUID

def uuid(): return str(uuid4())
