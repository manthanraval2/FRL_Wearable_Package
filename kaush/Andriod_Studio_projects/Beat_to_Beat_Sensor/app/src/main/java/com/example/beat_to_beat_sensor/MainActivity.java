package com.example.beat_to_beat_sensor;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import java.io.File;
import android.os.Environment;

import androidx.appcompat.app.AppCompatActivity;

import java.io.OutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileWriter;
import java.io.OutputStreamWriter;
import java.util.List;

public class MainActivity extends AppCompatActivity implements SensorEventListener{

    private static final String TAG = "###RRI_Sensor";

    public SensorManager sMgr;
    Sensor rriSensor = null;
    File file,create_file;
    public TextView t_stamp_text,interval_ms,peak_ms;
    FileWriter writer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Create File for saving data.
        file = new File(MainActivity.this.getFilesDir(), "eInfochips");
        if(!file.exists()) {
            file.mkdirs();
        }
        create_file = new File(file,"RRI_Results.csv");

        try {
            writer = new FileWriter(create_file);
            writer.append("");
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        t_stamp_text = (TextView) findViewById(R.id.t_stamp_text);
        interval_ms = (TextView) findViewById(R.id.interval_ms);
        peak_ms = (TextView) findViewById(R.id.peak_ms);
        Log.d(TAG, "onCreate: Initializing Beat to Beat Sensor Services");
        registerSesnor();
        Runnable someRunnable = new Runnable() {
            @Override
            public void run() {
                // todo: background tasks
              /*  sMgr = (SensorManager) getSystemService(SENSOR_SERVICE);
                heartSensor = sMgr.getDefaultSensor(TYPE_HEART_RATE);
                if(heartSensor != null)
                    Log.d(TAG, "onCreate: load sensor");
                else
                    Log.d(TAG, "onCreate:  no load sensor");*/

                //  sMgr.registerListener(MainActivity.this, heartSensor, SensorManager.SENSOR_DELAY_NORMAL);
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                    }
                });
                Log.d(TAG, "OnCreate: Registered PPGSensor listner");
            }
        };
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        System.out.println("onAccuracyChanged - accuracy: " + accuracy);

    }

    @Override
    protected void onResume() {
        super.onResume();
        bodySensorPermission();
    }

    private void registerSesnor(){
        sMgr  = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        /*List<Sensor> sensorList = sMgr.getSensorList(Sensor.TYPE_ALL);
        for (Sensor currentSensor : sensorList) {
            Log.d("List sensors", "Name: "+currentSensor.getName() + " /Type_String: " +currentSensor.getStringType()+ " /Type_number: "+currentSensor.getType());
        }*/
        rriSensor = sMgr.getDefaultSensor(65539);
        sMgr.registerListener(this,rriSensor,SensorManager.SENSOR_DELAY_FASTEST);
        Log.d(TAG, "OnCreate: Registered heartSensor listner");
        /*sMgr  = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        heartSensor = sMgr.getDefaultSensor(Sensor.);
        sMgr.registerListener(MainActivity.this, heartSensor, SensorManager.SENSOR_DELAY_FASTEST);
        Log.d(TAG, "OnCreate: Registered heartSensor listner");
        if(heartSensor != null)
            Log.d(TAG, "onCreate: load sensor");
        else
            Log.d(TAG, "onCreate:  no load sensor");*/
        //Your code for declaring and initializing Sensor manager and Heartrate sensor
    }
    private void bodySensorPermission(){
        if (checkSelfPermission(Manifest.permission.BODY_SENSORS)
                != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{Manifest.permission.BODY_SENSORS},
                    1);
        } else {
            //registerSesnor();
        };

    }
    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions,
                                           int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == 1
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            //Your code for declaring and initializing Sensor manager and Heartrate sensor
            //registerSesnor();
        }
    }
    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {

        String interval_ms_text = " RRi interval_ms: " + (float) sensorEvent.values[0];
        String peak_ms_text = "RRi peak_ms: " + (float) sensorEvent.values[1];
        String t_stamp = "t_stamp: " + (int) sensorEvent.timestamp;
        t_stamp_text.setText(t_stamp);
        interval_ms.setText(interval_ms_text);
        peak_ms.setText(peak_ms_text);
        //Do something with your PPG signal
        //heartRateValue = Integer.toString(sensorEvent.sensor.getType());
        //heartRateValue = String.valueOf((sensorEvent.values[0]));
        /*Log.d(TAG, "onSensorChanged");
        //textview1.setText(heartRateValue);

        textview1.setText("T_stamp: " + String.valueOf(sensorEvent.timestamp));
        textview2.setText("bpm: " + String.valueOf(sensorEvent.values[0]));


        File file = new File("/data/data/com.example.heartrate/files/eInfochips/Hrm_Results.csv");
        try {
            FileOutputStream fileOutputStream = new FileOutputStream(file,true);
            OutputStreamWriter writer = new OutputStreamWriter(fileOutputStream);
            String data_bpm = String.valueOf(sensorEvent.values[0]);
            String data_time = String.valueOf(sensorEvent.timestamp);
            writer.append("t_stamp,"+ data_time);
            writer.append(",bpm,"+ data_bpm);
            writer.append("\n");
            writer.close();
            fileOutputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }*/
    }
}