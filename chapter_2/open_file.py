#open json file

import json
from pprint import pprint

#with open('/Users/alexeylitovchenko/python_devops/chapter_2/services_policy.json', 'r') as json_file:
#	policy = json.load(json_file)

#pprint(policy)

#policy['Statement']['Resource'] = 'S3'

#with open('/Users/alexeylitovchenko/python_devops/chapter_2/services_policy.json', 'w') as open_file:
#	policy_new = json.dump(policy, open_file)

#pprint(policy_new)

#open YAML format

#import yaml

#with open('/Users/alexeylitovchenko/python_devops/chapter_2/verify-apache.yml', 'r') as open_file:
#	policy_server = yaml.safe_load(open_file)

#pprint(policy_server)

#open XML file - необходимо для чтения разметки веб-страниц

#import xml.etree.ElementTree as ET

#tree = ET.parse('http_feeds.feedburner.com_oreilly_radar_atom.xml')
#root = tree.getroot()
#print(f'ROOT is {root}')

#for child in root:
#	print(child.tag, child.attrib)


