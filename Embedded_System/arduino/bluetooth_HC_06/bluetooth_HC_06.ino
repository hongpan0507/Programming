/******************************************************************
Tutorials:
  # http://mcuoneclipse.com/2013/06/19/using-the-hc-06-bluetooth-module/
  # http://forcetronic.blogspot.com/2014/08/getting-started-with-hc-06-bluetooth.html

Device Notes:
  # HC_06 = CSR_BC417143 (bluetooth) + MX29LV800C (CMOS Flash)
    MX29LV800C; Macronix Internatinal Co; http://www.macronix.com/en-us/Product/Pages/ProductDetail.aspx?PartNo=MX29LV800C%20T/B     
  # Default parameter: Baud rate = 9600N81; ID = linvor; Password = 1234  

Programming Notes:
  # The Arduino Leonardo board uses Serial1 to communicate via TTL(Transistor to Transistor Level) serial on pins 0 (RX) and 1 (TX). 
  # Serial is reserved for USB CDC (Communication Device Class) communication
********************************************************************/

//--------------PC, Leonardo command variable-----------------
int cmd_val = 0;  
char cmd_char;
String cmd_str = "";
String cmd_val_str = "";
boolean cmd_ready = false;
boolean cmd_type_ready = false;
//-------------------------------------------------------------------
//--------------HC-06, Leonardo command variable-----------------
int bt_cmd_val = 0;  
char bt_cmd_char;
String bt_cmd_str = "";
String bt_cmd_val_str = "";
boolean bt_cmd_ready = false;
boolean bt_cmd_type_ready = false;
//-------------------------------------------------------------------
int led = 11;

void setup() {
  Serial.begin(9600); 
  Serial1.begin(9600); 
  pinMode(led, OUTPUT); 
  bluetooth_initialize();
}

void loop() {
  //--------------PC, leonardo command exchange---------------------------
  if(Serial.available()) {  //USB CDC communication; non-blocking; use while for blocking
    cmd_char = Serial.read();    
    if(cmd_char == '='){  //delimiter for determining the type of incoming cmd 
      cmd_type_ready = true;      
    } else if (cmd_char == ';'){  //delimiter of the end of incoming cmd; can be used for resetting cmd
      cmd_ready = true;      
      cmd_type_ready = false;   
    } else if (cmd_type_ready == false){  //accumulate charactor for cmd type
      cmd_str += cmd_char;
    } else if (cmd_type_ready == true){  //accumulate charactor for cmd value
      cmd_val_str += cmd_char;
    }   
  }     
  //--------------------------------------------------------------------- 
  //-----------------HC_06, Leonardo command exchange------------------   
  if(Serial1.available()) {  //RX, TX TTL communication; non-blocking; use while for blocking
    bt_cmd_char = Serial1.read();    
    if(bt_cmd_char == '='){  //delimiter for determining the type of incoming cmd 
      bt_cmd_type_ready = true;      
    } else if (bt_cmd_char == ';'){  //delimiter of the end of incoming cmd; can be used for resetting cmd
      bt_cmd_ready = true;      
      bt_cmd_type_ready = false;   
    } else if (bt_cmd_type_ready == false){  //accumulate charactor for cmd type
      bt_cmd_str += bt_cmd_char;
    } else if (bt_cmd_type_ready == true){  //accumulate charactor for cmd value
      bt_cmd_val_str += bt_cmd_char;
    }   
  }
  //---------------------------------------------------------------------

  //-----------------PC, Leonardo, HC_06 command exchange------------------  
  if(cmd_ready){   
    if(cmd_str == "AT_cmd"){  
      String AT_res = hc_bt_comm(cmd_val_str); 
      Serial.println(AT_res);  
    } else if (cmd_str == "BT_comm"){
      
    } else {
      Serial.println("command not recognized");
    }    
    cmd_ready = false;    //reset for command input
    cmd_str = "";  //reset for command input
    cmd_val_str = "";  //reset for command input
  }  
  
  if(bt_cmd_ready){   
    if(bt_cmd_str == "BT_comm"){  
      Serial.println(bt_cmd_val_str);  
    } else {
      Serial.println("command not recognized");
    }    
    bt_cmd_ready = false;    //reset for command input
    bt_cmd_str = "";  //reset for command input
    bt_cmd_val_str = "";  //reset for command input
  }  
  //--------------------------------------------------------------------    
}

void bluetooth_initialize(){
  delay(2000);    
  Serial.println(hc_bt_comm("AT"));   
  delay(500);
  Serial.println(hc_bt_comm("AT+VERSION"));   //hc_06 firmware versio
  delay(500);
  Serial.println(hc_bt_comm("AT+BAUD4"));   //set hc_06 baud rate to 9600; check on datasheet for more parameter
  delay(500);
  Serial.println(hc_bt_comm("AT+NAMEAtmega32_u4"));   //set bluetooth name to Atmega32_u4
  delay(500);
  Serial.println(hc_bt_comm("AT+PIN9600"));   //set bluetooth password to 9600
  delay(500);
  Serial.println(hc_bt_comm("AT+PO"));   //set hc_06 odd parity check on
  Serial.println("Bluetooth parameters all set");
}

String hc_bt_comm(String cmd_val_str){
  String cmd_res = "";  
  Serial1.write(cmd_val_str.c_str());  //RX, TX TTL communication
  delay(550); //HC06 requires 500 msec for reply
  while(Serial1.available()){    //RX, TX TTL communication
    char cmd_return = (char)Serial1.read();     //receive returned commands
    cmd_res += cmd_return;   
    digitalWrite(led,HIGH);
    delay(10); 
    digitalWrite(led,LOW);
  }   
  return cmd_res;  
}
