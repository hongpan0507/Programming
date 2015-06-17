/*Notes:
1. 1 channel of Encoder max output frequency = 2.5 kHz - 2.7 kHz;

*/

unsigned int left_encoderCount = 0;  //incoming encoder pulse
double left_revolution = 0.0;
double left_RPM = 0.0;
int left_encoderYellow = 2;  //encoder pulse incoming channel
int left_encoderWhite = 4;  //encoder pulse incoming channel
int left_forwardControl = 3;  //PWM control pin
int left_backwardControl = 5;  //PWM control pin
int left_previousStateA = 0;
int left_previousStateB = 0;
int left_timeCount = 0;  //time tracking at 16khz

unsigned int right_encoderCount = 0;  //incoming encoder pulse
double right_revolution = 0.0;
double right_RPM = 0.0;
int right_encoderYellow = 12;  //encoder pulse incoming channel
int right_encoderWhite = 10;  //encoder pulse incoming channel
int right_forwardControl = 11;  //PWM control pin
int right_backwardControl = 6;  //PWM control pin
int right_previousStateA = 0;
int right_previousStateB = 0;
int right_timeCount = 0;  //time tracking at 16khz

double interruptFreq = 16000; //change HERE if frequency changes!!!!
double timer = 0.0;
int currentStateA = 0;
int currentStateB = 0;


//int signalA = 0;  //incoming encoder pulse
//int signalB = 0;  //incoming encoder pulse
//boolean forward = false;  //determine the direction
//boolean backward = false;  //determine the direction
int speed_error = 0;
int sync = 0;
int integral = 0;
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
  pinMode(left_encoderYellow, INPUT);
  pinMode(left_encoderWhite, INPUT);
  pinMode(left_forwardControl, OUTPUT);
  pinMode(left_backwardControl, OUTPUT);
  pinMode(right_encoderYellow, INPUT);
  pinMode(right_encoderWhite, INPUT);
  pinMode(right_forwardControl, OUTPUT);
  pinMode(right_backwardControl, OUTPUT);
  Serial.begin(9600);
}

//interrupt routine
ISR(TIMER1_COMPA_vect){
  ++left_timeCount;  // increasing at 16kHz
  ++right_timeCount;  // increasing at 16kHz
  motor_speed(&left_revolution, &left_RPM, &left_encoderCount, &left_encoderYellow, &left_encoderWhite, &left_previousStateA, &left_previousStateB, &left_timeCount);
  motor_speed(&right_revolution, &right_RPM, &right_encoderCount, &right_encoderYellow, &right_encoderWhite, &right_previousStateA, &right_previousStateB, &right_timeCount);
  speed_error = left_RPM - right_RPM;  
}  //end of interrupt

//-----------------RPM calculation----------------------------------------------------------
void motor_speed(double *revolution, double *RPM, unsigned int *encoderCount, int *encoderYellow, int *encoderWhite, int *previousStateA, int *previousStateB, int *timeCount) {
  currentStateA = digitalRead(*encoderYellow);
  currentStateB = digitalRead(*encoderWhite);
  if((*previousStateA != currentStateA) || (*previousStateB != currentStateB)){  //encoder pulse is changed
    ++(*encoderCount);
    //signalA = currentStateA;
    //signalB = currentStateB;
  }   
  //sampling frequency must be high enough to determine the direction
  // direction_check();
  if (*encoderCount >= 100 || *timeCount >= 1600){ //update speed 
    *revolution = ((double)*encoderCount) / 64.0;
    timer = ((double)*timeCount)/interruptFreq;
    *RPM = *revolution / timer * 60.0 / 29.0;
    *timeCount = 0;
    *encoderCount = 0;
  } 
  *previousStateA = currentStateA;
  *previousStateB = currentStateB;
}
//-----------------------------------------------------------------------
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
  analogWrite(left_forwardControl, pwm_val); 
  sync = pwm_val+speed_error;
  if(sync > 255) sync = 255;
  else if (sync < 0) sync = 0;
  analogWrite(right_forwardControl, sync);
  pwm_in = "";
  Serial.print(" | ");
  Serial.print("left RPM: ");
  Serial.print((int)left_RPM);
  Serial.print(" | ");
  Serial.print("right RPM: ");
  Serial.print((int)right_RPM);
  Serial.print(" | ");
  Serial.print("speed error: ");
  Serial.print(speed_error);
  Serial.println(" | ");
  //Serial.print("Direction: ");
  //if(forward) Serial.println("forward");
  //else if(backward) Serial.println("backward");
 // else Serial.println("not moving");
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
