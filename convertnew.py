import json
import yaml
import xmltodict

with open('sample.json','r') as jsonf:
   pdd_f=json.load(jsonf)
 
 
with open('sample.yaml','w') as file_y:
   pdd_y=yaml.dump(pdd_f,file_y)
   
with open('sample.xml','w') as file_x:
   file_x.write(xmltodict.unparse(pdd_f))