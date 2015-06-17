////============================================================================
//// Name        :
//// Author      : hong
//// Version     :
//// Copyright   : no warranty; no guarantee
//// Description : frequency sampling using kissFFT + libsndfile
////=============================================================================
//
//#include <windows.h>
//#include <mmsystem.h>
//#include <Mmreg.h>	//defines wave formate
//#include <iostream>
//#include <stdio.h>
//#include <stdlib.h>
//#include <math.h>
////#include "kiss_fft.h"
//
//using namespace std;
//
//int main() {
//	int SampleRate = 44100;
//	int BitsPerSample = 16;
//	int channel = 1;
//	int RecordingTime = 10;
//	int BlockAlign = channel * BitsPerSample / 8;
//	int AvgBytesPerSec = SampleRate * BlockAlign;
//	int BufferSize = RecordingTime * SampleRate;
//	int magnitude = 0;
//    short int waveIn[BufferSize]; //buffer to store wave data //short int = 16 bits
//
//
//	for(int i = 0; i < BufferSize; i++){
//		waveIn[i] = 0;
//	}
//
//	HWAVEIN WaveInHandle;
//	HWAVEOUT WaveOutHandle;
//	WAVEHDR WaveHeader;
//	MMRESULT result;
//
//	//recording parameters
//	//more info at http://msdn.microsoft.com/en-us/library/windows/desktop/dd390970%28v=vs.85%29.aspx
//	WAVEFORMATEX WaveFormat;	// define the formate of waveform-audio data
//	WaveFormat.wFormatTag = WAVE_FORMAT_PCM; //format = pulse code modulation
//	WaveFormat.nChannels = channel;	// one channel = mono
//	WaveFormat.wBitsPerSample = BitsPerSample;	// 16 = high quality	8 = telephone
//	WaveFormat.nSamplesPerSec = SampleRate; // sampling rate
//	WaveFormat.nBlockAlign = BlockAlign;	// = channel * wBitsPerSample / 8
//	WaveFormat.nAvgBytesPerSec = AvgBytesPerSec; // = nSamplesPerSec * BlockAlign
//	WaveFormat.cbSize = 0;	// must be zero for WAVE_FORMATE_PCM
//
//	//Open the wave input device
//	result = waveInOpen(&WaveInHandle, WAVE_MAPPER, &WaveFormat, 0, 0, WAVE_FORMAT_DIRECT);
//	if(result) {
//		cout << "failed to open input device!";
//		return 1;
//	} //end of if
//
//	//set up and prepare header for input
//	WaveHeader.lpData = (LPSTR)waveIn;	//lpData = long pointer to the address of the waveform buffer
//	WaveHeader.dwBufferLength = BufferSize * 2; //dwBufferLength is size of array in bytes
//	WaveHeader.dwFlags = 0;	//must be zero before recording
//	WaveHeader.dwBytesRecorded = 0;
//	WaveHeader.dwLoops = 0;
//	WaveHeader.dwUser = 0;
//	waveInPrepareHeader(WaveInHandle, &WaveHeader, sizeof(WAVEHDR));
//
//	//insert a wave input buffer
//	result = waveInAddBuffer(WaveInHandle, &WaveHeader, sizeof(WAVEHDR));
//	if(result){
//		cout << "failed to read block from device";
//		return 1;
//	}//end of if
//
//	//start sampling input
//	result = waveInStart(WaveInHandle);
//	if(result){
//		cout << "failed to start recording!";
//		return 1;
//	}//end of if
//	Sleep(RecordingTime * 1000);	//sleep while recording
//
//
////	kiss_fft_cpx in[BufferSize], out[BufferSize];	//create complex array
////	size_t i;
////	for (i = 0; i < BufferSize; i++) {
////		in[i].i = 0;
////		in[i].r = waveIn[i];
////	}	//end of for
////
////	kiss_fft_cfg config = kiss_fft_alloc(BufferSize, 0, NULL, NULL); //forward FFT
////	kiss_fft(config, in, out);
////	free(config);
////
////	cout << "bin\t" << "real\t" << "imaginary\n";
////	for (i = 0; i < 1000; i++) {
////		//cout << i << "\t" << in[i].r << "\t" << in[i].i << "\n";
////		//cout << i << "\t" << out[i].r << "\t" << out[i].i << "\n";
////		magnitude = sqrt(out[i].r * out[i].r + out[i].i * out[i].i);
////		if (magnitude > 1) {
////			cout << i << "\t" << out[i].r << "\t" << out[i].i << "\n";
////		}
////	} //end of for
////
//
//
//	if(waveOutOpen(&WaveOutHandle, WAVE_MAPPER, &WaveFormat, 0, 0, WAVE_FORMAT_DIRECT)){
//		cout << "failed to play back!";
//	}//end of if
//	waveOutWrite(WaveOutHandle, &WaveHeader, sizeof(WAVEHDR));
//	Sleep(RecordingTime * 1000);	//sleep while playing
//
//
//	//cout << "WaveOutHandle: " << &WaveOutHandle <<"\tVaule: " << test;
//
//	waveOutUnprepareHeader(WaveOutHandle, &WaveHeader, sizeof(WAVEHDR));
//	waveInUnprepareHeader(WaveInHandle, &WaveHeader, sizeof(WAVEHDR));
//	waveInClose(WaveInHandle);
//	waveOutClose(WaveOutHandle);
//
//	return 0;
//}
//
