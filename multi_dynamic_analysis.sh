for apkfile in $1*.apk
do
	./dynamic_analysis.sh $apkfile
	
done
