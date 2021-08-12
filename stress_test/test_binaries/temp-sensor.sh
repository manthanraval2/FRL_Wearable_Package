# /data/local/tmp/test-sensor.sh 
START_DATE=`date`
echo "$START_DATE " >> temptest-time.txt
timeout 12h ./temptest
# Execute Process
END_DATE=`date`
echo "$END_DATE " >> temptest-time.txt
