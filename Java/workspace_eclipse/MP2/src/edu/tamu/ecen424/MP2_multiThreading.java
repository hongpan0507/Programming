package edu.tamu.ecen424;

import java.util.*;

public class MP2_multiThreading {
	public static void main(String[] args) throws InterruptedException {		
		int a1[][]=new int[20][20];	//row X column
		int a2[][]=new int[20][20];	//row X column
		array_stuffing(a1);
		array_stuffing(a2);
		System.out.println("First array: ");
		array_display(a1);
		System.out.println("Second array: ");
		array_display(a2);
		
		//dividing matrix
		int d1[][] = array_divide(a1, 4, 0);
		int d2[][] = array_divide(a1, 4, 4);
		int d3[][] = array_divide(a1, 4, 8);
		int d4[][] = array_divide(a1, 4, 12);
		int d5[][] = array_divide(a1, 4, 16);
		
		//using thread
		using_thread t1 = new using_thread(d1,a2);
		using_thread t2 = new using_thread(d2,a2);
		using_thread t3 = new using_thread(d3,a2);
		using_thread t4 = new using_thread(d4,a2);
		using_thread t5 = new using_thread(d5,a2);
		t1.start();
		t2.start();
		t3.start();
		t4.start();
		t5.start();
		t1.join();
		t2.join();
		t3.join();
		t4.join();
		t5.join();
		int result1[][] = t1.get();
		int result2[][] = t2.get();
		int result3[][] = t3.get();
		int result4[][] = t4.get();
		int result5[][] = t5.get();

		
		System.out.println("Product array from using thread: ");
		array_display(result1);
		array_display(result2);
		array_display(result3);
		array_display(result4);
		array_display(result5);
		
		//normal way computing
		int result6[][] = array_product(a1, a2);		
		System.out.println("Product array from normal way computing: ");
		array_display(result6);
	} //end of main
	
	public static void array_stuffing(int array[][]){
		Random rand = new Random();
		for(int row = 0; row < array.length; ++row){
			for(int column = 0; column < array[row].length; ++column){
				array[row][column] = rand.nextInt(10);
			}
		}	
	}	//end of array_stuffing
	
	public static int[][] array_product(int array1[][], int array2[][]){
		int product[][] = new int[array1.length][array2[1].length];
		int i = 0;
		for(int row1 = 0; row1 < array1.length; ++row1){
			for(int row2 = 0; row2 < array2.length; ++row2){
				for(int j = 0; j < array1[row1].length; ++j){
					i += array1[row1][j] * array2[j][row2];
				}
				product[row1][row2]= i;
				i = 0;
			}
		}	
		return product;
	}	//end of array_product
	
	public static void array_display(int array[][]){
		for(int row = 0; row < array.length; ++row){
			for(int column = 0; column < array[row].length; ++column){
				System.out.print(array[row][column] + " ");
			}
			System.out.println();
			System.out.println();
		}
	} //end of array_display
	
	public static int[][] array_divide(int array[][], int numb, int start){
		int result[][] = new int [numb][array[1].length];
		for(int row = start, i = 0; row < numb+start; ++row, ++i){
			for(int column = 0; column < array[row].length; ++column){
				result[i][column] = array[row][column];
			}
		}
		return result;
	}	//end of array_divide
	
}	//end of the world
