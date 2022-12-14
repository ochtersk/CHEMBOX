import pytest
from pprint import pformat
import chemplates.Chemplate as CP
import refdata.DataValue as DV
import render.Renderer as Render

answer_item=[
  CP.Chemplate(DoD={'correct': {'value': 'true'},
 'reason': {'value': 'To be implemented'},
 'text': {'value': 'mass/volume = (10.00 gram)/2.00 milliliter = 5.0000 gram / milliliter'},
 'units': {'value': 'gram / milliliter'},
 'value': {'value': DV.DataValue(magnitude = "2.00", units = "milliliter")}
 }),
CP.Chemplate(DoD={'correct': {'value': 'false'},
 'reason': {'value': 'To be implemented'},
 'text': {'value': 'mass/volume = (10.00 gram)/2.00 milliliter = 5.0000 gram / milliliter'},
 'units': {'value': 'gram / milliliter'},
 'value': {'value': DV.DataValue(magnitude = "2.00", units = "milliliter")}
 })
]


def test_simple_render():
    text = Render.render_item_to_string(answer_item[0])
    #print("ANS TEXT:",text)
    assert str(text) == "2.00 milliliter"
    text = Render.render_item_to_string(answer_item[1])
    #print("ANS TEXT:",text)
    assert str(text) == "2.00 gram / milliliter"




@pytest.mark.parametrize("print_list,rt_answer, wr_answer", [
    ([], "2.00 milliliter", "2.00 gram / milliliter"),
    (["text"],  "2.00 milliliter mass/volume = (10.00 gram)/2.00 milliliter = 5.0000 gram / milliliter", "2.00 gram / milliliter mass/volume = (10.00 gram)/2.00 milliliter = 5.0000 gram / milliliter"),
])
def test_printlist_render(print_list,rt_answer, wr_answer):
    text = Render.render_item_to_string(answer_item[0],print_list)
    #print("\nrANS print_list TEXT:",text)
    assert str(text) == rt_answer
    text = Render.render_item_to_string(answer_item[1],print_list)
    #print("wANS print_list TEXT:",text)
    assert str(text) == wr_answer
