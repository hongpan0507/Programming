/*Note:
1. For nmos, pwm=10 out of 255 is enough to generate high voltage; current = 3mA
2. For pmos, pwm=245 out of 255 is enough to generate high voltage; current = 4mA

*/
#include <avr/io.h>
#include <avr/interrupt.h> //C:\Program Files\Arduino\hardware\tools\avr\avr\include\avr
#include <kinetis.h>

//---------------pwm--------------------------
int pwm_freq = 3000;
int nmos_pwm_val = 20;  //preset pwm pulse width
int pmos_pwm_val = 230;  //preset pwm pulse width
const int pwm_pin9 =  9;  //nmos
const int pwm_pin10 =  10;  //pmos
const int ctrl_pin18 =  18;  //left; look from the back of the pcb
const int ctrl_pin19 =  19;  //right
//--------------------------------------------
//--------------command input-----------------
int cmd_val = 0;  
char cmd_char;
String cmd_str = "";
String cmd_val_str = "";
boolean cmd_ready = false;
boolean pin_num_ready = false;
//--------------------------------------------
//----------------interrupt-------------------
int pulse_switch = 0;
int driver_freq = 60;  //preset piezoelectric pump driver frequency
int interrupt_bus_freq = 24000000;
int led = 13;
//--------------------------------------------

void setup() {
  Serial.begin(9600);
  pinMode(pwm_pin9, OUTPUT);
  pinMode(pwm_pin10, OUTPUT);
  pinMode(ctrl_pin18, OUTPUT);
  pinMode(ctrl_pin19, OUTPUT);
  analogWriteFrequency(pwm_pin9, pwm_freq);
  analogWriteFrequency(pwm_pin10, pwm_freq);
  digitalWrite(pwm_pin9, HIGH);  
  digitalWrite(pwm_pin10, HIGH);
  digitalWrite(ctrl_pin18, LOW);
  digitalWrite(ctrl_pin19, LOW);
  
  timer0_interrupt();
  pinMode(led, OUTPUT); 
}

void loop() {
  //--------------command input-----------------
  if(Serial.available() > 0) {
    cmd_char = Serial.read();    
    if(cmd_char == '='){
      pin_num_ready = true;      
    } else if (cmd_char == ';'){
      cmd_ready = true;      
      pin_num_ready = false;   
    } else if (pin_num_ready == false){
      cmd_str += cmd_char;
    } else if (pin_num_ready == true){
      cmd_val_str += cmd_char;
    }    
  }
  //--------------------------------------------
  //---PWM generation+motor control-------------
  if(cmd_ready){    
    cmd_val = strtol(cmd_val_str.c_str(), NULL, 10);  //convert string to int
    Serial.print(cmd_str + "=");    //output for debugging
    Serial.println(cmd_val, DEC);  //debug
        
    if(cmd_str == "pwm_val"){     
      cmd_val = pwm_val_check(cmd_val);  //check to make sure 0<=pwm<=255; then change pwm pulse width 
      nmos_pwm_val = cmd_val;
      pmos_pwm_val = 255 - cmd_val;  //use nmos pusle width as a reference
    } else if (cmd_str == "left"){  //pin18
      if(cmd_val == 0){
        digitalWrite(ctrl_pin18, LOW);  //turn off motor
      } else if(cmd_val == 1){
        digitalWrite(ctrl_pin18, HIGH);  //turn on motor
        digitalWrite(ctrl_pin19, LOW);  //only allow one motor to turn on at a time
      }
    } else if (cmd_str == "right"){  //pin19
      if(cmd_val == 0){
        digitalWrite(ctrl_pin19, LOW);  //turn off motor
      } else if(cmd_val == 1){
        digitalWrite(ctrl_pin19, HIGH);  //turn on motor
        digitalWrite(ctrl_pin18, LOW);  //only allow one motor to turn on at a time        
      }
    } else if (cmd_str == "freq"){
      driver_freq = driver_freq_val_check(cmd_val);
      timer0_interrupt();
    }
  //--------------------------------------------
    cmd_ready = false;    //reset for command input
    cmd_str = "";  //reset for command input
    cmd_val_str = "";  //reset for command input
  }
}

int pwm_val_check(int cmd_val){  //check if the value entered is in the range of 0-255
  if(cmd_val > 255){
    cmd_val = 255;
  } else if (cmd_val < 0){
    cmd_val = 0;
  }
  return cmd_val;
}

int driver_freq_val_check(int cmd_val){  //check if the value entered is in the range of 0-255
  if(cmd_val > 200){
    cmd_val = 200;
  } else if (cmd_val < 0){
    cmd_val = 0;
  }
  return cmd_val;
}

void timer0_interrupt(){  //set up interrupt parameter
  SIM_SCGC6 |= 0x800000;  //System Clk Gating Control Register 6; PIT is on bit 23; freescale MK20DX page 256 and page 160  
  PIT_MCR = 0x00;  //0x(PIT enabled, Timer run in Debug mode); freescale MK20DX page 904
  PIT_LDVAL0 = interrupt_bus_freq/driver_freq - 1;  //driver frequency; timer 0 load value = 24M in hex; timer counts down; freescale MK20DX page 904
  PIT_TCTRL0 = 0x03;  // 0x(Chain Mode, Timer Interrupt Enable, Timer Enable); freescale MK20DX page 905
  //PIT_CVAL0 has the value of the current timer; freescale MK20DX page 905
  NVIC_ENABLE_IRQ(IRQ_PIT_CH0);  //enable interrupt;   
}

void pit0_isr(void){  //interrupt routine
  if(pulse_switch == 1) {
    pulse_switch = 0;
    digitalWrite(led,LOW);
    pinMode(pwm_pin10, OUTPUT);  //need to declare as GPIO before can be used as digital out
    digitalWrite(pwm_pin10, LOW);  //keep pmos on while pulsing nmos
    analogWrite(pwm_pin9, nmos_pwm_val);  //pulse nmos to generate high positive voltage
  } else {
    pulse_switch = 1;  
    digitalWrite(led,HIGH);     
    pinMode(pwm_pin9, OUTPUT);  //need to declare as GPIO before can be used as digital out
    digitalWrite(pwm_pin9, HIGH);  //keep nmos on while pulsing pmos
    analogWrite(pwm_pin10, pmos_pwm_val);  //pulse pmos to generate high negative voltage   
  }  
  //Timer Flag Register; Timer Interrupt Flag (TIF) must be set to 1 to clear the flag                   
  PIT_TFLG0 = 1;   //very important!!!
}

