//============================================================================
// Name        : Code2.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : assignment2
//============================================================================

#include <iostream>
#include "TemperatureData.h"
using namespace std;

TemperatureData data1;
double TempCel = 0.0;
double TempFah = 0.0;
double TempKel = 0.0;
bool temp = true;

void UnitToUnit() {
	if (data1.scale == "C") {
		TempFah = data1.temperature * 9 / 5 + 32.0;
		TempKel = data1.temperature + 273.15;
		TempCel = data1.temperature;
	} else if (data1.scale == "F") {
		TempCel = (data1.temperature - 32.0) * 5 / 9;
		TempKel = TempCel + 273.15;
		TempFah = data1.temperature;
	} else if (data1.scale == "K") {
		TempCel = data1.temperature - 273.15;
		TempFah = TempCel * 9 / 5 + 32.0;
		TempKel = data1.temperature;
	} else {
		temp = false;
	} //end of else
} //end of UnitToUnit

void FirstApp() {
	while (true) {
		cout << "Enter the temperature: ";
		cin >> data1.temperature;
		cout << "Enter the unit: ";
		cin >> data1.scale;
		cout << "Enter the year: ";
		cin >> data1.year;
		UnitToUnit();
		if (temp) {
			if (TempKel < 0) {
				cout << "Impossible Temperature! Out of Range!\n";
			} else {
				cout << "Year: " << data1.year << "\n";
				cout << "Temperature: " << TempCel << "C\t" << TempFah << "F\t"
						<< TempKel << "K\n";
			} //end of else
		} else {
			cout << "Unknown unit!\n";
		} //end of else
	} // end of while
} //end of firstApp

void SecondApp() {
	double TempBuffCel = 0.0;
	double TempBuffFah = 0.0;
	double TempBuffKel = 0.0;

	while (true) {
		cout << "Enter the first temperature: ";
		cin >> data1.temperature;
		cout << "Enter the unit: ";
		cin >> data1.scale;

		UnitToUnit();

		TempBuffCel = TempCel;
		TempBuffFah = TempFah;
		TempBuffKel = TempKel;

		cout << "Enter the second temperature: ";
		cin >> data1.temperature;
		cout << "Enter the unit: ";
		cin >> data1.scale;

		UnitToUnit();

		if (temp) {
			if (TempKel < 0) {
				cout << "Impossible Temperature! Out of Range!\n";
			} else if (TempBuffCel < TempCel) {
				cout << "Temperature: " << TempCel << "C\t" << TempFah << "F\t"
						<< TempKel << "K\n";
			} else if (TempBuffCel > TempCel) {
				cout << "Temperature: " << TempBuffCel << "C\t" << TempBuffFah
						<< "F\t" << TempBuffKel << "K\n";
			} else if (TempBuffCel == TempCel) {
				cout << "Temperature: " << TempCel << "C\t" << TempFah << "F\t"
						<< TempKel << "K\n";
			}
		} else {
			cout << "Unknown unit!\n";
		} //end of else
	} // end of while
} //end of secondApp

int main() {
	int select = 0;
	cout << "1 = first app\t" << "2 = second app\n";
	cin >> select;
	if (select == 1) {
		FirstApp();
	} else if (select == 2) {
		SecondApp();
	} else {
		cout << "No such option!\t";
	}
} //end of main
