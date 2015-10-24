import java.util.Scanner;

public class cat {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		bear bearObject = new bear("rachel");
		System.out.println("Enter the name of first gf here: ");
		
		String temp = input.nextLine();
		bearObject.setName(temp);
		bearObject.saying();
	}
}
