#!/usr/bin/python2.7
#title		:insert_newline.py

# Import modules
import sys
import os
import re

file_name = sys.argv[1]
input_file = open(file_name, 'r')
output_file = open(str(file_name[:-4]+"_new"+file_name[-4:]), 'wb')

contents = input_file.read()
end = len(contents)
i = 0
init_strip=0

while i < end:
	temp_string = contents[i:i+11]
	if temp_string == '<Parameter>':
		if init_strip == 0:
			contents = contents[i:]
			end = len(contents)
			init_strip = 1
			i = 11
			continue
		contents = contents[:i] + '\n' + contents[i:]
		i+=1
		end = len(contents)
	i+=1

for line in contents.splitlines():
	if re.search('<Parameter>',line):
		print line
		output_file.write(line+'\n')		

input_file.close()
output_file.close()
