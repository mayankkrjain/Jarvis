##Author:InfoBot Team
##This program parses the database file.
#!/usr/bin/python
import json
from collections import defaultdict
def get_domain(dict_instance,root,domain_list,synonym_list):
	if type(dict_instance) is dict:
		for items in dict_instance.keys():
			if str(items) == 'tagset':
				dict_instance[str(items)]=dict_instance[str(items)].split(',')
				for each_elem in dict_instance[str(items)]:
					synonym_list[str(each_elem)]=str(root)
			if str(items) not in ['meta','tagset','text']:		
				domain_list[str(items)]=1
			        synonym_list[str(items)]=str(items)
			get_domain(dict_instance[items],items,domain_list,synonym_list)
		
def get_list_attributes(data):
	entity_list=[]
	domain_list={}
	domain_list=defaultdict(lambda:0,domain_list)
	synonym_list={}
	synonym_list=defaultdict(lambda:0,synonym_list)
	logical=data['logical']   ##In the given database structure Logical contains the entities
	for key in logical:
		entity_list.append(str(key))
		synonym_list[str(key)]=str(key)
		if type(logical[key]) is dict:
			for items in logical[key].keys():
				if str(items) == 'tagset':
					logical[key][str(items)]=logical[key][str(items)].split(',')
					for each_elem in logical[key][st:r(items)]:
						synonym_list[str(each_elem)]=str(key)
				
				get_domain(logical[key][str(items)],items,domain_list,synonym_list)
	return (entity_list,domain_list.keys(),synonym_list)
	
