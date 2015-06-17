/*============================================================================
// Name        : CRC.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
Notes:
ctrl + / = comment
operators: http://www.cplusplus.com/doc/tutorial/operators/
============================================================================*/

#include <iostream>
using namespace std;

int main() {
//	int seed = 0xFFFF;	// short = 2 bytes = 16 bits
//	int poly = 0b10001000000100001;
	int poly = 0x07;
	int seed = 0x310;
	int data = 0x01;
	int data_size = 8;	//size of data in bits
	int CRC_size = 16;	//size of CRC in bits
	int MSB_CRC = 0;	//most significant bit of CRC
	int temp_CRC = 0;
	int current_CRC = 0;
	int temp_data = 0;


	cout << "Seed = " << hex << seed << endl;
	cout << "Poly = " << hex << poly << endl;

	current_CRC = seed;
	for (int i = data_size - 1; i >= 0; i --) { //perform calculation 8 times (from MSB to LSB)
		temp_data = data >> i;
		temp_data = temp_data & 1;	//"bit-wise and" to get individual bit of the data
		MSB_CRC = current_CRC >> (CRC_size - 1);
		MSB_CRC = MSB_CRC & 1;	//"bit-wise and" to get MSB of each CRC

		temp_CRC = current_CRC << 1; //add zero to the end to "XOR" ploy or 0
		if (temp_data^MSB_CRC) {	// if data bit "XOR" MSB_CRC bit = 1; use poly
			temp_CRC = temp_CRC ^ poly;
		} else if (!(temp_data^MSB_CRC)){	// if data bit "XOR" MSB_CRC bit = 0; use zero
			temp_CRC = temp_CRC ^ (0x0000);
		}
		current_CRC = temp_CRC & (0xffff); //only keep the least significant 16 bit as CRC
	}
	cout << "final CRC = " << hex << current_CRC;
	return 0;
}



