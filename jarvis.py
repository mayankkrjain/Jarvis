#!/usr/bin/python
##Author: Mayank Jain
##This program acts as a central command for Jarvis System
import tagger		##This imports code snippets of tagger.py
import quest_parse as qp	##quest_parse.py
import json
import json_parser as jp
import bot_search as bs
from fuzzywuzzy import fuzz
import subprocess



def main():
	p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	print "Hello " + output.capitalize().strip() + ". How can I help you"
	root=[]
	while True:
		fp=open('Patterns','r').read()
		data=json.loads(fp)
		(entity_list,domain_list,synonym_list)=jp.get_list_attributes(data)
		model=tagger.train_tagger(entity_list)
		line=raw_input('Question:\n')
		line=line.strip(' \n')
		line.lower()
		line.replace("'s",' ')
		tagged_line=tagger.tagit(line,model)
#		(ans,root)=qp.chat_bot(tagged_line,entity_list,domain_list,synonym_list,data,root)
#		print ans

if __name__=="__main__":
	main()
