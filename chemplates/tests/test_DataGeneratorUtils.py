import pytest
import json
from pprint import pformat
import chemplates.DataGeneratorUtils as DGU

# This is a short list because most of it is tested in t3est_DataGenerators
@pytest.mark.parametrize("test_list, answer", [
    ([ {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      ],"dataGenerator index(2):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"),
    ([ {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      ],""),
    ([ {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      ],"dataGenerator index(1):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"
        "dataGenerator index(2):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"
        ),
])
def test_validate_listOfDataGenerators(test_list, answer):
    msg = DGU.validate_listOfDataGenerators(test_list)
    assert msg  == answer

# This is a short list because most of it is tested in t3est_DataGenerators
@pytest.mark.parametrize("test_dict, answer", [
    ({"var1e": {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      "var2e": {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      },"dataGenerator key(var2e):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"),
    ({"var1v" : {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
     "var2v": {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      },""),
    ({"var1e": {'random_value' :{'type' : 'exact', 'exact' : '123.456'}},
      "var2e": {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      "var3e": {'random_value' :{'type' : 'exact', 'exact' : 123.456}},
      },"dataGenerator key(var2e):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"
        "dataGenerator key(var3e):\n  TypeError for argument exact; wanted:<class 'str'> got:<class 'float'>\n"),
])
def test_validate_dictOfDataGenerators(test_dict, answer):
    msg = DGU.validate_dictOfDataGenerators(test_dict)
    #print("msg:\n",msg,"<\n")
    #print("ans:\n",answer,"<\n")
    assert msg  == answer
