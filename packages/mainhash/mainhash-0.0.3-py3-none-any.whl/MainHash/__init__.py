__version_tuple__=(0,0,3)
try:
  import MainHash.blake2b as blake2b
except Exception as error:
  print(error)
try:
  import MainHash.blake2s as blake2s
except Exception as error:
  print(error)
try:
  import MainHash.md5 as md5
except Exception as error:
  print(error)
try:
  import MainHash.sha1 as sha1
except Exception as error:
  print(error)
try:
  import MainHash.sha224 as sha224
except Exception as error:
  print(error)
try:
  import MainHash.sha256 as sha256
except Exception as error:
  print(error)
try:
  import MainHash.sha384 as sha384
except Exception as error:
  print(error)
try:
  import MainHash.sha3_224 as sha3_224
except Exception as error:
  print(error)
try:
  import MainHash.sha3_256 as sha3_256
except Exception as error:
  print(error)
try:
  import MainHash.sha3_384 as sha3_384
except Exception as error:
  print(error)
try:
  import MainHash.sha3_512 as sha3_512
except Exception as error:
  print(error)
try:
  import MainHash.sha512 as sha512
except Exception as error:
  print(error)
# try:
  # import MainHash.shake_128 as shake_128
# except Exception as error:
  # print(error)
# try:
  # import MainHash.shake_256 as shake_256
# except Exception as error:
  # print(error)
# Данные о модуле
__version__="{}.{}.{}".format(*__version_tuple__)
__depends__={
  "required":[
    "hashlib",
    "mainshortcuts"
    ],
  "optional":[]
  }
__functions__=[
  "blake2b.file",
  "blake2b.path",
  "blake2b.text",
  "blake2s.file",
  "blake2s.path",
  "blake2s.text",
  "md5.file",
  "md5.path",
  "md5.text",
  "sha1.file",
  "sha1.path",
  "sha1.text",
  "sha224.file",
  "sha224.path",
  "sha224.text",
  "sha256.file",
  "sha256.path",
  "sha256.text",
  "sha384.file",
  "sha384.path",
  "sha384.text",
  "sha3_224.file",
  "sha3_224.path",
  "sha3_224.text",
  "sha3_256.file",
  "sha3_256.path",
  "sha3_256.text",
  "sha3_384.file",
  "sha3_384.path",
  "sha3_384.text",
  "sha3_512.file",
  "sha3_512.path",
  "sha3_512.text",
  "sha512.file",
  "sha512.path",
  "sha512.text"
  # "shake_128.file",
  # "shake_128.path",
  # "shake_128.text",
  # "shake_256.file",
  # "shake_256.path",
  # "shake_256.text"
  ]
__classes__={}
__variables__=[]
__all__=__functions__+__variables__+list(__classes__.keys())
__scripts__=[
  "MainHash-check",
  "MainHash-gen"
  ]
_algs=[
  "blake2b",
  "blake2s",
  "md5",
  "sha1",
  "sha224",
  "sha256",
  "sha384",
  "sha3_224",
  "sha3_256",
  "sha3_384",
  "sha3_512",
  "sha512"
  # "shake_128",
  # "shake_256"
  ]
__all__.sort()
__functions__.sort()
__scripts__.sort()
__variables__.sort()
_algs.sort()