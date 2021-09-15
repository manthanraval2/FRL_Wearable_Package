#!/bin/bash
output=/sdcard/output_file.txt
FILE=$output
while [ 1 ]
do
sleep 1m
if [ -f "$FILE" ]; then
	date +"Date: %m-%d-%Y - Time: %T" >> $output
	echo 1 > /sys/devices/platform/soc/soc:oculus,rt600_ctrl/reset
	echo "MCU Reseting.."
else
	echo "$FILE does not exist-> Creating one"
	touch $output
fi
done
