from pprint import pformat
import CHEMBOX.chemplates.Chemplate as CP
import CHEMBOX.refdata.DataValue as DV
import CHEMBOX.chemplates.ChemplateUtils as CPU


def is_correct(target_item):
    """ is_correct(target_item) returns true if this is a correct answer) """
    assert isinstance(target_item,CP.Chemplate)
    if target_item.existsIDattr("correct","value"):
        return target_item.getIDattr("correct","value") == "true"
    else:
        return False

def render_item(target_item, print_list=None):
    assert isinstance(target_item,CP.Chemplate)
    verbose = True
    if verbose:
        print("PRINT_LIST:",pformat(print_list))
    if print_list is None:
        print_list = []
    if is_correct(target_item):
        print("answer item is correct")
        answer_str = str(target_item.getIDattr("value","value"))
    else:
        value = target_item.getIDattr("value","value")
        print("answer item is incorrect",value)
        if isinstance(value, DV.DataValue):
            magnitude = value.magnitude
            units = target_item.getIDattr("units","value")
            value = DV.DataValue(magnitude = str(magnitude), units = units)
        answer_str = str(value)
    if "text" in print_list:
        answer_str += " " + target_item.getIDattr("text","value")

    return answer_str
