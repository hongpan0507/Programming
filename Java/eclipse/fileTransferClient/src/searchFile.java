import java.util.Scanner;

public class searchFile {
	private Scanner input;
	private String currentDir;
	private String fileName;
	private String finalDest;
	private boolean exitDir = false;
	private boolean exitFile = false;

	// constructor
	public searchFile() {

	}// end of constructor

	// start
	public String run() {
		input = new Scanner(System.in);
		searchDir();
		searchFileName();
		if (exitDir || exitFile) {
			return "exit";
		} else {
			return finalDest;
		}
	}// end of run()

	// search for directories
	private void searchDir() {
		search: while (true) {
			System.out.print("Enter file Directory: ");
			currentDir = input.nextLine();
			if (currentDir.equalsIgnoreCase("exit")) {
				exitDir = true;
				break;
			} else if (currentDir.equalsIgnoreCase("cd")) {
				break search;
			} else {
				System.out.println("Current Directory: " + currentDir);
				break;
			}
		} // end of search: while()
	}// end of searchDir()

	// search for files
	public void searchFileName() {
		System.out.print("Enter file name: ");
		fileName = input.nextLine();
		if (fileName.equalsIgnoreCase("cd")) {
			searchDir();
		} else if (fileName.equalsIgnoreCase("exit")) {
			exitFile = true;
		} else {
			finalDest = currentDir + "\\" + fileName;
		} 
	} // end of searchFileName()
}
