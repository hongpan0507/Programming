/*Note:
1. For nmos, pwm=10 out of 255 is enough to generate high voltage; current = 3mA
2. For pmos, pwm=245 out of 255 is enough to generate high voltage; current = 4mA

*/

const int pwm_pin9 =  9;  //nmos
const int pwm_pin10 =  10;  //pmos
const int ctrl_pin18 =  18;  //left; look from the back of the pcb
const int ctrl_pin19 =  19;  //right
int cmd_val = 0;  
char cmd_char;
String cmd_str = "";
String cmd_val_str = "";
boolean cmd_ready = false;
boolean pin_num_ready = false;
int pwm_pin_num = 0;

int pwm_freq = 5000;

void setup() {
  Serial.begin(9600);
  pinMode(pwm_pin9, OUTPUT);
  pinMode(pwm_pin10, OUTPUT);
  pinMode(ctrl_pin18, OUTPUT);
  pinMode(ctrl_pin19, OUTPUT);
  analogWriteFrequency(pwm_pin9, pwm_freq);
  analogWriteFrequency(pwm_pin10, pwm_freq);
  digitalWrite(pwm_pin9, LOW);  
  digitalWrite(pwm_pin10, LOW);
  digitalWrite(ctrl_pin18, LOW);
  digitalWrite(ctrl_pin19, LOW);
}

void loop() {
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
  
  if(cmd_ready){    
    cmd_val = strtol(cmd_val_str.c_str(), NULL, 10);  //convert string to int
    Serial.print(cmd_str + "=");
    Serial.println(cmd_val, DEC);  //debug
        
    if(cmd_str == "pin9"){     
      cmd_val = cmd_val_check(cmd_val);  //check to make sure 0<=pwm<=255
      pinMode(pwm_pin10, OUTPUT);  //need to declare as GPIO before can be used as digital out
      digitalWrite(pwm_pin10, LOW);  //keep pmos on while pulsing nmos
      analogWrite(pwm_pin9, cmd_val);  //pulse nmos to generate high positive voltage
    } else if (cmd_str == "pin10"){      
      cmd_val = cmd_val_check(cmd_val);  //check to make sure 0<=pwm<=255
      pinMode(pwm_pin9, OUTPUT);  //need to declare as GPIO before can be used as digital out
      digitalWrite(pwm_pin9, HIGH);  //keep nmos on while pulsing pmos
      analogWrite(pwm_pin10, cmd_val);  //pulse pmos to generate high negative voltage
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
    } 
    
    cmd_ready = false;
    cmd_str = "";
    cmd_val_str = "";
  }
}

int cmd_val_check(int cmd_val){
  if(cmd_val > 255){
    cmd_val = 255;
  } else if (cmd_val < 0){
    cmd_val = 0;
  }
  return cmd_val;
}

