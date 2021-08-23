1. DONE: rename chemical name stuff all to chemicalName to be consistent
1. DONE: implement and test math expressions stuff
1. DONE: implement stuff for changing source templates so you can have parameters to fill template
1. DONE: fix sigfigs repr
1. testing for templates

# code enhancements
1. DONE: chemistry formulas : use pyvalem
1. reactions
    1. bulk import of balanced reactions
       1. duplicate equation detector
       1. DONE: discern reaction type
    1. balancing
    1. stoichiometry
    1. DONE: (pretty well - needs refactoring) reaction types
    1. predicting products
    1. reaction db
1, Units conversions
  1. DONE use Pint https://pint.readthedocs.io/en/stable/index.html
  1. add flag to DataValue __init__ to get abbrev units.

# code fixes
1. fix function names to snake case
1. refactor Rxn.detectRxnType
1. DONE: fix test_create to not warn on sci not with no leading zeros

# new chemplates:
1. additional density and other math questions
    - real data sources

1. ionic compounds
    - implement ion lists
    - implement ion mixer

# output templates
  1. multiple choice even spacing
  1. short answer with columns (ionic names, compounds)

# server implementation
