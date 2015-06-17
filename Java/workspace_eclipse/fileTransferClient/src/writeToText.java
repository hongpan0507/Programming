import java.io.*;
import java.util.Scanner;


public class writeToText {
	public static void main(String[] args) {
		String pathName = null;
		String winPathName = null;
		File currentFile = null;
		PrintWriter textFile;
		int count = 0;

		searchPath: while (true) {
			System.out.print("Enter File Path: ");
			Scanner input = new Scanner(System.in);
			winPathName = input.nextLine();
			pathName = winPathName.replace("\\", "/");
			currentFile = new File(pathName);
			//System.out.println(currentFile.getPath());
			//System.out.println(currentFile.getName());
			if (currentFile.isDirectory()) {
				try {
					textFile = new PrintWriter("C:\\Users\\hp\\Desktop\\delete"+ String.valueOf(count) +".txt");
					count ++;
					for(int i = 0; i < currentFile.list().length; i++){
						textFile.println(currentFile.getPath() + "\\" +currentFile.list()[i]);	
					}
					textFile.close();
				} catch(Exception e){
					System.out.println("Something went wrong!");
				}
			} else {
				System.out.println("Path Not Found");
				continue searchPath;
			}// end of else
		}// end of while
	}// end of main
}
