import java.util.Scanner;
import java.io.*;

public class destoryFile {
	public static void main(String[] args) {
		String buffer = null;
		String path = null;
		Scanner input;
		Scanner keyIn;

		deleteFile del = new deleteFile();
		while (true) {
			System.out.print("Enter path: ");
			keyIn = new Scanner(System.in);
			path = keyIn.nextLine();
			for (int count = 0; count <= 4; count++) {
				try {
					input = new Scanner(new File(
							"C:\\Users\\hp\\Desktop\\delete"
									+ String.valueOf(count) + ".txt"));
					while (input.hasNext()) {
						buffer = input.nextLine();
						del.run(path, buffer);
					}// end of while
				} catch (Exception e) {
					System.out.println("Something went wrong!");
				}// end of catch()
			}// end of for
		}// end of while
	}// end of main
}
