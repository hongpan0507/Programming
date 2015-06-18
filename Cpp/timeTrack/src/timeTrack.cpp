//============================================================================
// Name        : timeTrack.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

int main() {
	try {
		//string fileName = "G:/timeTrack.txt";
		ofstream ost("C:/timeTrack2.txt");	// ofstream = writing to a file
		if(!ost) throw 0;
		int month = 1;
		while(month < 13) {
			if(month%2) {	// max day = 31
				for(int day = 1; day < 32; ++day){
					ost << month << "/" << day << "/2014:	" << endl;
				}
			} else {	// max day = 30 except february
				for(int day = 1; day < 31; ++day){
					ost << month << "/" << day << "/2014:	" << endl;
				}
			}
			++month;
		}	//end of while
		ost.close();
	} catch (int error) {
		cout << "cannot write to the file";
	}
	return 0;
}
