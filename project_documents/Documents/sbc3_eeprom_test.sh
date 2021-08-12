#!/bin/sh

. ./basic_cmd.sh

eeprom_testfile="$TMP_DIR/.eeprom_testfile"
eeprom_node="/sys/bus/i2c/devices/4-0050/eeprom"

#eeprom Test's process id and status
export eeprom_pid=0
eeprom_test_status_file="$TMP_DIR/.eeprom_test_status"

#Pass logfile name to basic_cmd with original command
execute_eeprom_cmd()
{
	execute_cmd "$1" "$LOG_DIR/eeprom-log-$ts.txt"
}

#Function to start eeprom test
start_eeprom_test()
{
	execute_eeprom_cmd "echo 'Starting eeprom Test'"
	echo "UP and Running" > $eeprom_test_status_file

	#generate file of 16KB
	eval ./busybox dd  if=/dev/urandom of=$eeprom_testfile bs=32 count=1 > /dev/null 2>&1
	rc=$?
	if [ "$rc" != 0 ]
	then
		#return if fail
		execute_eeprom_cmd "echo 'couldnt create test file $eeprom_testfile'"
		echo "Failed, couldn't create test file" > $eeprom_test_status_file
		return $rc
	fi
	execute_eeprom_cmd "echo 'Created test file successfully'"

	while [ 1 ]
	do
		#start write eeprom
		outfile=$eeprom_node
		eval ./busybox dd  if=$eeprom_testfile of=$outfile bs=32 count=1 > /dev/null 2>&1
		rc=$?
		if [ "$rc" != 0 ]
		then
			#return if fail
			execute_eeprom_cmd "echo 'eeprom Write failed'"
			echo "Failed, Write Failed" > $eeprom_test_status_file
			break
		fi
		execute_eeprom_cmd "echo 'eeprom Write done'"
		sleep 1

		#Read eeprom
		outfile="$eeprom_testfile.read"
		eval ./busybox dd  if=$eeprom_node of=$outfile bs=32 count=1 > /dev/null 2>&1
		rc=$?
		if [ "$rc" != 0 ]
		then
			#return if fail
			execute_eeprom_cmd "echo 'eeprom Read failed'"
			echo "Failed, Read Failed" > $eeprom_test_status_file
			break
		fi
		execute_eeprom_cmd "echo 'eeprom Read done'"
		sleep 1

		md5sum_check $eeprom_testfile $outfile
		rc=$?
		if [ "$rc" != 0 ]
		then
			execute_eeprom_cmd "echo 'MD5sum mismatch'"
			echo "Failed, MD5Sum mismatch" > $eeprom_test_status_file
			break
		fi
		execute_eeprom_cmd "echo 'Verified eeprom Read-Write md5sum'"

		#wait for 5 second
		sleep 5;

	done
}

#Function to stop eeprom test
stop_eeprom_test()
{
	if [ $eeprom_pid -gt 0 ]
	then
		execute_eeprom_cmd "echo 'Stoping eeprom Test'"
		kill -9 $eeprom_pid
		echo "Not Running" > $eeprom_test_status_file
		eeprom_pid=0
	fi

}

#Function to start/stop eeprom test
test_eeprom()
{
	#if value @1 is 1 then start the test
	if [ $1 -eq 1 ]
	then
		if [ $eeprom_pid -gt 0 ]
		then
			execute_eeprom_cmd "echo 'eeprom test is already running, restarting....'"
			stop_eeprom_test
		fi
		start_eeprom_test &
		eeprom_pid=$!
	else
		stop_eeprom_test
	fi
}

get_eeprom_test_status()
{
	ret="Not Running"
	if [ $eeprom_pid -gt 0 ]
	then
		ret=$(cat $eeprom_test_status_file)
	fi
	echo "$ret"
}
