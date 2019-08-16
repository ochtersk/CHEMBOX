import refdata.DataValue as DV
#db setup code
from random import randint
from tinydb import TinyDB, Query
import os
import json

with open('Config.json') as json_config_file:
    config = json.load(json_config_file)

dbFileName = config["rootdir"] + config["ChemDataDB"]["filename"]
CV_db = TinyDB(dbFileName)

class RefData():
    """RefData class for ChemBox to look up and deliver a DataValue holding the
    reference data.

    Attributes
    ----------
    value : DataValue
        The numerical magnitude and units
    compound : string
        The name (or chemical formula) used to look up the data for this
        compound (or element, or ion).
        property : what chemical property this is (ex: density)
        source : the reference for the source of the data
        addl_info : the field from the db, stored as a dictionary

    Public Methods
    --------------
    __init__ create a new Data Value with the supplied magnitude and units
            parameters:
                - ChemicalProperty (required) what property value to get
                - chemicalName: the name of a compound, if None, get a
                random one from the database

    __str__  give a string representation of the DataValue
    __repr__ give a more detailed representation of the DataValue


    """
    def __init__(self, chemicalProperty = None, chemicalName=None  ):
        Prop = Query()
        assert chemicalProperty != None, "No ChemicalProperty specified"
        results = {}
        if chemicalName != None:
            searchResultsList= CV_db.search((Prop.property == chemicalProperty)&(Prop.chemicalName == chemicalName))
            Nresults = len(searchResultsList)
            #print("cmpd + prop results:",searchResultsList)
            assert Nresults>0, f"No results from search {chemicalProperty},{chemicalName}"
            assert Nresults==1, f"too many ({Nresults}) results from search of {chemicalProperty}+{chemicalName}"
            results = searchResultsList[0]
        else:
            searchResultsList= CV_db.search(Prop.property == chemicalProperty)
            Nresults = len(searchResultsList)
            assert Nresults>0, f"No results from search of {chemicalProperty}"
            results = searchResultsList[randint(0,Nresults-1)]
        #print("DB Results:",results)
        self.value = DV.DataValue(results["value"],results["units"] )
        self.chemicalName = results["chemicalName"]
        self.property = results["property"]
        self.data_source = results["source"]
        #print(repr(self))

    def __str__(self):
        value = str(self.value)
        return f'{self.chemicalName} has a {self.property} value of {value}'

    def __repr__(self):
        value = str(self.value)
        return \
            f'RefData:\n'\
            f' compound:{self.chemicalName}\n'\
            f' property:{self.property}\n'\
            f'    value:{value}\n'\
            f' data src:{self.data_source}\n'
