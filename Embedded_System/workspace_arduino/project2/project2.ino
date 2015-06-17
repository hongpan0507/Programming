/*
Notes:
1. myservo.writeMicroseconds(i); for 1510 < i < 1515, servo stops.
2. myservo.writeMicroseconds(i); for 1300 < i < 1510, servo rotates to the clockwise
3. myservo.writeMicroseconds(i); for 1515 < i < 1700, servo rotates to the counter-clockwise
4. Teensy 3.1 PIT clk frequency = 48MHz
*/

#include <Servo.h> 

//servo and control
int servo_pin = A8;
Servo myservo;  // create servo object to control a servo 
int freq_prev = 0;
int freq_tol = 1;	//tolerance of frequency reading
int error = 0;
int error_prev = 0;
int error_count = 0;

String dir;
boolean max_found = false;
int state2_freq = 0;
boolean state2_blk = true;
boolean freq_increase = false;
boolean freq_decrease = false;
int count_decrease = 0;
boolean freq_const = false;

int rpm[49];
int rpm_count = 0;
int rpm_diff = 0;
int state = 0;



//analog to digital sensing
int analog_in = 0;
boolean soft_adc = false;
boolean pre_soft_adc = false;
int sensor_pin = A7; 

//sensor time and frequency
int time1 = 0;
int time2 = 0;
int read_count = 0;
int freq[4];
int freq_count = 0;
int freq_ave = 0;
int count = 0;

//interrupt frequency
int int_count = 0;
int PIT_freq = 48000000;	//Teensy 3.1 PIT clk frequency = 48 MHz

//calibration
int led_pin = 13;
int covered_read = 0;
int uncovered_read = 0;
int ref = 130;
int freq_max = 0;
byte serial_in = 0;

void setup() {	
	timer0_interrupt(3000);		
	timer1_interrupt(50);	
	//pinMode(led_pin, OUTPUT);	
	myservo.attach(servo_pin);  // attaches the servo on pin 9 to the servo object 	
	//cal();
}

void loop() {
	/*
	if(freq_ave > freq_max ) { //update freq_max
		freq_max = freq_ave;
	}		
	if (state == 0) {
		dir = "cw";
		servo(dir, 2);		
		delay(300);
		if(freq_ave > freq_prev+freq_tol){				
			state = 0;			
		} else if (freq_ave < freq_prev-freq_tol) {
			state = 1;			
			//dir_change = true;
		}
	} else if (state == 1) {
		dir = "ccw";
		servo(dir, 4);		
		delay(300);
		if(freq_ave > freq_prev+freq_tol){				
			state = 1;
		} else if (freq_ave < freq_prev-freq_tol) {
			state = 2;
		} 
	} else if (state == 2) {			
		dir = "stop";
		servo(dir, 0);			
		delay(300);
		if (freq_ave < freq_max-freq_tol) {
			freq_max = 0;			
			state = 0;			
		}
	}	
	*/
	/*
	if(freq_ave > freq_max ) { //update freq_max
		freq_max = freq_ave;
	}		
	if(freq_ave == 0){
		state = 3;
	}
	if (state == 0) {
		dir = "cw";
		servo(dir, 2);		
		delay(100);
		if(freq_ave > freq_prev+freq_tol){				
			state = 0;			
		} else if (freq_ave < freq_prev-freq_tol) {
			state = 1;						
		}
	} else if (state == 1) {
		dir = "ccw";
		servo(dir, 4);		
		delay(100);
		if(freq_ave > freq_prev+freq_tol){				
			state = 1;
		} else if (freq_ave < freq_prev-freq_tol) {
			state = 2;
		} 		
	} else if (state == 2) {
		if(max_found == false) {
			dir = "cw";
			servo(dir, 2);			
			delay(50);
		}		
		if (freq_ave > freq_max-10) {
			dir = "stop";
			servo(dir, 0);			
			max_found = true;
			delay(300);			
		}
		if (freq_ave < freq_max-10 && max_found == true) {
			freq_max = freq_max/2;			
			state = 0;			
			max_found = false;
		}
		if (freq_ave < freq_prev-freq_tol) {
			state = 0;
		}
	} else if (state == 3) {
			dir = "stop";
			servo(dir, 0);			
			delay(100);
			if (freq_ave != 0) {
				state = 0;
			}
	}
	*/
	
	if(freq_ave > freq_max ) { //update freq_max
		freq_max = freq_ave;
	}
	if(freq_ave == 0 ){
		state = 3;
	}
	if (state == 0) {
		dir = "cw";
		servo(dir, 2);			
		delay(100);
		if(freq_increase == true){				
			state = 0;					
		} else if (freq_decrease==true) {
			state = 1;								
		}
	} else if (state == 1) {
		dir = "ccw";
		servo(dir, 4);	
		delay(100);
		if(freq_increase == true){				
			state = 1;						
		} else if (freq_decrease==true) {
			++count_decrease;
			if(count_decrease == 1){
				state = 2;			
				count_decrease = 0;				
			}			
		}		
	} else if (state == 2) {
		if(max_found == false) {
			dir = "cw";		
			servo(dir, 2);			
			delay(100);
		}		
		if (freq_ave > freq_max-5) {
			dir = "stop";
			servo(dir, 0);			
			max_found = true;
			delay(300);			
		}		
		if (freq_decrease == true) {
			//freq_max = freq_max/2;			
			state = 0;			
			max_found = false;
		}					
	} else if (state == 3) {
			dir = "stop";
			servo(dir, 0);			
			freq_max = 0;
			delay(100);
			if (freq_ave != 0 || freq_ave != freq_prev) {
				state = 0;
				
			}
	}
	
	Serial1.print(freq_max); Serial1.print(' ');
    Serial1.print(freq_ave); Serial1.print(' ');
    Serial1.print(freq_prev); Serial1.print(' ');
	Serial1.print(analog_in); Serial1.print(' ');
	if(dir == "cw") {
		Serial1.print(1); Serial1.print(' ');
	} else if (dir == "ccw") {
		Serial1.print(-1); Serial1.print(' ');
	} else if (dir == "stop") {
		Serial1.print(0); Serial1.print(' ');
	}
	Serial1.print(" \n");
		
	//debug();	
}

//--------------------------debug control----------------------
void debug(){
	Serial.print("state = ");
	Serial.print(state);
	Serial.print("  |  ");	
	Serial.print("increase = ");
	Serial.print(freq_increase);
	Serial.print("  |  ");
	Serial.print("decrease = ");
	Serial.print(freq_decrease);
	Serial.print("  |  ");
	Serial.print("max frequency = ");
	Serial.print(freq_max);
	Serial.print("  |  ");
	Serial.print("current frequency = ");
	Serial.print(freq_ave);
	Serial.print("  |  ");
	Serial.print("previous frequency = ");
	Serial.print(freq_prev);
	Serial.print("  |  ");		
	Serial.print("photo diode = ");
	Serial.print(analog_in);
	Serial.print("  |  ");
	Serial.print("direction = ");
	Serial.println(dir);		
}

//--------------------------Bluetooth--------------------------
//void blue_tooth (String message0, String message1) {
void blue_tooth (int message0) {
	Serial1.print(message0);
/*
  while (Serial1.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (Serial1.available() >0) {
      char c = Serial1.read();  //gets one byte from serial buffer
      message0 += c; //makes the string readString
    } 
  }
  if(message0.length()>0){
    Serial.print("Read:");
    Serial.println(message0);
  }
  message0 = "";
  delay(100);
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      message1 += c; //makes the string readString
    } 
  }
  if(message1.length()>0){
    Serial.print("Send:");
    Serial.println(message1);
    Serial1.println(message1);
  }
  message1 = "";
  
  delay(100);
  Serial.flush();
  Serial1.flush();
  */
}
//--------------------------servo control----------------------
void servo(String dir, int rpm) {
	if (dir == "cw") {  // cw = clockwise
		myservo.writeMicroseconds(1510-rpm);
	} else if (dir == "ccw") {  // ccw = counter-clockwise
		myservo.writeMicroseconds(1515+rpm);
	} else if (dir == "stop" ) {
		myservo.writeMicroseconds(1512);
	}
}

//-------------------------timer0 ISR--------------------------
void pit0_isr(void){  
	analog_in = analogRead(sensor_pin);  
	if(analog_in > ref) soft_adc = true;  //true = photo resistor covered
	else soft_adc = false;    //false = photo resitosr uncovered

	if(read_count == 0) { 
		time1 = micros();
	} 
	if(read_count == 3) {
		time2 = micros();    
		freq[freq_count] = 1000000/(time2-time1);
		++freq_count;    		
		read_count = 0;    
	}

	if (freq_count > (sizeof(freq)/sizeof(int))-1) {  //average samples
		freq_count = 0;
		for(int i = 0; i < (sizeof(freq)/sizeof(int)); ++i){
			freq_ave += freq[i];
		}
		freq_ave = freq_ave/(sizeof(freq)/sizeof(int));
	} 

	if (soft_adc != pre_soft_adc) {   //transition happened
		++read_count;
		pre_soft_adc = soft_adc;
		count = 0;
	} else {
		++count;
	}
	if (count > 200) {
		freq_ave = 0;
		count = 0;
	}

	//Timer Flag Register; Timer Interrupt Flag (TIF) must be set to 1 to clear the flag                   
	PIT_TFLG0 = 1;   //very important!!!
}

//-------------------------timer0 ISR--------------------------
void pit1_isr(void){  
	rpm[rpm_count] = freq_ave;
	++rpm_count;
	if(rpm_count > (sizeof(rpm)/sizeof(int))-1){
		rpm_count = 0;
		for(int i = 0; i <(sizeof(rpm)/sizeof(int)-1); ++i){
			rpm_diff = rpm_diff + (rpm[i]-rpm[i+1]);
		}
		if(rpm_diff > freq_tol){
			freq_decrease = true;
			freq_increase = false;
			freq_const = false;				
		} else if(rpm_diff < -freq_tol){
			freq_decrease = false;
			freq_increase = true;
			freq_const = false;			
		} else {
			freq_decrease = false;
			freq_increase = false;
			freq_const = true;			
		}
		rpm_diff = 0;
	}
	debug();
	//Timer Flag Register; Timer Interrupt Flag (TIF) must be set to 1 to clear the flag                   
	PIT_TFLG1 = 1;   //very important!!!
}

//--------------------------setting up timer0 interrupt--------
void timer0_interrupt(int int_freq){  
	int_count = (PIT_freq/int_freq)-1;
	SIM_SCGC6 |= 0x800000;  //System Clk Gating Control Register 6; PIT is on bit 23; freescale MK20DX page 256
	PIT_MCR = 0x00;  //0x(PIT enabled, Timer run in Debug mode); freescale MK20DX page 904
	PIT_LDVAL0 = int_count;  //timer counts down; freescale MK20DX page 904
	PIT_TCTRL0 = 0x03;  // 0x(Chain Mode, Timer Interrupt Enable, Timer Enable); freescale MK20DX page 905
	//PIT_CVAL0 has the value of the current timer; freescale MK20DX page 905
	NVIC_ENABLE_IRQ(IRQ_PIT_CH0);  //enable interrupt;   
}

//--------------------------setting up timer0 interrupt--------
void timer1_interrupt(int int_freq){  
	int_count = (PIT_freq/int_freq)-1;
	SIM_SCGC6 |= 0x800000;  //System Clk Gating Control Register 6; PIT is on bit 23; freescale MK20DX page 256
	PIT_MCR = 0x00;  //0x(PIT enabled, Timer run in Debug mode); freescale MK20DX page 904
	PIT_LDVAL1 = int_count;  //timer counts down; freescale MK20DX page 904
	PIT_TCTRL1 = 0x03;  // 0x(Chain Mode, Timer Interrupt Enable, Timer Enable); freescale MK20DX page 905
	//PIT_CVAL0 has the value of the current timer; freescale MK20DX page 905
	NVIC_ENABLE_IRQ(IRQ_PIT_CH1);  //enable interrupt;   
}

