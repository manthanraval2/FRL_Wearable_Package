#!/bin/bash
#Start up Script
echo "Initiate Starting sequence.."
log_file="/sdcard/stress_testing_logs_"
dmesg_log_file="/sdcard/stress_testing_dmesg_logs_"
#Get date and time
var=`date +"%FORMAT_STRING"`
now=`date +"%m_%d_%Y"`
now=`date +"%Y-%m-%d"`
touch "$log_file""`date +%m%d%H%M%Y.%S`"""
touch "$dmesg_log_file""`date +%m%d%H%M%Y.%S`"""
echo "Creating log file!!"
logcat > "$log_file""`date +%m%d%H%M%Y.%S`""".txt &
dmesg -w > "$dmesg_log_file""`date +%m%d%H%M%Y.%S`""".txt &
echo "Capturing logs!!"
chmod 777 /data/local/tmp/frl_sensor_stress_test.sh
sh /data/local/tmp/frl_sensor_stress_test.sh &
