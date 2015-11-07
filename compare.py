__author__ = 'jiakuan'
import os, sys

def add_runtime_output():
	for file in os.listdir(runtime_path):
		file_name = runtime_path  +"/"+ file
		text = open(file_name);
		for line in text:
			runtime_file.append(line)


def minus_static_output():
	for file in os.listdir(static_path):
		file_name = static_path + "/" + file
		text = open(file_name)
		for line in text:
			if line not in runtime_file:
				static_extra.append(line)

			if line in runtime_file:
				runtime_file.remove(line)


def write_result():
	static_out = open(output_folder + "/static_REMAINING.txt", "a+")
	runtime_out = open(output_folder + "/runtime_REMAINING.txt", "a+")

	for elements in runtime_file:
		runtime_out.write(elements)
	runtime_out.close()

	for elements in static_extra:
		static_out.write(elements)
	static_out.close()


runtime_path = sys.argv[1]
static_path = sys.argv[2]
apk_name = sys.argv[3]
runtime_file_name = sys.argv[4]

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




