#define LOG_OUT 1 // use the log output function
#define FFT_N 256 // set to 256 point fft
#include <FFT.h> // include the library

void setup() {
  Serial.begin(9600); // use the serial port
}

void loop() {
  // put your main code here, to run repeatedly: 
  float k = 0;
  float t = 0;
  for (int i = 0 ; i < 512 ; i += 2) { // save 256 samples
    k = 1024 * sin(2*3.14159 * 100 * t / 1000 );
    t++;
    fft_input[i] = k; // put real data into even bins
    fft_input[i+1] = 0; // set odd bins to 0
  }
  fft_window(); // window the data for better frequency response
  fft_reorder(); // reorder the data before doing the fft
  fft_run(); // process the data in the fft
  fft_mag_log(); // take the output of the fft
  for(int i = 0; i < 128; i++){
    Serial.print("bin #: ");
    Serial.print(i);
    Serial.print("\t");
    Serial.print("log mag: ");
    Serial.println(fft_log_out[i]);
  }
  delay(1000); 
}

