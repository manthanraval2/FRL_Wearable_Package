# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> hrmtest-time.txt
timeout 60 ./hrmtest
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> hrmtest-time.txt
