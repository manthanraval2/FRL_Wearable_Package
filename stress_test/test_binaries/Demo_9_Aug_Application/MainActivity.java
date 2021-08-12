package com.example.test_pressure;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import java.io.File;
import android.os.Environment;
import java.io.OutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileWriter;
import java.io.OutputStreamWriter;

public class MainActivity extends AppCompatActivity implements SensorEventListener{

    private static final String TAG = "MainActivity";

    private SensorManager sensorManager;
    Sensor pressureSensor;
    File file,create_file;
    TextView textview1,textview2;
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
        create_file = new File(file,"Alt_Results.csv");

        try {
            writer = new FileWriter(create_file);
            writer.append("Test");
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        textview1 = (TextView) findViewById(R.id.textview1);
        textview2 = (TextView) findViewById(R.id.textview2);
        Log.d(TAG, "onCreate: Initializing Sensor Services");

        Runnable someRunnable = new Runnable() {
            @Override
            public void run() {
                // todo: background tasks
                sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
                pressureSensor = sensorManager.getDefaultSensor(Sensor.TYPE_PRESSURE);
                sensorManager.registerListener(MainActivity.this, pressureSensor, SensorManager.SENSOR_DELAY_NORMAL);
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                    }
                });
                Log.d(TAG, "OnCreate: Registered PressureSensor listner");
            }
        };
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int i) {

    }

    @Override
    protected void onResume() {

        super.onResume();
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        pressureSensor = sensorManager.getDefaultSensor(Sensor.TYPE_PRESSURE);
        sensorManager.registerListener(MainActivity.this, pressureSensor, SensorManager.SENSOR_DELAY_NORMAL);
        Log.d(TAG, "OnCreate: Registered PressureSensor listner");

    }

    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {
        textview1.setText("hPa: " + sensorEvent.values[0]);
        textview2.setText("T_stamp: " + sensorEvent.timestamp);

        File file = new File("/data/data/com.example.test_pressure/files/eInfochips/Alt_Results.csv");
        try {
            FileOutputStream fileOutputStream = new FileOutputStream(file,true);
            OutputStreamWriter writer = new OutputStreamWriter(fileOutputStream);
            String data_hpa = String.valueOf(sensorEvent.values[0]);
            String data_time = String.valueOf(sensorEvent.timestamp);
            writer.append("hPa,"+ data_hpa);
            writer.append(",t_stamp,"+ data_time);
            writer.append("\n\r");
            writer.close();
            fileOutputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}