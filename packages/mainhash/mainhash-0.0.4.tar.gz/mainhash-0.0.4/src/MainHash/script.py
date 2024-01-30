import os, traceback
import MainShortcuts as ms
import MainHash as mh
class mc:
  pid=os.getpid()
  args=ms.proc.args
  dir=ms.path.info(__file__)["dir"]
  exception=traceback.format_exc
  run=__name__=="__main__"
  class core:
    name="MainCore"
    version=1
# Обработка аргументов
argv=mc.args[1:]
opt={}
for full,short in {"print":"p","no-color":"c","help":"h"}.items():
  opt[full]=False
  for i in [full,short,"-"+full,"-"+short]:
    while f"-{i}" in argv:
      opt[full]=True
      argv.pop(argv.index(f"-{i}"))
del full, short, i
if len(argv)==0:
  opt["help"]=True
if opt["no-color"]:
  GREEN=""
  RED=""
  RESET=""
  YELLOW=""
else:
  try:
    import colorama
    colorama.init()
    GREEN=colorama.Fore.GREEN
    RED=colorama.Fore.RED
    RESET=colorama.Style.RESET_ALL
    YELLOW=colorama.Fore.YELLOW
  except:
    opt["no-color"]=True
    GREEN=""
    RED=""
    RESET=""
    YELLOW=""
help={"gen":[],"check":[]}
help["gen"]=[
  "Generating checksums for a file or folder",
  "",
  "Usage:",
  "  MainHash-gen {GREEN}<path>{RESET} {YELLOW}[options]",
  "{GREEN}Required args:",
  "  {GREEN}path{RESET} - path to the file or folder for which checksums need to be generated",
  "         You can specify multiple objects, separating them with a space",
  "{YELLOW}Optional args:",
  "  {YELLOW}-c{RESET} | {YELLOW}--no-color{RESET} - do not display colored text",
  "  {YELLOW}-p{RESET} | {YELLOW}--print{RESET}    - don't write checksums file, print them as JSON",
  "                    This also disables colored text",
  "                    Not recommended for use with multiple objects",
  "  {YELLOW}-h{RESET} | {YELLOW}--help{RESET}     - do nothing, just show this guide",
  '                    You can use "{YELLOW}--no-color{RESET}" to turn off color',
  "",
  "This program is included in the {GREEN}MainHash{RESET} module created by {GREEN}MainPlay TG",
  'To update: "{YELLOW}python -m{RESET} {GREEN}pip install -U mainhash{RESET}"',
  "Contact: {GREEN}https://t.me/MainPlay_TG{RESET} {YELLOW}(Russian language recommended)"
  ]
help["check"]=[
  "Comparing checksums with a previously written file (from the MainHash-gen command)",
  "",
  "Usage:",
  "  MainHash-check {GREEN}<path>{RESET} {YELLOW}[options]",
  "{GREEN}Required args:",
  "  {GREEN}path{RESET} - path to the file or folder whose checksum needs to be compared",
  "         You can specify multiple objects, separating them with a space",
  "{YELLOW}Optional args:",
  "  {YELLOW}-c{RESET} | {YELLOW}--no-color{RESET} - do not display colored text",
  "  {YELLOW}-p{RESET} | {YELLOW}--print{RESET}    - output comparison results as JSON",
  "                    This also disables colored text",
  "                    Not recommended for use with multiple objects",
  "  {YELLOW}-h{RESET} | {YELLOW}--help{RESET}     - do nothing, just show this guide",
  '                    You can use "{YELLOW}--no-color{RESET}" to turn off color',
  "",
  "This program is included in the {GREEN}MainHash{RESET} module created by {GREEN}MainPlay TG",
  'To update: "{YELLOW}python -m{RESET} {GREEN}pip install -U mainhash{RESET}"',
  "Contact: {GREEN}https://t.me/MainPlay_TG{RESET} {YELLOW}(Russian language recommended)"
  ]
def cprint(a):
  print(RESET+str(a).format(RESET=RESET,GREEN=GREEN,RED=RED,YELLOW=YELLOW).rstrip()+RESET)
class _print:
  def __init__(self):
    self.data={}
  def save(self):
    ms.json.print(self.data)
def _genFile(path,list=[],list_mode="b"):
  root=os.getcwd()
  info=ms.path.info(path)
  if info["type"]!="file":
    raise Exception("This is not a file")
  dir=os.path.dirname(path)
  if dir=="":
    dir="."
  os.chdir(dir)
  algs=[]
  for alg in mh._algs:
    if list_mode.lower() in ["-","0","b","black","blacklist","exclude","off"]: # Чёрный список
      if not alg in list:
        algs.append(alg)
    elif list_mode.lower() in ["+","1","include","on","w","white","whitelist"]: # Белый список
      if alg in list:
        algs.append(alg)
    else:
      raise Exception('Invalid list mode. Use "black" or "white", not "{0}"'.format(list_mode))
  d={}
  for alg in algs:
    d[alg]=getattr(mh,alg).path(path)
  os.chdir(root)
  return d
def _genDir(path=os.getcwd(),**kwargs):
  root=os.getcwd()
  if not os.path.isdir(path):
    raise Exception("This is not a folder")
  os.chdir(path)
  path=os.getcwd()
  info=ms.path.info(path,listdir=True,listlinks=False)
  files=info["files"]
  d={}
  for i in files:
    if not i.lower().endswith(".mainhash"):
      d[os.path.relpath(i,path)]=_genFile(i,**kwargs)
  os.chdir(root)
  return d
def _genAuto(path,**kwargs):
  type=ms.path.info(path)["type"]
  if type=="file":
    return _genFile(path,**kwargs)
  elif type=="dir":
    return _genDir(path,**kwargs)
  else:
    raise Exception(f"Unknown type: {type}")
def _checkFile(path,h1,h2=None,**kwargs):
  if h2==None:
    h2=_genFile(path,**kwargs)
  d={"diff":[],"equal":[],"only1":[],"only2":[]}
  for i in h1:
    if i in h2:
      if h1[i]==h2[i]:
        d["equal"].append(i)
      else:
        d["diff"].append(i)
    else:
      d["only1"].append(i)
  for i in h2:
    if not i in h1:
      d["only2"].append(i)
  return d
def _checkDir(path=os.getcwd(),h1=None,h2=None,**kwargs):
  if h1==None:
    raise Exception('The "h1" argument is not set, there is nothing to compare it with')
  if h2==None:
    h2=_genDir(path,**kwargs)
  d={"diff":{},"equal":{},"only1":[],"only2":[],"none":{}}
  for i in h1:
    if not i.lower().endswith(".mainhash"):
      if i in h2:
        h=_checkFile(i,h1[i],h2[i],**kwargs)
        if len(h["diff"])==0 and len(h["equal"])>0:
          d["equal"][i]=h
        elif len(h["diff"])==0 and len(h["equal"])==0:
          d["none"][i]=h
        else:
          d["diff"][i]=h
      else:
        d["only1"].append(i)
  for i in h2:
    if not i.lower().endswith(".mainhash"):
      if not i in h1:
        d["only2"].append(i)
  return d
def _checkAuto(path,**kwargs):
  type=ms.path.info(path)["type"]
  if type=="file":
    return _checkFile(path,**kwargs)
  elif type=="dir":
    return _checkDir(path,**kwargs)
  else:
    raise Exception(f"Unknown type: {type}")
# Выполняемый код
def gen(files=argv,**kwargs):
  if opt["help"]:
    for i in help["gen"]:
      cprint(i)
    ms.exit(0)
  if type(files)==str:
    files=[files]
  for f in files:
    if not opt["print"]:
      cprint(f'Generating checksums for "{f}"')
    try:
      info=ms.path.info(f)
      h=_genAuto(f,**kwargs)
      if opt["print"]:
        json=_print()
      elif info["type"]=="file":
        json=ms.cfg(info["fullpath"]+".MainHash",type="json",json_args={"mode":"p"})
      elif info["type"]=="dir":
        json=ms.cfg(ms.path.merge([info["fullpath"],"dir.MainHash"]),type="json",json_args={"mode":"p"})
      json.data={"format":1,"files":h,"type":info["type"]}
      json.save()
      if not opt["print"]:
        cprint(f'{GREEN}The checksums are written to the file "{os.path.abspath(json.path)}"')
    except:
      if not opt["print"]:
        cprint(f'{YELLOW}Checksums could not be generated for "{f}"')
        cprint(RED+str(mc.exception()))
def check(files=argv,**kwargs):
  if opt["help"]:
    for i in help["check"]:
      cprint(i)
  if type(files)==str:
    files=[files]
  for f in files:
    if not opt["print"]:
      cprint(f'Generating checksums for "{f}"')
    try:
      info=ms.path.info(f)
      hgen=_genAuto(f,**kwargs)
    except:
      if not opt["print"]:
        cprint(f'{YELLOW}Checksums could not be generated for "{f}"')
        cprint(RED+str(mc.exception()))
    if not opt["print"]:
      cprint(f'Checksum comparison for "{f}"')
    try:
      if info["type"]=="file":
        json=ms.cfg(info["fullpath"]+".MainHash",type="json")
      elif info["type"]=="dir":
        json=ms.cfg(ms.path.merge([info["fullpath"],"dir.MainHash"]),type="json")
      hload=json.load()["files"]
      if opt["print"]:
        ms.json.print(_checkAuto(f,h1=hload,h2=hgen,**kwargs))
        raise Exception("Skipping unnecessary processing is not an error")
      r=_checkAuto(f,h1=hload,h2=hgen,**kwargs)
      if info["type"]=="file":
        if len(r["equal"])==0 and len(r["diff"])>0:
          cprint(f"{RED}No matches between files")
        elif len(r["equal"])>0 and len(r["diff"])==0:
          cprint(f"{GREEN}All available checksums match")
        elif len(r["equal"])==0 and len(r["diff"])==0:
          cprint(f"{YELLOW}No checksums to compare")
        else:
          tmp1=", ".join(r["equal"])
          tmp2=", ".join(r["diff"])
          cprint(f"{GREEN}Checksums {tmp1} match")
          cprint(f"{RED}Checksums {tmp2} do not match")
          del tmp1, tmp2
        if len(r["only1"])>0:
          tmp=", ".join(r["only1"])
          cprint(f"{YELLOW}Failed to generate checksums {tmp}")
          del tmp
        if len(r["only2"])>0:
          tmp=", ".join(r["only2"])
          cprint(f"{YELLOW}Checksums {tmp} were not found in the saved file")
      elif info["type"]=="dir":
        diff=list(r["diff"].keys())
        equal=list(r["equal"].keys())
        onlyload=r["only2"]
        onlygen=r["only1"]
        none=list(r["none"].keys())
        if len(equal)==0 and len(diff)>1:
          cprint(f"{RED}No files match")
        elif len(equal)>0 and len(diff)==0 and len(onlyload)==0 and len(onlygen)==0 and len(none)==0:
          cprint(f"{GREEN}All files are the same. No extra or lost files")
        else:
          if len(equal)>0:
            cprint("{0}Files {1} are the same".format(GREEN,", ".join(equal)))
          if len(diff)>0:
            cprint("{0}Files {1} do not match".format(RED,", ".join(diff)))
          if len(onlyload)>0:
            cprint("{0}Files {1} not found".format(YELLOW,", ".join(onlyload)))
          if len(onlygen)>0:
            cprint("{0}Files {1} are extra".format(YELLOW,", ".join(onlygen)))
          if len(none)>0:
            cprint("{0}Files {1} do not have common checksums".format(YELLOW,", ".join(none)))
    except:
      if not opt["print"]:
        cprint(f'{YELLOW}Checksum comparison error for "{f}"')
        cprint(RED+str(mc.exception()))
