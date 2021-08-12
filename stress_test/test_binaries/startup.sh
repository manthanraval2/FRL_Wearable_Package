./alt-sensor.sh &
./gyr-sensor.sh &
./temp-sensor.sh &
./acc-sensor.sh &
logcat >> logcat.txt &
dmesg >> dmesg.txt &
