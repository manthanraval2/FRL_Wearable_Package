import subprocess
print("Pushing the test utilities into the Test-Board")

subprocess.call("adb push alttest /data/local/tmp/.",shell=True)
subprocess.call("adb push gyrtest /data/local/tmp/.",shell=True)
subprocess.call("adb push acctest /data/local/tmp/.",shell=True)
subprocess.call("adb push temptest /data/local/tmp/.",shell=True)
print("Pushing the test script into the Test-Board")
subprocess.call("adb shell rm  /data/local/tmp/alt-time.txt",shell=True)
subprocess.call("adb shell rm  /data/local/tmp/gyrtest-time.txt",shell=True)
subprocess.call("adb shell rm  /data/local/tmp/temptest-time.txt",shell=True)
subprocess.call("adb shell rm  /data/local/tmp/acctest-time.txt",shell=True)

subprocess.call("adb push alt-sensor.sh /data/local/tmp/.",shell=True)
subprocess.call("adb push temp-sensor.sh /data/local/tmp/.",shell=True)
subprocess.call("adb push gyr-sensor.sh /data/local/tmp/.",shell=True)
subprocess.call("adb push acc-sensor.sh /data/local/tmp/.",shell=True)
subprocess.call("adb push startup.sh /data/local/tmp/.",shell=True)
print("Running the start up script into the Test-Board")
#subprocess.call("adb shell ./data/local/tmp/startup.sh & ",shell=True)

