#include <avr/io.h>
#include <avr/interrupt.h>

int timer_count = 0;
int sensor_pin1 = 15;
int sensor_pin2 = 16;
int time1 = 0;
int time2 = 0;
int val1 = 0;
int val2 = 0;
int sensor1_ref_ambient = 0;
int sensor2_ref_ambient = 0;
int sensor1_ref_light = 0;
int sensor2_ref_light = 0;
int sensor1_ref = 0;
int sensor2_ref = 0;
double space = 0.03; //in meters
double speed1 = 0;
byte buff;

void setup() {
  // put your setup code here, to run once:
  //------------------------setting timer1 interrupt at 4khz--------------------
  //pinMode(sensor_pin1, INPUT);
  //pinMode(sensor_pin2, INPUT);
  Serial.begin(9600);
  //cal();

}

void loop() {
  // put your main code here, to run repeatedly: 
  
  val1 = analogRead(sensor_pin1);
  val2 = analogRead(sensor_pin2);
  if(val1 > 500){
    time1 = millis();    
  }
  if (val2 > 500) {
    time2 = millis();
  }
  if (time2 > time1)
    speed1 = (space * 1000)/(time2-time1);
  else
    speed1 = (space * 1000)/(time1-time2);
  Serial.print("speed = ");
  Serial.println(speed1);
}

void cal() {
  Serial.println("Cover the sensor and hit enter");
  while(!Serial.available()){    
  }
  buff = Serial.read();
  sensor1_ref_ambient = analogRead(sensor_pin1);
  sensor2_ref_ambient = analogRead(sensor_pin2);
  Serial.println("Remove the cover and hit enter");
  while(!Serial.available()){    
  }
  buff = Serial.read();
  sensor1_ref_light = analogRead(sensor_pin1);
  sensor2_ref_light = analogRead(sensor_pin2);  
  sensor1_ref = (sensor1_ref_ambient+sensor1_ref_ambient)/2;
  sensor1_ref = (sensor1_ref_light+sensor1_ref_light)/2;
}

