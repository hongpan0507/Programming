//#include "FileLoop.h"
//#include "FileWvOut.h"
//#include <iostream>
//#include <stdio.h>
//#include <stdlib.h>
//#include <math.h>
//#include "kiss_fft.h"
//using namespace stk;
//using namespace std;
//
//int main() {
//	// Set the global sample rate before creating class instances.
//	//Stk::setSampleRate(44100.0);
//
//	FileRead input;
//	//StkFloat output;
//	StkFrames sample(44100, 1);
//	double mag = 0;
//	int size = 44100;
//
//
//	// Load the sine wave file.
//	input.open("E:/programming/eclipse/downloadedLib/stk/rawwaves/sinewave.raw", true);
//	input.read(sample);
//
//	kiss_fft_cpx in[size], out[size];	//create complex array
//	size_t i;
//	for (i = 0; i <size; i++) {
//		in[i].i = 0;
//		in[i].r = sample[i];
//	}	//end of for
//
//	kiss_fft_cfg config = kiss_fft_alloc(size, 0, NULL, NULL); //forward FFT
//	kiss_fft(config, in, out);
//	free(config);
//
//	cout << "bin\t" << "Mag\n";
//	for (i = 0; i < size/2; i++) {
//		mag = sqrt(out[i].r * out[i].r + out[i].i * out[i].i);
//		if(mag > 100)
//		cout << i <<"\t" << mag << endl;
//
//	} //end of for
//
//
//	return 0;
//}
