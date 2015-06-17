//// sineosc.cpp
//
//#include "FileLoop.h"
//#include "FileWvOut.h"
//using namespace stk;
//using namespace std;
//
//int main()
//{
//  // Set the global sample rate before creating class instances.
//  Stk::setSampleRate( 44100.0 );
//
//  FileRead input;
//  //StkFloat output;
//  StkFrames sample(40000, 1);
//
//  // Load the sine wave file.
//  input.open( "C:/Users/hp/Desktop/sine_500Hz.wav", true );
//  input.read(sample);
//  // Run the oscillator for 40000 samples, writing to the output file
////  for ( int i=0; i<40000; i++ )
////    sample[i] = input.tick();
//  for(int i = 0; i < 1000; i+=10)
//  	cout << sample[i] << endl;
//
//  return 0;
//}
