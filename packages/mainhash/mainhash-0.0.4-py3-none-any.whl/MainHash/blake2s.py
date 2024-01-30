import hashlib as __hl
def path(p):
  h=__hl.blake2s()
  with open(p,"rb") as f:
    for i in f:
      h.update(i)
  return h.hexdigest()
def file(f):
  h=__hl.blake2s()
  for i in f:
    h.update(i)
  return h.hexdigest()
def text(t,encoding="utf-8"):
  return __hl.blake2s(str(t).encode(encoding)).hexdigest()
