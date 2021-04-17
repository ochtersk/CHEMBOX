import pytest
from pprint import pformat
import commentjson
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.chemplates.ChemplateUtils as CPU
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.render.Renderer as Render
import CHEMBOX.render.RenderUtils as RenderUtils

with open('/Users/ochtersk/src/CHEMBOX/chemplates/template_v5.json', 'r') as handle:
    chemplatedict = commentjson.load(handle)

def test_process_chemplate():
    template_name = "density1"
    template = chemplatedict[template_name]

    results_dict = RenderUtils.process_chemplate(template)
    #print(pformat(results_dict))
    assert isinstance(results_dict["question"], str)
    assert isinstance(results_dict["answers"], list)
    for answer in results_dict["answers"]:
        assert isinstance(answer, str)

#XXX someday make tempplate validator functions
