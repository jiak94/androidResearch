#!/bin/sh
#get source folder
apk_dataset=$1

#get target folder
backsmali_output=$2

#get runtime output folder
Folder_runtime_out=$3

#location of static anaysis result
Full_Path_File_Folder=$4

#Folder_runtime_out=$(aapt dump badging "$*" | awk '/package/{gsub("name=|'"'"'","");  print $2}')

cat ./$Folder_runtime_out/*.txt > ./$Folder_runtime_out/catfile.txt
################################
#   backsmali for all apk in dataset folder #
################################
for file_a in ${apk_dataset}/*; do
	temp_file=`basename $file_a`
	java -jar baksmali-2.1.0.jar ${apk_dataset}/${temp_file} -o ${backsmali_output}/${temp_file}
	for sub_folder in ${backsmali_output}/*; do
		##################################
		#  argv[1] directory of static analysis output  #
		#           argv[2] directory of the .smali file      #
		##################################
		python countSmali.py ${Full_Path_File_Folder} ${sub_folder}
		echo $sub_folder
	done
	####################################
	#argv[1] directory of runtime analysis output    #
	#argv[2] directory of static analysis output        #
	#argv[3] name of the apk                                     #
	####################################
	python compare.py ${Folder_runtime_out} ${Full_Path_File_Folder} $temp_file catfile.txt
	#reset all the folder, ready to analysis next app
	#rm -rf ${backsmali_output}/*
	#rm -rf ${Folder_runtime_out}/*
	#rm -rf ${Full_Path_File_Folder}/*
done
