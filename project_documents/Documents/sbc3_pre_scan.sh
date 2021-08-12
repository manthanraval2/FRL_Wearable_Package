#!/bin/sh

. ./sbc3_audio_capture_test.sh
. ./sbc3_audio_playback_test.sh
. ./sbc3_wifi_test.sh
. ./sbc3_eeprom_test.sh
. ./sbc3_testboard_i2c_test.sh
. ./sbc3_testboard_spi_test.sh
. ./sbc3_gpio_test.sh

# User Configurable variables --------------------------------------------------
CURR_DIR=$(pwd)

#Function to stop all the tests
stop_all_tests()
{
	#Stop Audio test
	test_audio_capture 2
	#Stop Audio Playback test
	test_audio_playback 2
	#stop Wifi test
	test_wifi 2
	#stop EEPROM Processor test
	test_eeprom 2
	#stop Test Board I2C test
	test_testboard_i2c 2
	#stop Test Board SPI test
	test_testboard_spi 2
	#stop Gpio test
	test_gpio 2
	#kill any stale process of busybox
	pkill busybox
}

#Function to start all the tests
start_all_tests()
{
	#Start Audio Capture test
	test_audio_capture 1
	#Start Audio Playback test
	test_audio_playback 1
	#Start the Wifi test
	test_wifi 1
	#Start the eeprom test
	test_eeprom 1
	#stop Test Board I2C test
	test_testboard_i2c 1
	#stop Test Board SPI test
	test_testboard_spi 1
	#Start the gpio test
	test_gpio 1
}

#Signal handler for SIGINT
sigint()
{
	stop_all_tests
	echo "signal INT received, script ending"
	exit 0
}

#Register signal handler for SIGINT
trap 'sigint'  INT

execute_shell_cmd()
{
	echo "Enter shell command :"
	read exe_cmd
	eval $exe_cmd
	return $?
}

#Read user input to start or stop the test
read_start_stop()
{
	echo "Enter 1 to start the test $1"
	echo "Enter 2 to stop the test $1"
	echo "=================================================================="
	read start_stop
	return $start_stop
}

#Function to print the test status
print_tests_status()
{
	status=$(get_audio_capture_test_status)
	echo "1. Audio Capture Test :" $status
	status=$(get_audio_playback_test_status)
	echo "2. Audio Playback Test :" $status
	status=$(get_wifi_test_status)
	echo "3. Wifi Test :" $status
	status=$(get_eeprom_test_status)
	echo "4. EEPROM Test :" $status
	status=$(get_testboard_i2c_test_status)
	echo "5. Test Board I2C Test :" $status
	status=$(get_testboard_spi_test_status)
	echo "6. Test Board SPI Test :" $status
	status=$(get_gpio_test_status)
	echo "7. Gpio Test :" $status
}

#Function to manually test the commands by
manual_user_test()
{
# Add the if else statement
	echo
	echo
	echo "=================================================================="
	echo "1. Audio Capture Test"
	echo "2. Audio Playback Test"
	echo "3. Wifi Test"
	echo "4. EEPROM Test"
	echo "5. Test Board I2C Test"
	echo "6. Test Board SPI Test"
	echo "7. Gpio Test"
	echo "8. Enter CTRL+D to confirm tests "
	echo "=================================================================="
	echo
	echo
	echo " Choose your multiple tests "

#Making a dynamic array to take no of tests
	tests=()
	while read -r input;
	do
		tests+=("$input")
	done

	test_len=${#tests[@]}
	if [ test_len -eq 0 ]
	then
		echo "No Tests Entered"
	else
		echo Starting the tests: ${tests[@]}

		test_started="$test_len"
		i=0
		while [ $test_started -ne 0 ]
		do
			if [[ ${tests[$i]} == 1 ]]
			then
				test_audio_capture 1

			elif [[ ${tests[$i]} == 2 ]]
			then
				test_audio_playback 1

			elif [[ ${tests[$i]} == 3 ]]
			then
				test_wifi 1

			elif [[ ${tests[$i]} == 4 ]]
			then
				test_eeprom 1

			elif [[ ${tests[$i]} == 5 ]]
			then
				test_testboard_i2c 1

			elif [[ ${tests[$i]} == 6 ]]
			then
				test_testboard_spi 1

			elif [[ ${tests[$i]} == 7 ]]
			then
				test_gpio 1
			fi

			test_started=`expr $test_started - 1`
			i=`expr $i + 1`
		done
	fi
}

main()
{
	#Proper arrangement of table
	svc power stayon true
	chmod +x busybox
	mkdir -p $LOG_DIR
	while [ 1 ]
	do
		echo "=================================================================="
		echo "1. Audio Capture Test"
		echo "2. Audio Playback Test"
		echo "3. Wifi Test"
		echo "4. EEPROM Test"
		echo "5. Test Board I2C Test"
		echo "6. Test Board SPI Test"
		echo "7. Gpio Test"
		echo "8. All Test"
		echo "9. Show status"
		echo "10.Manual user test"
		echo "11.Stop everthing and Exit"
		echo "=================================================================="
		echo "Choose your test:"
		read choice

		echo "You choose Test :$choice"
		echo "=================================================================="

		case $choice in
		    1)
				read_start_stop $choice
				#Start or stop audio capture test based on user input
				test_audio_capture $?;;
		    2)
				read_start_stop $choice
				#Start or stop audio play_back test on user input
				test_audio_playback $?;;

		    3)
				read_start_stop $choice
				#Start or stop wifi test on user input
				test_wifi $?;;

		    4)
				read_start_stop $choice
				#Start or stop eeprom-processor test on user input
				test_eeprom $?;;

		    5)
				read_start_stop $choice
				#Start or stop eeprom test on user input
				test_testboard_i2c $?;;

			6)
				read_start_stop $choice
				#Start or stop eeprom test on user input
				test_testboard_spi $?;;

		    7)
				read_start_stop $choice
				#Start or stop gpio test on user input
				test_gpio $?;;

		    8)
				#Start all tests
				start_all_tests;;

		    9)
				#Print status of all tests
				print_tests_status;;

		    10)
				#manually test command by user input
				manual_user_test;;

		    11)
				#stop all the tests
				echo "Stoping all tests"
				stop_all_tests
				exit 0;;

		    *)
		        echo "Wrong Choice....";;

		esac # end of case
	done #end of while
}

main
