import java.util.Scanner;

public class test {
	public static void main(String[] args) {
		String IP;

		Scanner input = new Scanner(System.in);
		IPCheck checkIP = new IPCheck();

		goTo: while (true) {
			try {
				System.out.print("Enter ip address: ");
				IP = input.nextLine();

				if (checkIP.run(IP)) {
					System.out.println("good ip");
				} else {
					System.out.println("bad- ip");
				}
			} catch (NumberFormatException n) {
				System.out.println("bad+ ip");
				continue goTo;
			}//end of catch
		}
	}
}
