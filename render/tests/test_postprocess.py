import pytest
from pprint import pformat
import render.Renderer as Render


@pytest.mark.parametrize("text,request_list", [
    ("ion: CH_3^1+", [   #typical
     ("ion: CH", "NORMAL"),
     ("3", "SUBSCRIPT"),
     ("1+", "SUPERSCRIPT")
    ]),
    ("_14^7N", [  #No preceding text
     ("14", "SUBSCRIPT"),
     ("7", "SUPERSCRIPT"),
     ("N", "NORMAL"),
    ]),
    ("N", [ #Only normal text
     ("N", "NORMAL"),
    ]),
    ("", [ # no text
    ]),
    ("_7^14N", [ #opposite order
     ("7", "SUBSCRIPT"),
     ("14", "SUPERSCRIPT"),
     ("N", "NORMAL"),
    ]),
    ("C_2H_4^+2", [ # multiple tokens
     ("C", "NORMAL"),
     ("2", "SUBSCRIPT"),
     ("H", "NORMAL"),
     ("4", "SUBSCRIPT"),
     ("+2", "SUPERSCRIPT"),
    ]),
    ("g/cm^3", [ #units
     ("g/cm", "NORMAL"),
     ("3", "SUPERSCRIPT"),
    ]),
    ("ion: CH_3^1+ trailing text", [ #trailing text
     ("ion: CH", "NORMAL"),
     ("3", "SUBSCRIPT"),
     ("1+", "SUPERSCRIPT"),
     (" trailing text", "NORMAL"),
    ]),

])
def test_post_process_working(text, request_list):
    actual = Render.post_process(text)
    assert len(actual) == len(request_list)
    assert all([a == b for a, b in zip(actual, request_list)])
