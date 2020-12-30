from pprint import pformat
from jinja2 import Environment, Template, select_autoescape

class sstring:
    def __init__(self, sstring):
        self.sstring = sstring

    def superscriptify(text):
        return "<sup>"+str(text.sstring )+"</sup>"



env = Environment(
    autoescape=select_autoescape(['html', 'xml'])
)

x =sstring("abc")

print(x.superscriptify())

tt = ' part1={{ var1.superscriptify() }} part2={{var2}} part3={{var3}} tail\n'

jt = Template(tt)

vars = { 'var1': sstring("x1"), 'var2': "y2", "var3": "z3"}

gen = jt.generate(vars)

for x in gen:
  print(pformat(x))

print("\n---\n")
print(pformat("the end"))
