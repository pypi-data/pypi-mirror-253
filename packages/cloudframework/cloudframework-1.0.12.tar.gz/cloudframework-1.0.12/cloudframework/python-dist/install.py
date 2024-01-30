import os
from shutil import copyfile

doc_root = os.getcwd()
this_script_path = os.path.dirname(__file__)

"""
Copy main.py
"""
copyfile(this_script_path+'/main.py', doc_root+'/main.py')

"""
Requirements
"""
f = open(doc_root+"/requirements.txt", "w")
f.write("cloudframework")
f.close()

"""
app.yaml
"""

appyaml = """service: python-test
runtime: python39
"""

f = open(doc_root+"/app.yaml", "w")
f.write(appyaml)
f.close()
print("The following files have been created: main.py, requirements.txt, app.yaml")
print("To run locally execute:\npython main.py\n")
print("To deploy in standard environment modify app.yaml and change 'service' attribute and execute:\ngcloud app deploy app.yaml --project={your_project_name}\n")
