# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> otttest-time.txt
./Otttest 30
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> otttest-time.txt
