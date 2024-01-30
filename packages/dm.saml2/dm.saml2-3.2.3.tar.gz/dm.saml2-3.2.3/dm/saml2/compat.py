# Copyright (C) 2019 by Dr. Dieter Maurer <dieter@handshake.de>; see 'LICENSE.txt' for details
"""Python 2/3 compatibility."""

def to_str(v):
  """convert *v* to `str`."""
  return (v if isinstance(v, str) # already `str`
          else v.decode("utf-8") if isinstance(v, bytes) # Python 3 `bytes`
          else v.encode("utf-8") # Python 2 `unicode`
          )


def to_bytes(v):
  """convert *v* to `bytes`."""
  return (v if isinstance(v, bytes) # already `bytes`
          else v.encode("utf-8") # Python 3 `str` or Python 2 `unicode`
         )

utext_type = unicode if str is bytes else str
