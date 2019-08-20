from py_expression_eval import Parser
import refdata.DataValue as DV
from pprint import pformat
parser = Parser()

# x=parser.parse('2 * 3').evaluate({})
# print(x)
# x=parser.parse('2 * 3.0').evaluate({})
# print(x)
# x=parser.parse('2 * x').evaluate({'x': 7})
# print(x)
# x=parser.parse('2 * x').evaluate({'x': 7.0})
# print(x)
# x=parser.parse('g /mL*mL').simplify({}).toString()
# print(x)
x = DV.DataValue('3.0000 g')
y = DV.DataValue('6.000 g')
v = DV.DataValue('3.00 mL')
print(x,y)
z=parser.parse('(x + y)/v').evaluate({'y':y, 'x':x, 'v' : v})
print(z)
