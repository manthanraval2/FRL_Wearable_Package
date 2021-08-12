# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> hrmtest-time.txt
./hrmtest 30
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> hrmtest-time.txt
