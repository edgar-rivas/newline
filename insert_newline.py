#!/usr/bin/python2.7
import sys
import os

file_name = sys.argv[1]
input_file = open(file_name, 'r')
contents = input_file.read()
end = len(contents)+1000000
print end
for i in range(end):
	temp_string = contents[i:i+12]
	if temp_string == '</Parameter>':
		contents = contents[:i+12] + '\n' + contents[i+12:]
output_filename = file_name[:-4]+'_new'+file_name[-4:]
output_file = open(output_filename,'wb')
output_file.write(contents)

print output_filename
input_file.close()
output_file.close()

input_file_2 = open(output_filename, 'r')
grep_str = 'grep -i "<parameter>" '+output_filename+' > '+output_filename[:-4]+'_grep'+output_filename[-4:]
os.system(grep_str)

#print contents
