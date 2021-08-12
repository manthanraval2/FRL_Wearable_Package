import subprocess
import time
subprocess.call("adb root",shell=True)
print("Capturing Build Version on the Test-Board")
subprocess.call("adb shell getprop ro.build.description >> build_version.csv ",shell=True)

subprocess.call("adb install frl_wearable.apk",shell=True)
subprocess.call("adb push config.json /data/local/tmp/",shell=True)
print("launching the sensor activity of Application")
time.sleep(5)
#subprocess.call("adb shell am start -n com.example.test_pressure/com.example.test_pressure.MainActivity",shell=True)
subprocess.call("adb shell am start -n com.einfochips.frl_wearable/com.einfochips.frl_wearable.MainActivity",shell=True)
time.sleep(10)
#subprocess.call("adb pull /data/data/com.example.test_pressure/files/eInfochips/Alt_Results.csv",shell=True)
subprocess.call("adb pull /data/data/com.einfochips.frl_wearable/files/eInfochips/Hrm_Results.csv",shell=True)
subprocess.call("adb uninstall com.einfochips.frl_wearable",shell=True)

print("Process done Sucessfully !!! ")
print("opening the logs in html page !!!")

subprocess.call("python3 createHTML.py",shell=True)


