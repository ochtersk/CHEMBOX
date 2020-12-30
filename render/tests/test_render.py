import pytest
from pprint import pformat
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.render.Renderer as Render

answer_item=[
  CP.Chemplate(DoD={'correct': {'value': 'true'},
 'reason': {'value': 'To be implemented'},
 'text': {'value': 'mass/volume = (10.00 g)/2.00 mL = 5.0000 g/mL'},
 'units': {'value': 'g/mL'},
 'value': {'value': DV.DataValue(magnitude = "2.00", units = "mL")}
 }),
CP.Chemplate(DoD={'correct': {'value': 'false'},
 'reason': {'value': 'To be implemented'},
 'text': {'value': 'mass/volume = (10.00 g)/2.00 mL = 5.0000 g/mL'},
 'units': {'value': 'g/mL'},
 'value': {'value': DV.DataValue(magnitude = "2.00", units = "mL")}
 })
]


def test_simple_render():
    text = Render.render_item_to_string(answer_item[0])
    #print("ANS TEXT:",text)
    assert str(text) == "2.00 mL"
    text = Render.render_item_to_string(answer_item[1])
    #print("ANS TEXT:",text)
    assert str(text) == "2.00 g/mL"




@pytest.mark.parametrize("print_list,rt_answer, wr_answer", [
    ([], "2.00 mL", "2.00 g/mL"),
    (["text"],  "2.00 mL mass/volume = (10.00 g)/2.00 mL = 5.0000 g/mL", "2.00 g/mL mass/volume = (10.00 g)/2.00 mL = 5.0000 g/mL"),
])
def test_printlist_render(print_list,rt_answer, wr_answer):
    text = Render.render_item_to_string(answer_item[0],print_list)
    #print("\nrANS print_list TEXT:",text)
    assert str(text) == rt_answer
    text = Render.render_item_to_string(answer_item[1],print_list)
    #print("wANS print_list TEXT:",text)
    assert str(text) == wr_answer
