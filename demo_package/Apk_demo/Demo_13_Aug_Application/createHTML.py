# write-html.py
import webbrowser
import csv
import os.path
from os import path

''' File Naming '''
build_version_file = 'build_version.csv'
pressure_file_name = 'Alt_Results.csv'
hrm_file_name = 'Hrm_Results.csv'
gyro_file_name = 'Gyr_Results.csv'
acc_file_name = 'Acc_Results.csv'
pedo_file_name = 'Pedometer_Results.csv'

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

if __name__ == "__main__":
    parse_build_version()
    parse_alt_sensor()
    parse_hrm_sensor()
    parse_gyro_sensor()
    parse_acc_sensor()
    parse_pedo_sensor()
    

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
                        5
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
                        5 
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
                        <td rowspan="1"> CrTopicMsgCreator AltData </td>
                        <td > t_stamp </td>
                        <td > """ +parse_alt_sensor.alttimestamp_ns  +"""	</td>
                        <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                        <td rowspan="2">
                                    <a href="Alt_Results.csv"> Alt_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> AltData *&gt;(msg.get) </td> 
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
                                    <a href="Hrm_Results.csv"> Hrm_Results.csv </a> </td>    
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
                                    <a href="Gyr_Results.csv"> Gyr_Results.csv </a> </td>    
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
                                    <a href="Acc_Results.csv"> Acc_Results.csv </a> </td>    
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
                                    <a href="Pedometer_Results.csv"> Pedometer_Results.csv </a> </td>    
                    </tr>
                                
                    <tr>
                        <td rowspan="1"> getDefaultSensor(Sensor.TYPE_STEP_COUNTER) </td> 
                        <td> steps </td>
                        <td> """+parse_pedo_sensor.ped_steps+""" </td>
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
