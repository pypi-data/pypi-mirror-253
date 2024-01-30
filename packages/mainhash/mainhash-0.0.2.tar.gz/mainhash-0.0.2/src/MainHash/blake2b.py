import hashlib as __hl
def path(p):
  h=__hl.blake2b()
  with open(p,"rb") as f:
    for i in f:
      h.update(i)
  return h.hexdigest()
def file(f):
  h=__hl.blake2b()
  for i in f:
    h.update(i)
  return h.hexdigest()
def text(t,encoding="utf-8"):
  return __hl.blake2b(str(t).encode(encoding)).hexdigest()
