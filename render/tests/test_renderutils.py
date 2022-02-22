import pytest
from pprint import pformat
import glob
import re
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
    print(pformat(results_dict))
    assert isinstance(results_dict["question"], str)
    assert isinstance(results_dict["answers"], list)
    for answer in results_dict["answers"]:
        assert isinstance(answer, str)

#DONE someday make tempplate validator functions
def process_chemplatefile(filename):
    with open(filename, 'r') as handle:
        try:
            chemplateDict = commentjson.load(handle)
        except TypeError:
            print(f"malformed JSON in {filename}")
        finally:
            handle.close()
        #return

    chemplateNameList = [k for k in chemplateDict.keys() if "_answer" not in k ]
    #print("proc_chemfile:",pformat(chemplateDict),pformat(chemplateNameList))
    return (chemplateDict,chemplateNameList)

def _validate_answer(answer,answers):
    #first choose the correct answer
    correct_ans =""
    pattern = re.compile(r'^\*\*\*')
    for ans in answers:
        if pattern.match(ans):
            correct_ans = ans[3:] #Take the rest of the string after *** sigil
            break
    ansDV=DV.DataValue(correct_ans)
    if "range" in answer.keys():
        ans_magnitude = float(ansDV.magnitude)
        low = answer["range"]["low"]
        high = answer["range"]["high"]
        assert ans_magnitude >= low, f"answer magnitude is too low {ans_magnitude} < {low}"
        assert ans_magnitude <= high, f"answer magnitude is too high {ans_magnitude} > {high}"
    if "units" in answer.keys():
        assert answer["units"] == ansDV.units, f"units don't match:{answer['units']} neq {ansDV.units}"
    return True


@pytest.fixture
def collect_question_files():
    chemplateFilenamesList = glob.glob('render/testchemplates/question_chemplate000*.json')
    return sorted(chemplateFilenamesList)


def test_chemplatefiles_question_types(collect_question_files):
    # this doesn't work for all chemplate files because some are intentionally malformed (008)
    verbose = False
    verbose_results = True
    for filename in collect_question_files:
        if verbose: print("--------------------------------------file:",pformat(filename))
        (chemplateDict,chemplateNameList) = process_chemplatefile(filename)
        for CPname in chemplateNameList:
            if verbose: print(f"file:{filename} chemplate:{CPname}")
            chemplate = chemplateDict[CPname]
            answer = chemplateDict[CPname + "_answer"]
            if verbose: print("chemplate::\n",pformat(chemplate),f"\n_answer n:{CPname}:",answer)
            var = RenderUtils.process_chemplate(chemplate)
            if verbose or verbose_results: print(f"\n{filename}::\n",pformat(var), answer)
            #check if answer is in in_range
            valid = _validate_answer(answer, var["answers"])
            assert valid == True
