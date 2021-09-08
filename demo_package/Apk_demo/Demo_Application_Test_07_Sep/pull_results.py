import subprocess

subprocess.call("adb root",shell=True)
print("Capturing Results From the Test-Board")

                         
subprocess.call("adb pull /sdcard/stress_testing_dmesg_logs_082015252021.41.txt",shell=True)
subprocess.call("adb pull /sdcard/stress_testing_logs_082015252021.41.txt",shell=True)
subprocess.call("adb pull /data/data/com.einfochips.frl_wearable/files/eInfochips",shell=True)
print("Process done Successfully !!! ")



