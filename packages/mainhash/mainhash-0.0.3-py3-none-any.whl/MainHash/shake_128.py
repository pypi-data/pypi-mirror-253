import hashlib as _hl
def path(p):
  h=_hl.shake_128()
  with open(p,"rb") as f:
    for i in f:
      h.update(i)
  return h.hexdigest()
def file(f):
  h=_hl.shake_128()
  for i in f:
    h.update(i)
  return h.hexdigest()
def text(t,encoding="utf-8"):
  return _hl.shake_128(str(t).encode(encoding)).hexdigest()
