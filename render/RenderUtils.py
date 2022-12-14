from pprint import pformat
from random import shuffle
import chemplates.Chemplate as CP
import refdata.DataValue as DV
import render.Renderer as Render
import chemplates.ChemplateUtils as CPU

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
    verbose = False
    correcttag= "***"

    sourceCP = CP.Chemplate(DoD=template["sources"])
    sources = CPU.create_Chemplate_from_sources(sourceCP)
    src_vals = {id:sources.getIDvalue(id) for id in sources.getIDs()}

    intermediate_vals = src_vals
    search_key = "intermediate_"
    intermediate_keys = [key for key, val in template.items() if search_key in key]
    if verbose: print("PROCESS CHEMPLATE\n",pformat(intermediate_keys))
    for intermediate_key in sorted(intermediate_keys):
        if verbose: print("PROCESSING: ",intermediate_key,"\n")
        if verbose: print("CURRENT vals:\n",pformat(intermediate_vals),"\n")
        intermediateCP = CP.Chemplate(DoD=template[intermediate_key])
        sources = CPU.create_Chemplate_from_sources(intermediateCP,None,intermediate_vals)
        new_vals = {id:sources.getIDvalue(id) for id in sources.getIDs()}
        if verbose: print("\n=======\nintermediateCP:",pformat(intermediateCP))
        intermediate_vals.update(new_vals)
        if verbose: print("PROCESSED: ",intermediate_key,"\n",pformat(intermediate_vals),"\n")

    if verbose: print("Intermediate PROCESSING DONE\n")




    # This has its own label because the question list in the template has none
    # and it would be harder to code if it did - it'd just be thrown away.
    qCP = CP.Chemplate(DoD={"q":template["questionlist"][0]})
    if verbose: print("qCP:",pformat(qCP))
    if verbose: print("type sources",type(sources))
    question = CPU.create_Chemplate_from_sources(qCP,None,intermediate_vals)

    if verbose: print("\nQuestion:",pformat(question))

    answerlist = template["answerlist"]
    if verbose: print("intermediate_vals:",pformat(intermediate_vals))
    if verbose: print("answer_list:",pformat(answerlist))
    answer_results = []
    for answer in answerlist:
        if verbose: print("answer list n:",pformat(answer))

        answerCP=CP.Chemplate(DoD=answer)
        answerval=CPU.create_Chemplate_from_sources(answerCP,None,intermediate_vals)
        if verbose: print("answerval:",pformat(answerval))
        answertext = Render.render_item_to_string(answerval)
        if verbose: print("answer text:",answertext)
        if Render.is_correct(answerval):
            answer_results.insert(0,correcttag+ answertext)
        else:
            answer_results.append(answertext)
    shuffle(answer_results)
    if verbose: print("answer_results:",pformat(answer_results))
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
