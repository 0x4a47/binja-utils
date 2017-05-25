import binaryninja as bn
import time

def findFuncs(bv):
    dangerous = ["fgets", "main", "printf"]
    symbols = bv.get_symbols()
    for symbol in symbols:
        if dangerous in symbol.name:
            bn.log.log(1, "Found dangerous Symbol: " + str(symbol.name))
        bn.log.log(2, "Found Symbol: " + str(symbol.name))

bn.PluginCommand.register("suspicious Functions", "find suspicious Functions", findFuncs)
