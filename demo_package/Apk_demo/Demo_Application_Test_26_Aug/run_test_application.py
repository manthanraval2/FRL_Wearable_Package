import subprocess
import time
import json

''' Read configuration data from config.json file '''
with open('config.json') as f:
  data = json.load(f)

''' find max timeout''' 
max_timeout = int(data['sensor_pressure_timeout'])
    
if max_timeout < int(data['sensor_gyroscope_timeout']):
    max_timeout = int(data['sensor_gyroscope_timeout'])
    
if max_timeout < int(data['sensor_pedometer_timeout']):
    max_timeout = int(data['sensor_pedometer_timeout'])
    
if max_timeout < int(data['sensor_heartrate_timeout']):
    max_timeout = int(data['sensor_heartrate_timeout'])
    
if max_timeout < int(data['sensor_accelerometer_timeout']):
    max_timeout = int(data['sensor_accelerometer_timeout'])

if max_timeout < int(data['sensor_accelerometer_timeout']):
    max_timeout = int(data['sensor_accelerometer_timeout'])

if max_timeout < int(data['sensor_tilt_timeout']):
    max_timeout = int(data['sensor_tilt_timeout'])

if max_timeout < int(data['sensor_owd_timeout']):
    max_timeout = int(data['sensor_owd_timeout'])

if max_timeout < int(data['sensor_ppg_timeout']):
    max_timeout = int(data['sensor_ppg_timeout'])
    
if max_timeout < int(data['sensor_rri_timeout']):
    max_timeout = int(data['sensor_rri_timeout'])
    
if max_timeout < int(data['sensor_temp_timeout']):
    max_timeout = int(data['sensor_temp_timeout'])
    
if max_timeout < int(data['sensor_calorie_timeout']):
    max_timeout = int(data['sensor_calorie_timeout'])
    
if max_timeout < int(data['sensor_ott_timeout']):
    max_timeout = int(data['sensor_ott_timeout'])
    
if max_timeout < int(data['sensor_pdr_timeout']):
    max_timeout = int(data['sensor_pdr_timeout'])
    
timeout_sec = int(max_timeout/1000)
print("Maximum TImeout =" + str(timeout_sec)+" sec")

subprocess.call("adb root",shell=True)
print("Capturing Build Version on the Test-Board")
subprocess.call("adb shell getprop ro.build.description >> build_version.csv ",shell=True)

subprocess.call("adb install frl_wearable.apk",shell=True)
subprocess.call("adb push config.json /data/local/tmp/",shell=True)
print("launching the sensor activity of Application")
time.sleep(3)
subprocess.call("adb shell am start -n com.einfochips.frl_wearable/com.einfochips.frl_wearable.MainActivity",shell=True)

for x in range(0, timeout_sec):
    #send mocking commands from here
    subprocess.call('adb shell "mfg_tool mcu bbcmd shellcmd pedometer set"',shell=True)
    print("\033[F",end = '')
    
    subprocess.call('adb shell "mfg_tool mcu bbcmd shellcmd tilt_set"',shell=True)
    print("\033[F",end = '')
    
    subprocess.call('adb shell "mfg_tool mcu bbcmd shellcmd owd_set 1 1"',shell=True)
    print("\033[F",end = '')
    
    print("Seconds Remaining . . .",str(timeout_sec-x).zfill(5),end = '')
    print("\033[F")

    #send mocking command at every 1 sec
    time.sleep(0.5)

subprocess.call("adb pull /data/data/com.einfochips.frl_wearable/files/eInfochips",shell=True)
time.sleep(5)
#subprocess.call("adb uninstall com.einfochips.frl_wearable",shell=True)

print("Process done Sucessfully !!! ")
print("opening the logs in html page !!!")

subprocess.call("python3 createHTML.py",shell=True)
