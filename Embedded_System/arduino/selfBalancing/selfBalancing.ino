/*Notes:
1. 1 channel of Encoder max output frequency = 2.5 kHz - 2.7 kHz;

*/


unsigned int encoderCount = 0;  //incoming encoder pulse
unsigned int totalEncoderCount = 0;  //for debugging purpose only for now
int timeCount = 0;  //time tracking at 4khz
double revolution = 0.0;
double timer = 0.0;
double RPM = 0;
double interruptFreq = 16000; //change HERE if frequency changes!!!!
int currentStateA = 0;
int currentStateB = 0;
int previousStateA = 0;
int previousStateB = 0;
int encoderYellow = 2;  //encoder pulse incoming channel
int encoderWhite = 4;  //encoder pulse incoming channel
int forwardControl = 3;  //PWM control pin
int backwardControl = 5;  //PWM control pin
int signalA = 0;  //incoming encoder pulse
int signalB = 0;  //incoming encoder pulse
boolean forward = false;  //determine the direction
boolean backward = false;  //determine the direction
int speed_error = 0;
String pwm_in = "";
boolean pwm_blk = false;
int pwm_val = 0;

void setup(){  
//------------------------setting timer1 interrupt at 4khz--------------------
  cli(); //stop interrupts
  TCCR1A = 0; // set TCCR1A register to 0
  TCCR1B = 0; // set TCCR1B register to 0
  TCNT1 = 0; //initialize counter value to 0
  OCR1A = 999;  //set compare match register for 16000 khz increments
  TCCR1B |= (1<<WGM12);  //turn on CTC mode
  TCCR1B |= (1<<CS10);  //set prescaler = 1
  TIMSK1 |= (1<<OCIE1A);  //enable timer compare interrupt
  sei();  //enable interrupts
//--------------------------------------------------------------------------------
  pinMode(encoderYellow, INPUT);
  pinMode(encoderWhite, INPUT);
  pinMode(forwardControl, OUTPUT);
  pinMode(backwardControl, OUTPUT);
  Serial.begin(9600);
}

//interrupt routine
ISR(TIMER1_COMPA_vect){
//-----------------rising edge detection + RPM calculation---------------------
   ++timeCount;  // increasing at 16kHz
  currentStateA = digitalRead(encoderYellow);
  currentStateB = digitalRead(encoderWhite);
  if((previousStateA != currentStateA) || (previousStateB != currentStateB)){  //encoder pulse is changed
    ++encoderCount;
    ++totalEncoderCount;  //total encoder count from start up (no reset)
    signalA = currentStateA;
    signalB = currentStateB;
  }   
  //sampling frequency must be high enough to determine the direction
  // direction_check();
  if (encoderCount >= 100 || timeCount >= 1600){ //update speed 
    revolution = ((double)encoderCount) / 64.0;
    timer = ((double)timeCount)/interruptFreq;
    RPM = revolution / timer * 60.0 / 29.0;
    timeCount = 0;
    encoderCount = 0;
  } 
  previousStateA = currentStateA;
  previousStateB = currentStateB;
//-----------------------------------------------------------------------
}  //end of interrupt

/*
void pid_control () {
  speed_error
}
*/

void loop(){
//------------------------debugging--------------------------------------
  /*
  for(int i = 100; i < 256; ++i){
    analogWrite(forwardControl, i);
    Serial.print("PWM: ");
    Serial.print(i);
    Serial.print(" | ");
    Serial.print("RPM: ");
    Serial.print((int)RPM);
    Serial.print(" | ");
    Serial.print("Direction: ");
    if(forward) Serial.println("forward");
    else if(backward) Serial.println("backward");
    else Serial.println("not moving");
    delay(100);
  }
  */
  while(Serial.available()){
    char inChar = Serial.read();
    pwm_in += inChar;
    pwm_blk = true;
  }
  if (pwm_blk) {
    pwm_val = pwm_in.toInt();
    pwm_blk = false;
  }
  analogWrite(forwardControl, pwm_val);
  
  pwm_in = "";
  //analogWrite(backwardControl, 100);
  Serial.print("encoder count: ");
  Serial.print(totalEncoderCount);
  Serial.print(" | ");
  Serial.print("RPM: ");
  Serial.print((int)RPM);
  Serial.print(" | ");
  Serial.print("Direction: ");
  if(forward) Serial.println("forward");
  else if(backward) Serial.println("backward");
  else Serial.println("not moving");
  delay(100);  
//------------------------------------------------------------
}

/*
//finding the direction of the motor
void direction_check() {
  if(previousStateA == 0 && previousStateB == 0 && signalA == 0 && signalB == 1) {
    forward = true;
    backward = false;
  } else if (previousStateA == 0 && previousStateB == 1 && signalA == 1 && signalB == 0) {
    forward = true;
    backward = false;
  } else if (previousStateA == 1 && previousStateB == 0 && signalA == 0 && signalB == 0) {
    forward = true;
    backward = false;
  } else if (previousStateA == 1 && previousStateB == 1 && signalA == 1 && signalB == 0) {
    forward = true;
    backward = false;
  } else if (previousStateA == 0 && previousStateB == 0 && signalA == 1 && signalB == 0) {
    forward = false;
    backward = true;
  } else if (previousStateA == 0 && previousStateB == 1 && signalA == 0 && signalB == 0) {
    forward = false;
    backward = true;
  } else if (previousStateA == 1 && previousStateB == 0 && signalA == 1 && signalB == 1) {
    forward = false;
    backward = true;
  } else if (previousStateA == 1 && previousStateB == 1 && signalA == 0 && signalB == 1) {
    forward = false;
    backward = true;
  } else {
    forward = false;
    backward = false;  
  }
}
*/
