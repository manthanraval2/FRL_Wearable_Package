# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> acctest-time.txt
timeout 12h ./acctest
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> acctest-time.txt
