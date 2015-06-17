//============================================================================
// Name        : Code3b.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;


//void version1(int (*ptr)[col_size]){
//	for(auto &row : ia){
//		for(int &col : row){
//			cout << "ia[3][4] = " << col;
//		}//end of column
//	}//end of row
//}

int main() {
	int ia[3][4] = {{0,1,2,3},
					{4,5,6,7},
					{8,9,10,11}};
	const int row_size = sizeof(ia)/sizeof(ia[0]);
	const int col_size = sizeof(ia[0])/sizeof(ia[0][0]);

	//method 1: using pointers
	cout << "ia[3][4] = ";
	for(int (*row)[col_size] = ia; row != ia + row_size; ++row){	//row
		for(int *col = *row; col != *row + col_size; ++col){ //column
			cout << *col << " ";
		}
	}

	//method 2: using subscript
	cout << "\n" << "ia[3][4] = ";
	for(int row = 0; row < row_size; ++row){	//row
		for(int col = 0; col < col_size; ++col){ //column
			cout << ia[row][col] << " ";
		}
	}

	//method 3: using range for
	cout << "\n" << "ia[3][4] = ";
	for(int (&row)[col_size] : ia){	//row
		for(int &col : row){		//column
			cout << col << " ";
		}
	}

	return 0;
}
