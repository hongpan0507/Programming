package edu.tamu.ecen424;

public class using_thread  extends Thread {
	int b1[][];
	int b2[][];
	int result[][];
	
	public using_thread(int a1[][], int a2[][]){
		b1 = a1;
		b2 = a2;
	}	//end of constructor
	
	public void run(){
		result = array_product(b1, b2);
	}	//end of run
		
	public int[][] get(){
		return result;
	}
	 
	public int[][] array_product(int array1[][], int array2[][]){
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
}	//end of world
