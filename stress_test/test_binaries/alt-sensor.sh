# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> alt-time.txt
timeout 12h ./alttest
# Execute Process
END_DATE=`date`
echo "$END_DATE ">> alt-time.txt
