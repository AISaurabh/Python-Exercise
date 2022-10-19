#Example No. 7
import mypkg.mymod
import importlib

importlib.reload(mypkg.mymod)
mypkg.mymod.output()
