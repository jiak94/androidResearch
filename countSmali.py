__author__ = 'jiakuan'
import os, sys

def get_full_path(file_name):
	file = open(file_name)
	line = file.readline()
	line = line[line.rfind(" ")+1:]
	write_to_file(line)

def write_to_file(full_path):
	file = open(output_folder + "/" + output_file_name, "a")
	file.write(full_path)
	file.close()

def rename_output_file(smaliCount, old_name, path):
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)) == True:
			if old_name in file:
				new_name = file[:file.rfind('.')] + "_"+str(smaliCount) + "_.txt"
				os.rename(os.path.join(path, file), os.path.join(path, new_name))

def generate_output(path, smaliCount):
	for  root, dirs, files in os.walk(path):
		for name in files:
			if ".smali" in name:
				smaliCount = smaliCount + 1
				get_full_path(root + "/" + name)


#location that store the full_path_file
output_folder = sys.argv[1]

#location of the .smali file folder (after decompile)
apk_folder = sys.argv[2]
output_file_name = apk_folder[apk_folder.find("/")+1:]+ ".txt"
path = os.getcwd()  + "/" +apk_folder

smaliCount = 0

generate_output(path, smaliCount)
rename_output_file(smaliCount, output_file_name, os.getcwd() + "/" + output_folder)
print "Decomile Done for " + apk_folder
