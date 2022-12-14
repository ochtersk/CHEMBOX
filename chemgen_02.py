from jinja2 import Environment, PackageLoader, select_autoescape
import commentjson
import sys

print(__name__)
sys.path.insert(0,"/Users/ochtersk/src/")
print(sys.path)


import render.RenderUtils as RenderUtils

env = Environment(
    loader=PackageLoader('CHEMBOX', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

with open('/Users/ochtersk/src/CHEMBOX/chemplates/template_v5.json', 'r') as handle:
    chemplatedict = commentjson.load(handle)

template_name = "density1"
template = chemplatedict[template_name]
results_dict = RenderUtils.process_chemplate(template)



template = env.get_template('qanda_ol.html')
text = template.render(results_dict)
print(text)
exit()

#print(template.render(name='John Doe'))
