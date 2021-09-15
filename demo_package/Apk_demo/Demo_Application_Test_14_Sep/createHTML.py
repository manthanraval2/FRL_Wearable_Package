# write-html.py
import webbrowser
import csv
import os.path
from os import path

''' File Naming '''
build_version_file = 'build_version.csv'
pressure_file_name = 'eInfochips/Alt_Results.csv'
hrm_file_name = 'eInfochips/Hrm_Results.csv'
gyro_file_name = 'eInfochips/Gyr_Results.csv'
acc_file_name = 'eInfochips/Acc_Results.csv'
pedo_file_name = 'eInfochips/Ped_Results.csv'
tilt_file_name = 'eInfochips/Tilt_Results.csv'
owd_file_name = 'eInfochips/Owd_Results.csv'
ppg_file_name = 'eInfochips/Ppg_Results.csv'
rri_file_name = 'eInfochips/Rri_Results.csv'
temp_file_name = 'eInfochips/Temp_Results.csv'
cal_file_name = 'eInfochips/Cal_Results.csv'
ott_file_name = 'eInfochips/Ott_Results.csv'
pdr_file_name = 'eInfochips/Pdr_Results.csv'
sgm_file_name = 'eInfochips/Sgm_Results.csv'
hrv_file_name = 'eInfochips/Hrv_Results.csv'
adt_file_name = 'eInfochips/Adt_Results.csv'

Fail_Message = "FAIL"
Pass_Message = "PASS"

def isExist(file_name):
    if (path.exists(file_name)):
        print("File: "+file_name+" present")
        if (os.stat(file_name).st_size == 0):
            print("FILE: "+file_name+" is empty")   
            return False
        else:
            return True
    else:
        print("File: "+file_name+" not exists")
        return False

def build_file_empty():
    parse_build_version.device_build_type = 0
    parse_build_version.build_version_release = 0 
    parse_build_version.build_id = 0

def alt_file_empty():
    parse_alt_sensor.altpressure_val = 0
    parse_alt_sensor.alttimestamp_ns = 0
    
def hrm_file_empty():
    parse_alt_sensor.altpressure_val = 0
    parse_alt_sensor.alttimestamp_ns = 0
    
def gyro_file_empty():
    parse_gyro_sensor.gyr_timestamp_ns = 0
    parse_gyro_sensor.gyr_x_val = 0
    parse_gyro_sensor.gyr_y_val = 0
    parse_gyro_sensor.gyr_z_val = 0

def acc_file_empty():
    parse_acc_sensor.acc_timestamp_ns = 0
    parse_acc_sensor.acc_x_val = 0
    parse_acc_sensor.acc_y_val = 0
    parse_acc_sensor.acc_z_val = 0
    
def pedo_file_empty():
    parse_pedo_sensor.ped_timestamp_ns = 0
    parse_pedo_sensor.ped_steps = 0

def tilt_file_empty():
    parse_tilt_sensor.tilt_timestamp_ns = 0
    parse_tilt_sensor.tilt_tiltVal = 0

def owd_file_empty():
    parse_owd_sensor.owd_timestamp_ns = 0
    parse_owd_sensor.owd_prox = 0
    parse_owd_sensor.owd_cradle = 0
    
def ppg_file_empty():
    parse_ppg_sensor.ppg_timestamp_ns = 0
    parse_ppg_sensor.ppg_frame = 0
    parse_ppg_sensor.ppg_ir_val_1 = 0
    parse_ppg_sensor.ppg_ir_val_2 = 0
    parse_ppg_sensor.ppg_red_val_1 = 0
    parse_ppg_sensor.ppg_red_val_2 = 0
    parse_ppg_sensor.ppg_green_val_1 = 0
    parse_ppg_sensor.ppg_green_val_2 = 0

def rri_file_empty():
    parse_rri_sensor.rri_timestamp_ns = 0
    parse_rri_sensor.rri_Msg_interval_ms = 0
    parse_rri_sensor.rri_Msg_peak_ms = 0
    
def temp_file_empty():
    parse_temp_sensor.temp_timestamp_ns = 0
    parse_temp_sensor.temp_sensor = 0
    parse_temp_sensor.temp_value = 0

def cal_file_empty():
    parse_cal_sensor.cal_timestamp_ns = 0
    parse_cal_sensor.cal_value = 0

def ott_file_empty():
    parse_ott_sensor.ott_timestamp_ns = 0
    parse_ott_sensor.ott_bytes = 0

def pdr_file_empty():
    parse_pdr_sensor.pdr_timestamp_ns = 0
    parse_pdr_sensor.pdr_sensor_position_update= 0
    parse_pdr_sensor.pdr_positionUpdateMessage_x = 0
    parse_pdr_sensor.pdr_positionUpdateMessage_y = 0
    parse_pdr_sensor.pdr_positionUpdateMessage_z = 0
    
def sgm_file_empty():
    parse_sgm_sensor.sgm_timestamp_ns = 0
    parse_sgm_sensor.sgm_sensor_scalar_update= 0

def hrv_file_empty():
    parse_hrv_sensor.hrv_timestamp_ns = 0
    parse_hrv_sensor.hrv_sensor_hrv_update= 0
    parse_hrv_sensor.hrv_sensor_hr_update= 0
    parse_hrv_sensor.hrv_sensor_interval_update= 0
    parse_hrv_sensor.hrv_sensor_coverage_update= 0
    parse_hrv_sensor.hrv_sensor_samples_update= 0
    parse_hrv_sensor.hrv_sensor_gaps_update= 0
    parse_hrv_sensor.hrv_sensor_method_update= 0

def adt_file_empty():
    parse_adt_sensor.adt_timestamp_ns = 0
    parse_adt_sensor.adt_activity= 0

def parse_build_version():
    parse_build_version.device_build_type = "0"
    parse_build_version.build_version_release = "0"
    parse_build_version.build_id = "0"
    parse_build_version.build_version_incremental = "0"
    if(isExist(build_version_file)):
        with open(build_version_file, 'rt') as Version:
            version_data = csv.reader(Version, delimiter="\t")
            for version_data_row in version_data:
                list_data_version = version_data_row[0].split()
                parse_build_version.device_build_type = list_data_version[0]
                parse_build_version.build_version_release = list_data_version[1]
                parse_build_version.build_id = list_data_version[2]
                parse_build_version.build_version_incremental = list_data_version[3]
    else:
        if (len(parse_build_version.device_build_type) == 0 or len(parse_build_version.build_version_release) == 0 or len(parse_build_version.build_id) == 0 or len(parse_build_version.build_version_incremental) == 0):
            build_file_empty()
        
def parse_alt_sensor():
    '''Alt Sensor schema'''
    parse_alt_sensor.altpressure_val = "0"
    parse_alt_sensor.alttimestamp_ns = "0"
    
    if (isExist(pressure_file_name)):
        with open(pressure_file_name, 'rt') as AltData:
            altdata = csv.reader(AltData)
            for altrow in altdata:
                pass
            parse_alt_sensor.alttimestamp_ns = altrow[1]
            parse_alt_sensor.altpressure_val = altrow[3]
    else:
        if (len(parse_alt_sensor.alttimestamp_ns) == 0 or len(parse_alt_sensor.alttimestamp_ns) == 0):
            alt_file_empty()

def parse_hrm_sensor():
    parse_hrm_sensor.hrm_timestamp_ns = "0"
    parse_hrm_sensor.hrm_bmp = "0"
    
    if (isExist(hrm_file_name)):
        with open(hrm_file_name, 'rt') as HrmData:
            hrmdata = csv.reader(HrmData)
            for hrmrow in hrmdata:
                pass
            parse_hrm_sensor.hrm_timestamp_ns = hrmrow[1]
            parse_hrm_sensor.hrm_bmp = hrmrow[3]
    else:
        if (len(parse_hrm_sensor.hrm_timestamp_ns) == 0 or len(parse_hrm_sensor.hrm_bmp) == 0):
            hrm_file_empty()
            
               
def parse_gyro_sensor():
    '''Gyro Sensor schema'''
    parse_gyro_sensor.gyr_timestamp_ns = "0"
    parse_gyro_sensor.gyr_x_val = "0"
    parse_gyro_sensor.gyr_y_val = "0"
    parse_gyro_sensor.gyr_z_val = "0"
    
    if(isExist(gyro_file_name)):
        with open(gyro_file_name, 'rt') as GyrData:
            gyrdata = csv.reader(GyrData)
            for gyrrow in gyrdata:
                pass
            parse_gyro_sensor.gyr_timestamp_ns = gyrrow[1]
            parse_gyro_sensor.gyr_x_val = gyrrow[3]
            parse_gyro_sensor.gyr_y_val = gyrrow[5]
            parse_gyro_sensor.gyr_z_val = gyrrow[7]
    else:
        if (len(parse_gyro_sensor.gyr_timestamp_ns) == 0 or len(parse_gyro_sensor.gyr_x_val) == 0 or len(parse_gyro_sensor.gyr_y_val) == 0 or len(parse_gyro_sensor.gyr_z_val) == 0):
            gyro_file_empty()
            
def parse_acc_sensor():
    '''Accelerometer Sensor schema'''
    parse_acc_sensor.acc_timestamp_ns = "0"
    parse_acc_sensor.acc_x_val = "0"
    parse_acc_sensor.acc_y_val = "0"
    parse_acc_sensor.acc_z_val = "0"
    
    if(isExist(acc_file_name)):
        with open(acc_file_name, 'rt') as AccData:
            accdata = csv.reader(AccData)
            for accrow in accdata:
                pass
            parse_acc_sensor.acc_timestamp_ns = accrow[1]
            parse_acc_sensor.acc_x_val = accrow[3]
            parse_acc_sensor.acc_y_val = accrow[5]
            parse_acc_sensor.acc_z_val = accrow[7]
    else:
        if (len(parse_acc_sensor.acc_timestamp_ns) == 0 or len(parse_acc_sensor.acc_x_val) == 0 or len(parse_acc_sensor.acc_y_val) == 0 or len(parse_acc_sensor.acc_z_val) == 0):
            acc_file_empty()
          
def parse_pedo_sensor():
    '''Pedometer Sensor schema'''
    parse_pedo_sensor.ped_timestamp_ns = "0"
    parse_pedo_sensor.ped_steps = "0"
    
    if(isExist(pedo_file_name)):
        with open(pedo_file_name, 'rt') as PedData:
            peddata = csv.reader(PedData)
            for pedrow in peddata:
                pass
            parse_pedo_sensor.ped_timestamp_ns = str(pedrow[1])
            parse_pedo_sensor.ped_steps = str(pedrow[3])
    else:
        if(len(parse_pedo_sensor.ped_timestamp_ns) == 0 or len(parse_pedo_sensor.ped_steps) == 0):
            pedo_file_empty()

def parse_tilt_sensor():
    '''Tilt Sensor schema'''
    parse_tilt_sensor.tilt_timestamp_ns = "0"
    parse_tilt_sensor.tilt_tiltVal = "0"
    
    if(isExist(tilt_file_name)):
        with open(tilt_file_name, 'rt') as TiltData:
            tiltdata = csv.reader(TiltData)
            for tiltrow in tiltdata:
                pass
            parse_tilt_sensor.tilt_timestamp_ns = tiltrow[1]
            parse_tilt_sensor.tilt_tiltVal = tiltrow[3]
    else:
        if (len(parse_tilt_sensor.tilt_timestamp_ns) == 0 or len(parse_tilt_sensor.tilt_tiltVal) == 0):
            tilt_file_empty()

def parse_owd_sensor():
    '''OnWristDetection Sensor schema'''
    parse_owd_sensor.owd_timestamp_ns = "0"
    parse_owd_sensor.owd_prox = "0"
    parse_owd_sensor.owd_cradle = "0"
    
    if(isExist(owd_file_name)):
        with open(owd_file_name, 'rt') as OwdData:
            owddata = csv.reader(OwdData)
            for owdrow in owddata:
                pass
            parse_owd_sensor.owd_timestamp_ns = owdrow[1]
            parse_owd_sensor.owd_prox = owdrow[3]
            parse_owd_sensor.owd_cradle = owdrow[5]
    else:
        if (len(parse_owd_sensor.owd_timestamp_ns) == 0 or len(parse_owd_sensor.owd_prox) == 0 or len(parse_owd_sensor.owd_cradle) == 0):
            owd_file_empty()
            
def parse_ppg_sensor():
    '''PPG Sensor schema'''
    parse_ppg_sensor.ppg_timestamp_ns = "0"
    parse_ppg_sensor.ppg_frame = "0"
    parse_ppg_sensor.ppg_ir_val_1 = "0"
    parse_ppg_sensor.ppg_ir_val_2 = "0"
    parse_ppg_sensor.ppg_red_val_1 = "0"
    parse_ppg_sensor.ppg_red_val_2 = "0"
    parse_ppg_sensor.ppg_green_val_1 = "0"
    parse_ppg_sensor.ppg_green_val_2 = "0"
    
    if(isExist(ppg_file_name)):
        with open(ppg_file_name, 'rt') as PpgData:
            ppgdata = csv.reader(PpgData)
            for ppgrow in ppgdata:
                pass
            parse_ppg_sensor.ppg_timestamp_ns = ppgrow[1]
            parse_ppg_sensor.ppg_frame = ppgrow[3]
            parse_ppg_sensor.ppg_ir_val_1 = ppgrow[5]
            parse_ppg_sensor.ppg_ir_val_2 = ppgrow[7]
            parse_ppg_sensor.ppg_red_val_1 = ppgrow[9]
            parse_ppg_sensor.ppg_red_val_2 = ppgrow[11]
            parse_ppg_sensor.ppg_green_val_1 = ppgrow[13]
            parse_ppg_sensor.ppg_green_val_2 = ppgrow[15]
    else:
        if (len(parse_ppg_sensor.ppg_timestamp_ns) == 0 or len(parse_ppg_sensor.ppg_frame) == 0 or len(parse_ppg_sensor.ppg_ir_val_1) == 0 or len(parse_ppg_sensor.ppg_ir_val_2) == 0 or len(parse_ppg_sensor.ppg_red_val_1) == 0 or len(parse_ppg_sensor.ppg_red_val_2) == 0):
            ppg_file_empty()

def parse_rri_sensor():
    '''RRI Sensor schema'''
    parse_rri_sensor.rri_timestamp_ns = "0"
    parse_rri_sensor.rri_Msg_interval_ms = "0"
    parse_rri_sensor.rri_Msg_peak_ms = "0"
    
    if(isExist(rri_file_name)):
        with open(rri_file_name, 'rt') as RriData:
            rridata = csv.reader(RriData)
            for rrirow in rridata:
                pass
            parse_rri_sensor.rri_timestamp_ns = rrirow[1]
            parse_rri_sensor.rri_Msg_interval_ms = rrirow[3]
            parse_rri_sensor.rri_Msg_peak_ms = rrirow[5]
    else:
        if (len(parse_rri_sensor.rri_timestamp_ns) == 0 or len(parse_rri_sensor.rri_Msg_interval_ms) == 0 or len(parse_rri_sensor.rri_Msg_peak_ms) == 0):
            rri_file_empty()

def parse_temp_sensor():
    '''Temp Sensor schema'''
    parse_temp_sensor.temp_timestamp_ns = "0"
    parse_temp_sensor.temp_sensor = "0"
    parse_temp_sensor.temp_value = "0"
    
    if(isExist(temp_file_name)):
        with open(temp_file_name, 'rt') as TempData:
            tempdata = csv.reader(TempData)
            for temprow in tempdata:
                pass
            parse_temp_sensor.temp_timestamp_ns = temprow[1]
            parse_temp_sensor.temp_sensor = temprow[3]
            parse_temp_sensor.temp_value = temprow[5]
            
    else:
        if (len(parse_temp_sensor.temp_timestamp_ns) == 0 or len(parse_temp_sensor.temp_sensor) == 0 or len(parse_temp_sensor.temp_value) == 0):
            temp_file_empty()

def parse_cal_sensor():
    '''Cal Sensor schema'''
    parse_cal_sensor.cal_timestamp_ns = "0"
    parse_cal_sensor.cal_value = "0"
    
    if(isExist(cal_file_name)):
        with open(cal_file_name, 'rt') as CalData:
            caldata = csv.reader(CalData)
            for calrow in caldata:
                pass
            parse_cal_sensor.cal_timestamp_ns = calrow[1]
            parse_cal_sensor.cal_value = calrow[3]
    else:
        if (len(parse_cal_sensor.cal_timestamp_ns) == 0 or len(parse_cal_sensor.cal_value) == 0):
            cal_file_empty()

def parse_ott_sensor():
    '''Ott Sensor schema'''
    parse_ott_sensor.ott_timestamp_ns = "0"
    parse_ott_sensor.ott_bytes = "0"
    
    if(isExist(ott_file_name)):
        with open(ott_file_name, 'rt') as OttData:
            ottdata = csv.reader(OttData)
            for ottrow in ottdata:
                pass
            parse_ott_sensor.ott_timestamp_ns = ottrow[1]
            parse_ott_sensor.ott_bytes = ottrow[3]
    else:
        if (len(parse_ott_sensor.ott_timestamp_ns) == 0 or len(parse_ott_sensor.ott_bytes) == 0):
            ott_file_empty()
  
def parse_pdr_sensor():
    '''PedestrianDeadReckoning Sensor schema'''
    parse_pdr_sensor.pdr_timestamp_ns = "0"
    parse_pdr_sensor.pdr_sensor_position_update= "0"
    parse_pdr_sensor.pdr_positionUpdateMessage_x = "0"
    parse_pdr_sensor.pdr_positionUpdateMessage_y = "0"
    parse_pdr_sensor.pdr_positionUpdateMessage_z = "0"
    
    if(isExist(pdr_file_name)):
        with open(pdr_file_name, 'rt') as PdrData:
            pdrdata = csv.reader(PdrData)
            for pdrrow in pdrdata:
                pass
            parse_pdr_sensor.pdr_timestamp_ns = pdrrow[1]
            parse_pdr_sensor.pdr_sensor_position_update = pdrrow[3]
            parse_pdr_sensor.pdr_positionUpdateMessage_x = pdrrow[5]
            parse_pdr_sensor.pdr_positionUpdateMessage_y = pdrrow[7]
            parse_pdr_sensor.pdr_positionUpdateMessage_z = pdrrow[9]
            
    else:
        if (len(parse_pdr_sensor.pdr_timestamp_ns) == 0 or len(parse_pdr_sensor.pdr_sensor_position_update) == 0 or len(parse_pdr_sensor.pdr_positionUpdateMessage_x) == 0 or len(parse_pdr_sensor.pdr_positionUpdateMessage_y) == 0 or len(parse_pdr_sensor.pdr_positionUpdateMessage_z) == 0):
            pdr_file_empty()

def parse_sgm_sensor():
    '''Significant motion virtual Sensor schema'''
    parse_sgm_sensor.sgm_timestamp_ns = "0"
    parse_sgm_sensor.sgm_sensor_scalar_update= "0"
    
    if(isExist(sgm_file_name)):
        with open(sgm_file_name, 'rt') as SgmData:
            sgmdata = csv.reader(SgmData)
            for sgmrow in sgmdata:
                pass
            parse_sgm_sensor.sgm_timestamp_ns = sgmrow[1]
            parse_sgm_sensor.sgm_sensor_scalar_update = sgmrow[3]
            
    else:
        if (len(parse_sgm_sensor.sgm_timestamp_ns) == 0 or len(parse_sgm_sensor.sgm_sensor_scalar_update) == 0):
            sgm_file_empty()
            
def parse_hrv_sensor():
    '''HRV RMSSD virtual Sensor schema'''
    parse_hrv_sensor.hrv_timestamp_ns = "0"
    parse_hrv_sensor.hrv_sensor_hrv_update = "0"
    parse_hrv_sensor.hrv_sensor_hr_update = "0"
    parse_hrv_sensor.hrv_sensor_interval_update = "0"
    parse_hrv_sensor.hrv_sensor_coverage_update = "0"
    parse_hrv_sensor.hrv_sensor_samples_update = "0"
    parse_hrv_sensor.hrv_sensor_gaps_update = "0"
    parse_hrv_sensor.hrv_sensor_method_update = "0"
    
    if(isExist(hrv_file_name)):
        with open(hrv_file_name, 'rt') as HrvData:
            hrvdata = csv.reader(HrvData)
            for hrvrow in hrvdata:
                pass
            parse_hrv_sensor.hrv_timestamp_ns = hrvrow[1]
            parse_hrv_sensor.hrv_sensor_hrv_update = hrvrow[3]
            parse_hrv_sensor.hrv_sensor_hr_update = hrvrow[5]
            parse_hrv_sensor.hrv_sensor_interval_update = hrvrow[7]
            parse_hrv_sensor.hrv_sensor_coverage_update = hrvrow[9]
            parse_hrv_sensor.hrv_sensor_samples_update = hrvrow[11]
            parse_hrv_sensor.hrv_sensor_gaps_update = hrvrow[13]
            parse_hrv_sensor.hrv_sensor_method_update = hrvrow[15]
            
    else:
        if (len(parse_hrv_sensor.hrv_timestamp_ns) == 0 or len(parse_hrv_sensor.hrv_sensor_hrv_update) == 0 or len(parse_hrv_sensor.hrv_sensor_hr_update) == 0 or len(parse_hrv_sensor.hrv_sensor_interval_update) == 0):
            hrv_file_empty()

def parse_adt_sensor():
    '''ActivityDetection Sensor schema'''
    parse_adt_sensor.adt_timestamp_ns = "0"
    parse_adt_sensor.adt_activity= "0"
    
    if(isExist(adt_file_name)):
        with open(adt_file_name, 'rt') as AdtData:
            adtdata = csv.reader(AdtData)
            for adtrow in adtdata:
                pass
            parse_adt_sensor.adt_timestamp_ns = adtrow[1]
            parse_adt_sensor.adt_sensor_position_update = adtrow[3]
            
    else:
        if (len(parse_adt_sensor.adt_timestamp_ns) == 0 or len(parse_adt_sensor.adt_activity) == 0):
            adt_file_empty()
             
if __name__ == "__main__":
    parse_build_version()
    parse_alt_sensor()
    parse_hrm_sensor()
    parse_gyro_sensor()
    parse_acc_sensor()
    parse_pedo_sensor()
    parse_tilt_sensor()    
    parse_owd_sensor() 
    parse_ppg_sensor()
    parse_rri_sensor()  
    parse_temp_sensor() 
    parse_cal_sensor() 
    parse_ott_sensor()
    parse_pdr_sensor()
    parse_sgm_sensor() 
    parse_hrv_sensor()
    parse_adt_sensor()

f = open('FRL_Test_Report.html','w')
message = """
    <html><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
            <style>
              table, tr, td, th{
              border: 1px solid black;
              border-collapse: collapse;
              padding: 5px;
              }
                                  
            </style>

            <style type="text/css">

            .test-result-table {

    #            border: 1px solid black;
                width: 800px;
            }

            .test-result-table-header-cell {

    #            border-bottom: 1px solid black;
                background-color: grey;
                color: white;
            }

            .test-result-step-command-cell {

    #            border-bottom: 1px solid black;
            }

            .test-result-step-description-cell {

    #            border-bottom: 1px solid black;
            }

            .test-result-step-result-cell-ok {
    #            border-bottom: 1px solid black;
                font-size: 20px;
                font-weight: bold;
            }

            .test-result-step-result-cell-failure {

                color: red;
    #            border-bottom: 1px solid black;
                background-color:  #f7dc6f;
                <!-- background-color: red; -->
            }

            .test-result-step-result-cell-notperformed {

    #            border-bottom: 1px solid gray;
                background-color: white;
            }

            .test-result-describe-cell {
                background-color: tan;
                font-style: italic;
            }

            .test-result-step-result-cell-ok {
                color: green;
    #            border-bottom: 1px solid black;
                background-color:  #f7dc6f;
                font-size: 20px;
            }
            
            .center {
              margin-left: auto;
              margin-right: auto;
            }

            .left {
              margin-left: 0;
            }

            .right {
              margin-right: 10;
            }

            .summary-table-data {
                background-color:powderblue; 
                color:black;
                font-weight: bold;
                font-family:verdana; 
            }
            
            .test-result-step-row test-result-step-row-altone {
                color:black;
            }
            
            # result{
            font-weight: bold;
            }

            </style>
        </head>
        <body>
            <h1 class="test-results-header">
                <center>Test Report</center>
            </h1>

    <div style="overflow-x:auto;">
            <table style="width:100%">
                <tbody><tr>
                    <td class="summary-table-data"> Project Name </td>
                    <td class="summary-table-data"> Wearable Device-FRL  </td>                
                </tr>
                <tr>
                    <td class="summary-table-data"> Test Type </td>
                    <td class="summary-table-data"> API Testing </td>                
                </tr>
                <tr>
                    <td rowspan="5" class="summary-table-data"> Test Build Version of Board </td>
                    <tr>
                        <td class="summary-table-data"> device_build_type:"""+parse_build_version.device_build_type+""" </td>
                    
                    </tr>
                    <tr>
                        <td class="summary-table-data"> build_version_release:"""+parse_build_version.build_version_release+""" </td>
                    </tr>
                    <tr>
                        <td class="summary-table-data"> build_id:"""+parse_build_version.build_id+""" </td>
                    </tr>
                    <tr>
                        <td class="summary-table-data"> build_version_incremental:"""+parse_build_version.build_version_incremental+""" </td>
                    </tr>               
                </tr>
                <tr>
                    <td class="summary-table-data"> Date &amp; Time </td>
                    <td class="summary-table-data">
                        <p>
                            <span id="datetime">23.07.2021 11:49</span>
                              <script>
                                var dt = new Date();
                                document.getElementById("datetime").innerHTML = (("0"+dt.getDate()).slice(-2)) +"."+ (("0"+ (dt.getMonth()+1)).slice(-2)) +"."+ (dt.getFullYear()) +" "+ (("0"+dt.getHours()).slice(-2)) +":"+(("0"+dt.getMinutes()).slice(-2));
                              </script>
                        </p>
                    </td>
                                  
                </tr>
                <tr>
                    <td class="summary-table-data"> 						
                        Pass 
                    </td>
                    <td class="summary-table-data"> 
                        16
                    </td>                 	
                </tr>
                <tr>
                    <td class="summary-table-data"> 						
                        Fail 
                    </td>
                    </td><td class="summary-table-data"> 
                        0
                    </td>                   	
                </tr>
                <tr>
                    <td class="summary-table-data"> 
                        Not Executed 
                    </td>
                    <td class="summary-table-data"> 
                        0 
                    </td>                
                </tr>
                <tr>
                    <td class="summary-table-data"> 
                        Total 
                    </td>
                    <td class="summary-table-data"> 
                        16
                    </td>               
                </tr>
            </tbody></table>

            <table class="test-result-table" style="width:100%" cellspacing="0">
                    <thead><tr>
                        <th class="test-result-table-header-cell">
                            Sensor Name
                        </th>
                        <th class="test-result-table-header-cell">
                            Description
                        </th>
                        <th class="test-result-table-header-cell">
                            Called API's
                        </th>
                        <th class="test-result-table-header-cell" colspan="2">
                            Sensor's Data
                        </th>
                        <th class="test-result-table-header-cell" >
                            Result
                        </th>              
                        <th class="test-result-table-header-cell">
                            Log File
                        </th>
                    </tr>
                </thead>

                <tbody>
                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> ALT </td>
                        <td rowspan="2"> To Validate ALT Pressure Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > t_stamp </td>
                        <td > """ +parse_alt_sensor.alttimestamp_ns  +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Alt_Results.csv"> Alt_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(Sensor.TYPE_PRESSURE) </td> 
                        <td> hPa </td>
                        <td> """+parse_alt_sensor.altpressure_val +""" </td>
                     </tr>
                                        
                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Heart-Rate </td>
                        <td rowspan="2"> To Validate Heart-Rate Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_hrm_sensor.hrm_timestamp_ns +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Hrm_Results.csv"> Hrm_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(Sensor.TYPE_HEART_RATE) </td> 
                        <td> bmp </td>
                        <td> """+ parse_hrm_sensor.hrm_bmp +""" </td>
                     </tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="4" class="test-result-step-command-cell"> Gyroscope </td>
                        <td rowspan="4"> To Validate Gyroscope Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_gyro_sensor.gyr_timestamp_ns +"""	</td>
                        <td rowspan="4" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="4">
                                    <a href="eInfochips/Gyr_Results.csv"> Gyr_Results.csv </a> </td>    
                    </tr>
                    <tr>
                        <td> x_val </td>
                        <td> """+parse_gyro_sensor.gyr_x_val+""" </td>
                    </tr>
                                
                    <tr>
                        <td rowspan="2"> getDefaultSensor(Sensor.TYPE_GYROSCOPE) </td> 
                        <td> y_val </td>
                        <td> """+ parse_gyro_sensor.gyr_y_val +""" </td>
                    </tr>
                    <tr>
                        <td> z_val </td>
                        <td> """+parse_gyro_sensor.gyr_z_val+""" </td>
                    </tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="4" class="test-result-step-command-cell"> Accelerometer </td>
                        <td rowspan="4"> To Validate Accelerometer Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_acc_sensor.acc_timestamp_ns +"""	</td>
                        <td rowspan="4" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="4">
                                    <a href="eInfochips/Acc_Results.csv"> Acc_Results.csv </a> </td>    
                    </tr>
                    <tr>
                        <td> x_val </td>
                        <td> """+parse_acc_sensor.acc_x_val+""" </td>
                    </tr>
                                
                    <tr>
                        <td rowspan="2"> getDefaultSensor(Sensor.TYPE_ACCELEROMETER) </td> 
                        <td> y_val </td>
                        <td> """+parse_acc_sensor.acc_y_val +""" </td>
                    </tr>
                    <tr>
                        <td> z_val </td>
                        <td> """+parse_acc_sensor.acc_z_val+""" </td>
                    </tr>
                                        
                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Pedometer </td>
                        <td rowspan="2"> To Validate Pedometer Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ +parse_pedo_sensor.ped_timestamp_ns +""" </td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Ped_Results.csv"> Ped_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(Sensor.TYPE_STEP_COUNTER) </td> 
                        <td> steps </td>
                        <td> """+parse_pedo_sensor.ped_steps+""" </td>
                     </tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Tilt Sensor </td>
                        <td rowspan="2"> To Validate Tilt Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_tilt_sensor.tilt_timestamp_ns +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Tilt_Results.csv"> Tilt_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(26) </td> 
                        <td> tiltVal </td>
                        <td> """+ parse_tilt_sensor.tilt_tiltVal +""" </td>
                    </tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="3" class="test-result-step-command-cell"> OnWristDetection </td>
                        <td rowspan="3"> To Validate OnWristDetection Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_owd_sensor.owd_timestamp_ns +"""	</td>
                        <td rowspan="3" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="3">
                                    <a href="eInfochips/Owd_Results.csv"> Owd_Results.csv </a> </td>    
                    </tr>
                    <tr>
                        <td> owd_prox </td>
                        <td> """+parse_owd_sensor.owd_prox+""" </td>
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(65544) </td> 
                        <td> owd_cradle </td>
                        <td> """+parse_owd_sensor.owd_cradle +""" </td>
                    </tr>
                    
                   <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="8" class="test-result-step-command-cell"> PPG Sensor </td>
                        <td rowspan="8"> To Validate PPG Sensor </td>
                        <td rowspan="4"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_ppg_sensor.ppg_timestamp_ns + """	</td>
                        <td rowspan="8" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="8">
                                    <a href="eInfochips/Ppg_Results.csv"> Ppg_Results.csv </a> </td>  
                    </tr>
						<tr>
							<td> ppg_frame </td>
							<td> """ +parse_ppg_sensor.ppg_frame +""" </td>
						</tr>  
						<tr>
							<td> ppg_ir_val_1 </td>
							<td> """+parse_ppg_sensor.ppg_ir_val_1+""" </td>
						</tr>
						<tr>
							<td> ppg_ir_val_2 </td>
							<td> """+parse_ppg_sensor.ppg_ir_val_2+""" </td>
						</tr>
					
								
						<tr>
							<td rowspan="4"> getDefaultSensor(65541) </td> 
							<td> ppg_red_val_1 </td>
							<td> """+parse_ppg_sensor.ppg_red_val_1+""" </td>
						</tr>
						<tr>
							<td> ppg_red_val_2 </td>
							<td> """+parse_ppg_sensor.ppg_red_val_2+""" </td>
						</tr>
						
						<tr>
							<td> ppg_green_val_1 </td>
							<td> """+parse_ppg_sensor.ppg_green_val_1+""" </td>
						</tr>
						<tr>
							<td> ppg_green_val_2 </td>
							<td> """+parse_ppg_sensor.ppg_green_val_2+""" </td>
						</tr>

					<tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="3" class="test-result-step-command-cell"> Beat to Beat(RRI) Sensor </td>
                        <td rowspan="3"> To Validate RRI Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """+parse_rri_sensor.rri_timestamp_ns+"""	</td>
                        <td rowspan="3" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="3">
                                    <a href="eInfochips/Rri_Results.csv"> Rri_Results.csv </a> </td>    
                    </tr>
                    
						<tr>
							<td> rri_Msg_interval_ms </td>
							<td> """+parse_rri_sensor.rri_Msg_interval_ms+""" </td>
						</tr>  		
						<tr>
							<td rowspan="1"> getDefaultSensor(65539) </td> 
							<td> rri_Msg_peak_ms </td>
							<td> """+parse_rri_sensor.rri_Msg_peak_ms+""" </td>
						</tr>
												
					<tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="3" class="test-result-step-command-cell"> Temperature Debug Virtual Sensor </td>
                        <td rowspan="3"> To Validate Temperature Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """+parse_temp_sensor.temp_timestamp_ns+"""	</td>
                        <td rowspan="3" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="3">
                                    <a href="eInfochips/Temp_Results.csv"> Temp_Results.csv </a> </td>    
                    </tr>
                    
						<tr>
							<td> Sensor Id </td>
							<td> """+parse_temp_sensor.temp_sensor+""" </td>
						</tr>  		
						<tr>
							<td rowspan="1"> getDefaultSensor(65543) </td> 
							<td> Temp (fahrenheit) </td>
							<td> """+parse_temp_sensor.temp_value+""" </td>
						</tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Calorie Sensor </td>
                        <td rowspan="2"> To Validate Calorie Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """ + parse_cal_sensor.cal_timestamp_ns +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Cal_Results.csv"> Cal_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(65540) </td> 
                        <td> cal_value </td>
                        <td> """+ parse_cal_sensor.cal_value +""" </td>
                    </tr>

                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> OTT </td>
                        <td rowspan="2"> To Validate OTT Pressure Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > t_stamp </td>
                        <td > """ +parse_ott_sensor.ott_timestamp_ns  +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Ott_Results.csv"> Ott_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(65545) </td> 
                        <td> ott_data_bytes </td>
                        <td> """+parse_ott_sensor.ott_bytes +""" </td>
                     </tr>    

    		    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="5" class="test-result-step-command-cell"> PedestrianDeadReckoning Sensor </td>
                        <td rowspan="5"> To Validate PedestrianDeadReckoning Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """+parse_pdr_sensor.pdr_timestamp_ns+"""	</td>
                        <td rowspan="5" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="5">
                                    <a href="eInfochips/Pdr_Results.csv"> Pdr_Results.csv </a> </td>    
                    </tr>
                    
                    <tr>
                        <td> Sensor Position Update </td>
                        <td> """+parse_pdr_sensor.pdr_sensor_position_update+""" </td>
                    </tr>  		
                    <tr>
                        <td rowspan="3"> getDefaultSensor(65546) </td> 
                        <td> Position x_delta_meters </td>
                        <td> """+parse_pdr_sensor.pdr_positionUpdateMessage_x+""" </td>
                    </tr>
                    <tr>
                        <td> Position y_delta_meters </td>
                        <td> """+parse_pdr_sensor.pdr_positionUpdateMessage_y+""" </td>
                    </tr>
                    <tr>
                        <td> Position z_delta_meters </td>
                        <td> """+parse_pdr_sensor.pdr_positionUpdateMessage_z+""" </td>
                    </tr>
                    
					<tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Significant Motion Virtual Sensor </td>
                        <td rowspan="2"> To Validate Significant Motion Sensor </td>
                        <td rowspan="2"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """+parse_sgm_sensor.sgm_timestamp_ns+"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Sgm_Results.csv"> Sgm_Results.csv </a> </td>    
                    </tr>
                    
						<tr>
							<td> Sensor Position Update </td>
							<td> """+parse_sgm_sensor.sgm_sensor_scalar_update+""" </td>
						</tr>  	
						
					<tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="8" class="test-result-step-command-cell"> HRV RMSSD Sensor </td>
                        <td rowspan="8"> To Validate HRV RMSSD Sensor </td>
                        <td rowspan="4"> getSystemService </td>
                        <td > time-stamp </td>
                        <td > """+parse_hrv_sensor.hrv_timestamp_ns+"""	</td>
                        <td rowspan="8" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="8">
                                    <a href="eInfochips/Hrv_Results.csv"> Hrv_Results.csv </a> </td>    
                    </tr>
                    
						<tr>
							<td> hrvMsg->hrv </td>
							<td> """+parse_hrv_sensor.hrv_sensor_hrv_update+""" </td>
						</tr>  
						<tr>
							<td> hrvMsg->hr </td>
							<td> """+parse_hrv_sensor.hrv_sensor_hr_update+""" </td>
						</tr>
						<tr>
							<td> hrvMsg->interval </td>
							<td> """+parse_hrv_sensor.hrv_sensor_interval_update+""" </td>
						</tr>
								
						<tr>
							<td rowspan="4"> getDefaultSensor(65547) </td> 
							<td> hrvMsg->coverage </td>
							<td> """+parse_hrv_sensor.hrv_sensor_coverage_update +""" </td>
						</tr>
						<tr>
							<td> hrvMsg->samples </td>
							<td> """+parse_hrv_sensor.hrv_sensor_samples_update+""" </td>
						</tr>	
						<tr>
							<td> hrvMsg->gaps </td>
							<td> """+parse_hrv_sensor.hrv_sensor_gaps_update+""" </td>
						</tr>
						<tr>
							<td> hrvMsg->method </td>
							<td> """+parse_hrv_sensor.hrv_sensor_method_update+""" </td>
						</tr>
                        
                    <tr class="test-result-step-row test-result-step-row-altone">
                        <td rowspan="2" class="test-result-step-command-cell"> Activity Detection Sensor </td>
                        <td rowspan="2"> To Validate Activity Detection Sensor </td>
                        <td rowspan="1"> getSystemService </td>
                        <td > t_stamp </td>
                        <td > """ +parse_adt_sensor.adt_timestamp_ns  +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="eInfochips/Adt_Results.csv"> Adt_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(65548) </td> 
                        <td> adt_activity </td>
                        <td> """+parse_adt_sensor.adt_activity +""" </td>
                     </tr>    

                 </tbody>
            </table>
            </div>
    </body></html>
    """

f.write(message)
f.close()
new = 3
url = "./FRL_Test_Report.html"
webbrowser.open(url,new=new)
