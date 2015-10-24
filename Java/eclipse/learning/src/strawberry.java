import java.util.Scanner;

public class strawberry {
	public static void main(String args[]){
		//double bear;
		//bear = 3.14;
		//System.out.println("I want "); //println will put the cursor to a new line after printing
		//System.out.print(bear);
		
		//Scanner OptimusPrime = new Scanner(System.in);
		//System.out.println(OptimusPrime.nextLine());
		
		/*
		Scanner blueBerry = new Scanner(System.in);
		double fnum, snum, ans;
		
		System.out.println("Enter first number ");
		fnum = blueBerry.nextDouble();
		System.out.println("Enter second number ");
		snum = blueBerry.nextDouble();
		ans = fnum + snum;
		System.out.print("the answer is ");
		System.out.println(ans);
		*/
		
		/*
		int bear = 10;
		System.out.println(bear++);
		bear = 10;
		System.out.println(++bear);
		*/
		
		/*
		 switch(age){
		 case 1:
		 	System.out.println("You suck");
		 	break;
		 case 2:
		 	break;
		 default:
		 	System.out.println("You still suck");
		 	break;
		 } 
		 */
		
		
		/* a way to use multiply classes
		blueberry blueberryStuff = new blueberry();
		blueberryStuff.message();
		*/
		
		Scanner input = new Scanner(System.in);
		blueberry blueberryObject = new blueberry();
		
		System.out.println("Enter your name here: ");
		String name = input.nextLine();
		
		blueberryObject.message(name);
	}
}
