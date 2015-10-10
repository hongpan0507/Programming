import java.util.Scanner;

public class averaging_number {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int total =0;
		int grade =0;
		int average = 0;
		int counter = 0;
		int inputNum = 0;
		
		System.out.print("How many numbers do you have to add? ");
		inputNum = input.nextInt();
		
		System.out.println("Enter the grades: ");
		
		while (counter < inputNum){
			grade = input.nextInt();
			total += grade;
			counter++;
		}
		
		average = total/counter;
		System.out.println("The average is " + average);
	}
}
