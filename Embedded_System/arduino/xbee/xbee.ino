int baud_rate = 115200;
int count_byte = 0;
int xbee_in = 0;
int start_delimiter = 0x7E;
int frame_len = 0;  //size of frame data in bytes excluding checksum, length, start delimiter
int frame_len_MSB = 0;
int frame_len_LSB = 0;
int API_id = 0;
int source_addr = 0;
int source_addr_MSB = 0;
int source_addr_LSB = 0;
int RSSI_val = 0;
int option = 0;
int data_byte = 0;
int check_sum = 0;
boolean FS = false;  //frame start

void setup() {
  // put your setup code here, to run once:
  Serial1.begin(baud_rate);
  Serial.begin(baud_rate);
}

void loop() {
  // put your main code here, to run repeatedly: 
  if(Serial1.available()){
    xbee_in = Serial1.read();
    if(FS == true){
      ++count_byte;
      if(count_byte == 2){  //2nd byte = MSB of length
        frame_len_MSB = xbee_in; 
        frame_len_MSB = frame_len_MSB << 8;  //1 byte = 8 bits
      }
      if(count_byte == 3){  //3rd byte = LSB of length
        frame_len_LSB = xbee_in; 
        frame_len = frame_len_MSB | frame_len_LSB;  //bitwise or to get the length of frame data; max length = 0x64 (100 in dec)
        Serial.print("frame Length (dec) = ");
        Serial.println(frame_len, DEC);
      }
      if(count_byte == 4){  //4rd byte = API identifier
        API_id = xbee_in;         
        Serial.print("API identifier (hex) = ");
        Serial.println(xbee_in, HEX);
      }
      if(API_id == 0x81){
        if(count_byte == 5){  //5th byte = MSB of source address
          source_addr_MSB = xbee_in;   
          source_addr_MSB = source_addr_MSB << 8; //1 byte = 8 bits
        }
        if(count_byte == 6){  //6th byte = LSB of source address
          source_addr_LSB = xbee_in;   
          source_addr = source_addr_MSB | source_addr_LSB; //bitwise or to get source address
          Serial.print("Source Address (hex) = ");
          Serial.println(source_addr, HEX);
        }
        if(count_byte == 7){  //7th byte = RSSI
          RSSI_val = xbee_in;           
          Serial.print("RSSI (dBm) (dec) = -");
          Serial.println(RSSI_val, DEC);
        }
        if(count_byte == 8){  //8th byte = options; bit 7-3 = [reserved], bit 2 = PAN broadcast, bit 1 = address of broadcast, bit 0 = [reserved]
          option = xbee_in;           
          Serial.print("option (bin)= ");
          Serial.println(option, BIN);
        }
        if(count_byte > 8 && count_byte <= frame_len + 3){  // 3 is the first 3 bytes in the packet
          data_byte = xbee_in;
          Serial.print("Data (dec) = ");
          Serial.println(data_byte, DEC);
        }
        if(count_byte > frame_len + 3){  // 3 is the first 3 bytes in the packet
          check_sum = xbee_in;
          Serial.print("Check Sum (hex) = ");
          Serial.println(check_sum, HEX);
          FS = false;
          count_byte = 0;
        }                
      }
    } else if(xbee_in == start_delimiter){  //1st byte = start delimiter
      ++count_byte;
      FS = true;      
      Serial.print("Start Delimiter (hex) = ");
      Serial.println(xbee_in, HEX);
    }
  }
}
