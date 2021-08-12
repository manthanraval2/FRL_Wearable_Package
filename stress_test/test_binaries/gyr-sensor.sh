# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> gyrtest-time.txt
timeout 12h ./gyrtest
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> gyrtest-time.txt
