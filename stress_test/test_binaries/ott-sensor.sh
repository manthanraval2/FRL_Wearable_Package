# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> otttest-time.txt
timeout 60 ./Otttest
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> otttest-time.txt
