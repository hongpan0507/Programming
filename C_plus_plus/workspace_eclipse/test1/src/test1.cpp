//============================================================================
// Name        : test1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <time.h>
#include <sstream>

using namespace std;

int main() {
	time_t current_time = time(0);
	string time_parse = ctime(&current_time);
	string local_time = " ";
	string temp = " ";
	for(int i = 0; i < time_parse.size(); ++i) {
		if (i > 10 && i < 19) {
			stringstream ss;
			ss << time_parse[i];
			ss >> temp;
			local_time = local_time + temp;
		}
	}
	cout << "It is" << local_time << " in aggieland" << endl;
	return 0;
}


