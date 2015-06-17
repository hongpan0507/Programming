/*
 * test.cpp
 *
 *  Created on: Jul 13, 2013
 *      Author: hp
 */
#include <stdio.h>

int my_array[] = { 1, 2, 3, 4, 5, 6 };
int *ptr;

int main() {
	//ptr = &my_array[0];
	ptr = my_array;
	for(int i = 0; i < 6; i++){
		printf("my_array[%d] = %d\t", i, my_array[i]);
		//printf("ptr + %d = %d\n", i, *(ptr + i));
		printf("ptr + %d = %d\n", i, *ptr++);
	}

}

