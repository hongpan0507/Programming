//============================================================================
// Name        : Code3.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>
#include <vector>
#include <stdlib.h>

using namespace std;



int main() {
	vector<double> temperature;
	string temp;
	string input;
	double buff = 0.0;
	double TempCel = 0.0;

	cout << "Seperate all the numbers by space and end the last number with \";\"" << endl;
	cout << "Enter the temperatures in Fahrenheit: ";
	while (cin >> input) {
		if (input[input.size() - 1] != ';') {
			buff = atof(input.c_str());
			temperature.push_back(buff);
		} else if (input.size() >= 2) {
			for (unsigned int i = 0; i < input.size() - 1; ++i) {
				temp += input[i];
			}	//end of for
			buff = atof(temp.c_str());
			temperature.push_back(buff);
			break;
		} else if(temperature.size() == 0){
			cout << "NO DATA has been recorded ! Please retry: " << endl;
		} else {
			break;
		}	//end of else
	}	//end of while


	cout <<"\n" <<"Number of temperature data available: " << temperature.size() << endl;
	cout << "Temperature: " << endl;
	cout << "In Fahreheit: \t" << "In Celsuis: " << endl;

	for (auto &TempFah : temperature) {
		TempCel = (TempFah - 32.0) * 5 / 9;
		cout << setw(9) << fixed << setprecision(1) << TempFah << "\t";
		cout << setw(9) << fixed << setprecision(1) << TempCel << endl;
	}	//end of for

	return 0;
}
