import pytest
from pprint import pformat
import chemplates.DataGenerators as DG

def validate_listOfDataGenerators(generatorList):
    """ validates a list of DataGenerators
    """
    msg=""
    for idx, dataGenerator in enumerate(generatorList,start=1):
        result = DG.validate_args(dataGenerator)
        #print("result",pformat(result))
        if len(result) != 0:
            msg += "\n  ".join([f"dataGenerator index({idx}):",*result])
        if len(msg)>0: msg += "\n"
    return msg

def validate_dictOfDataGenerators(dictOfGenerators):
    """ validates a dictionary of DataGenerators
    """
    msg=""
    for var,dataGenerator in dictOfGenerators.items():
        result = DG.validate_args(dataGenerator)
        #print("result",len(result),":",pformat(result),"<<\n")
        if len(result) != 0:
            msg += "\n  ".join([f"dataGenerator key({var}):",*result])
        if len(msg)>0: msg += "\n"
    return msg
