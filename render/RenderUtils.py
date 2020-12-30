from pprint import pformat
from random import shuffle
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.render.Renderer as Render
import CHEMBOX.chemplates.ChemplateUtils as CPU

def validate_QA_template(template):
    QA_model = {
        "sources" : {"name":{"DataGenerator":"paramlist"}},
        "questionlist" : [{"DataGenerator":"paramlist"}],
        "answerlist" : [{"name":{"DataGenerator":"paramlist"}}]
    }
    pass



def process_chemplate(template):
    """
    process_chemplate(chemplate) - process the sources, questionlist, and
        answerlist in a full chemplate, in that order.
    Parameters
    --------
        chemplate: dict of CP.Chemplates (required)
               the dict must have sources, questionlist, and
                   answerlist as IDs, each value is a CP.ChemPlate
    Returns
    _______
        a dictionary of strings:
            'question' : the text of the question used with templates filled in
            'answers' : a list of answer strings, the first one is the correct one


    Raises
    ------
        AttributeError
            if any of the required IDs are missing

    """
    correcttag= "***"

    sourceCP = CP.Chemplate(DoD=template["sources"])
    sources = CPU.create_Chemplate_from_sources(sourceCP)
    src_vals = {id:sources.getIDvalue(id) for id in sources.getIDs()}

    # This has it's own label because the question list in the template has none
    # and it would be harder to code if it did - it'd just be thrown away.
    qCP = CP.Chemplate(DoD={"q":template["questionlist"][0]})
    #print("qCP:",pformat(qCP))
    #print("type sources",type(sources))
    question = CPU.create_Chemplate_from_sources(qCP,None,src_vals)

    #print("\nQuestion:",pformat(question.getIDvalue('q')))

    answerlist = template["answerlist"]
    #print("var_vals:",pformat(var_vals))
    answer_results = []
    for answer in answerlist:
        answerCP=CP.Chemplate(DoD=answer)
        answerval=CPU.create_Chemplate_from_sources(answerCP,None,src_vals)
        answertext = Render.render_item_to_string(answerval)
        if Render.is_correct(answerval):
            answer_results.insert(0,correcttag+ answertext)
        else:
            answer_results.append(answertext)
    shuffle(answer_results)
    return ({'question':question.getIDvalue('q'), 'answers':answer_results})

def process_chemplates(template):
    """
    process_chemplate(chemplate) - process the sources, questionlist, and
        answerlist in a full chemplate, in that order.
    Parameters
    --------
        chemplate: dict of CP.Chemplates (required)
               the dict must have sources, questionlist, and
                   answerlist as IDs, each value is a CP.ChemPlate
    Returns
    _______
        a dictionary of strings:
            'question' : the text of the question used with templates filled in
            'answers' : a list of answer strings, the first one is the correct one


    Raises
    ------
        AttributeError
            if any of the required IDs are missing

    """
