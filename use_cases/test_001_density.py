import sys
from pprint import pformat
print(f"{sys.path =}")
from chemplates import DataGenerators as DG

# this is a test case for denisty calulations written in python 

d_templates = [ 
    "Calculate the     density of an object which has a mass of {mass} and volume of {volume}.",
    ]

mass = DG.random_value({'type': 'exact','exact' : 12.5})
print(f"{mass =}")
print(mass)
print("test mass:",str(mass))