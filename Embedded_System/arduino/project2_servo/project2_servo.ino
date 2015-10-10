/*
Notes:
1. myservo.writeMicroseconds(i); for 1510 < i < 1515, servo stops.
2. myservo.writeMicroseconds(i); for 1300 < i < 1510, servo rotates to the clockwise
3. myservo.writeMicroseconds(i); for 1515 < i < 1700, servo rotates to the counter-clockwise
*/


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
int count = 0;                
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  myservo.attach(A8);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(9600);
  //myservo.writeMicroseconds(1300);
  //myservo.detach();
} 
 
 
void loop() 
{   
   servo("ccw", 4);
/*  
  for(int i = 1510; i < 6; ++i){                               
    myservo.writeMicroseconds(i);
    Serial.print("servo write =");    
    Serial.println(1500+i);
    delay(500);                       
  }
 */
} 

void servo(String dir, int rpm) {
	if (dir == "cw") {  // cw = clockwise
		myservo.writeMicroseconds(1510-rpm);
	} else if (dir == "ccw") {  // ccw = counter-clockwise
		myservo.writeMicroseconds(1515+rpm);
	} else if (dir == "stop" ) {
		myservo.writeMicroseconds(1512);
	}
}