import binaryninja as bn
import time

def functionCount(bv):
    bn.log.log(2, "function count: " + str(len(bv.functions)))

def functionStartList(bv):
    for func in bv.functions:
        bn.log.log(2, "Function starts @ " + hex(func.start))

def functionBlocksRangeList(bv):
    for func in bv.functions:
        bn.log.log(2, "Basic Blocks in function: " + str(func.name))
        for block in func.basic_blocks:
            bn.log.log(1, "\t Basic Block Range: " + hex(block.start)+ " --> " + hex(block.end))

def getLastFunctionBlock(bv):
    lfunc = bv.functions[len(bv.functions)-1]
    bn.log.log(2, "Last function is: " + str(lfunc.name))
    blocks = lfunc.basic_blocks
    bigblock = blocks[0] #default to the first block
    #sort the blocks and store the largest in the bigblock
    for i in range(0, len(blocks)):
        if blocks[i].start > bigblock.start:
            bn.log.log(1,"\t Block @ "+ hex(blocks[i].start) + " is largest")
            bigblock = blocks[i]

    lblock = bigblock
    bn.log.log(1, "\t Last Block within that function is: " + hex(lblock.start) + " --> " + hex(lblock.end))
    return lblock

def createProcedure(bv):
    last_block = getLastFunctionBlock(bv)
    bn.log.log(2, "Found last block @ " + hex(last_block.start))
    last_block_addr_str = hex(last_block.end)[:-1]
    last_block_addr_int = int(last_block_addr_str, 16)
    bn.log.log(2, "Creating Procedure after last block @ " + last_block_addr_str)
    #bn.log.log(2, "Creating Procedure after last block @ " + str(type(last_block_addr_int)))
    bv.create_user_function(last_block_addr_int)

def createAllProcedures(bv):
    for i in range(0,5): #index out of range...
            time.sleep(1)
            createProcedure(bv)


bn.PluginCommand.register("foldr_count_funcs", "Count Functions", functionCount)
bn.PluginCommand.register("foldr_start_list", "list Function entry points", functionStartList)
bn.PluginCommand.register("foldr_blocks_range_list", "get the function block ranges", functionBlocksRangeList)
bn.PluginCommand.register("foldr_get_last_function_block", "Get the last function block", getLastFunctionBlock)
bn.PluginCommand.register("foldr_create_procedure", "Create 1 procedure", createProcedure)
bn.PluginCommand.register("foldr_create_all_procedure", "Try to create all procedures", createAllProcedures)
