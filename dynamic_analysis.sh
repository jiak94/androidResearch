package=$(aapt dump badging "$*" | awk '/package/{gsub("name=|'"'"'","");  print $2}')
activity=$(aapt dump badging "$*" | awk '/launchable-activity/{gsub("name=|'"'"'","");  print $2}')
echo "file: $1"
echo "package: $package"
echo "launchable-activity: $activity"

mkdir "./$package"
echo "$package" > "./pkgname"

adb push ./pkgname /data/
adb install $1
adb shell am start -n $package/$activity

sleep 5

adb shell mkdir /data/data/$package/class_names
adb shell mv /data/data/$package/*.txt /data/data/$package/class_names
adb pull /data/data/$package/class_names ./$package/

adb shell am force-stop $package
adb uninstall $package
