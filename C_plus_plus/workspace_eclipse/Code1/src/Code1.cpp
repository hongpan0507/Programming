//============================================================================
// Name        : Code1.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : assignment 1
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int num1 = 0;
	int num2 = 0;
	int sum = 0;
	int quit = 1;

	cout << "enter two integer to add" << endl;

	while(quit == 1){
		cout << "first number: ";
		cin >> num1;
		cout <<"second number: ";
		cin >> num2;

		sum = num1 + num2;
		cout << num1 << "+" << num2 << "=" << sum <<endl;
		cout << "Try again?" <<"Yes == 1; No == 0" <<endl;
		cin >> quit;
	}	//end of while

	return 0;
}
