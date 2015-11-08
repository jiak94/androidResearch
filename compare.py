__author__ = 'jiakuan'
import os, sys


def add_runtime_output():
	file_name = runtime_path  +"/"+ runtime_file_name
	text = open(file_name);
	for line in text:
		runtime_file.append(line)
	
def minus_static_output():
	for file in os.listdir(static_path):
		file_name = static_path + "/" + file
		text = open(file_name)
		for line in text:
			if line not in runtime_file:
				#print line + "not in"
				static_extra.append(line)
				#i = i + 1

			if line in runtime_file:
				#print line + "in"
				runtime_file.remove(line)
				#print len(runtime_file)


def write_result():
	runtime_out = open(output_folder + "/runtime_REMAINING.txt", "a")

	for elements in runtime_file:
		runtime_out.write(elements)
	runtime_out.close()

	static_out = open(output_folder + "/static_REMAINING.txt", "a")

	for elements in static_extra:
		static_out.write(elements)
	static_out.close()



runtime_path = sys.argv[1]
static_path = sys.argv[2]
runtime_file_name = sys.argv[3]

global output_folder
output_folder = runtime_path

#output_folder = apk_name[:apk_name.find(".apk")]

runtime_file = list();
static_extra = list();

add_runtime_output()

minus_static_output()

if not runtime_file and not static_extra:
	print "NOT encrypt"
else:
	print "is encrypt"
	write_result()





