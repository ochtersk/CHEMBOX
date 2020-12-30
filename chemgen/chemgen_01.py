from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('chemgen', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

res = {'answers': ['0.982 g/mL', '1.02 g/mL', '132 g/mL'],
    'question': 'What is the density of a sample with mass 11.4 g and volume 11.61 mL?'}

template = env.get_template('qanda_ol.html')
text = template.render(res)
print(text)
exit()

#print(template.render(name='John Doe'))
