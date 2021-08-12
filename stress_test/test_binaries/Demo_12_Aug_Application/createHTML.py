# write-html.py
import webbrowser
import csv

'''Alt Sensor schema'''
altpressure_val = 0
alttimestamp_ns = 0

'''Build version check'''
device_build_type = 0
build_version_release = 0
build_id = 0
build_version_incremental = 0

with open('build_version.csv', 'rt') as Version:
    version_data = csv.reader(Version, delimiter="\t")
    for version_data_row in version_data:
        list_data_version = version_data_row[0].split()

    device_build_type = list_data_version[0]
    build_version_release = list_data_version[1]
    build_id = list_data_version[2]
    build_version_incremental = list_data_version[3]

with open('Alt_Results.csv', 'rt') as AltData:
    altdata = csv.reader(AltData)
    for altrow in altdata:
        pass
    altpressure_val = altrow[1]
    alttimestamp_ns = altrow[3]
            
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

            border: 1px solid black;
            width: 800px;
        }

        .test-result-table-header-cell {

            border-bottom: 1px solid black;
            background-color: grey;
            color: white;
        }

        .test-result-step-command-cell {

            border-bottom: 1px solid black;
        }

        .test-result-step-description-cell {

            border-bottom: 1px solid black;
        }

        .test-result-step-result-cell-ok {
            border-bottom: 1px solid black;
            font-size: 20px;
			font-weight: bold;
        }

        .test-result-step-result-cell-failure {

			color: red;
            border-bottom: 1px solid black;
            background-color:  #f7dc6f;
            <!-- background-color: red; -->
        }

        .test-result-step-result-cell-notperformed {

            border-bottom: 1px solid gray;
            background-color: white;
        }

        .test-result-describe-cell {
            background-color: tan;
            font-style: italic;
        }

        .test-result-step-result-cell-ok {
			color: green;
            border-bottom: 1px solid black;
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
					<td class="summary-table-data"> device_build_type:"""+device_build_type+""" </td>
				
				</tr>
            	<tr>
					<td class="summary-table-data"> build_version_release:"""+build_version_release+""" </td>
				</tr>
            	<tr>
					<td class="summary-table-data"> build_id:"""+build_id+""" </td>
				</tr>
            	<tr>
					<td class="summary-table-data"> build_version_incremental:"""+build_version_incremental+""" </td>
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
					6
                </td>                 	
            </tr>
            <tr>
            	<td class="summary-table-data"> 						
					Fail 
                </td>
				</td><td class="summary-table-data"> 
					4
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
					10 
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
					<td > hPa</td>
					<td > """ +altpressure_val +"""	</td>
                    <td rowspan="2" class="test-result-step-result-cell-ok" id="result"> PASS </td>
                    <td rowspan="2">
                                <a href="Alt_Results.csv"> Alt_Results.csv </a> </td>    
				</tr>
                     		
				<tr>
				    <td rowspan="1"> AltData *&gt;(msg.get) </td> 
					<td> t_stamp </td>
					<td> """+alttimestamp_ns +""" </td>
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
