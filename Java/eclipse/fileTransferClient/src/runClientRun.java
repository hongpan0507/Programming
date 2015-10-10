import java.util.Scanner;

public class runClientRun {
	public static void main(String[] args) {

		String serverIP;
		String fileDir; // "C:/Users/hp/Desktop/summer 2013/assignment1.docx";
		String finalDest;
		String fileName;

		fileTransferClient client = new fileTransferClient();

		Scanner input = new Scanner(System.in);
		IPCheck ip = new IPCheck();

		newIP: while (true) {
			System.out.print("Enter Sever IP: ");
			serverIP = input.nextLine();
			try {
				if (ip.run(serverIP)) {
					System.out.println("Connnecting to: " + serverIP);
				} else {
					System.out.println("Invalid IP address");
					continue newIP;
				}// end of else
			} catch (NumberFormatException n) {
				System.out.println("invalid IP address");
				continue newIP;
			}// end of catch
			
			searchDir: while (true) {
				System.out.print("Enter file Directory: ");
				fileDir = input.nextLine();
				if (fileDir.startsWith("IP")) {
					continue newIP;
				} else {
					System.out.println("Current Directory: " + fileDir);
					searchFile: while (true) {
						System.out.print("Enter file name: ");
						fileName = input.nextLine();
						if (fileName.equalsIgnoreCase("cd")) {
							continue searchDir;
						} else if(fileName.equalsIgnoreCase("exit")){
							break;
						} else {
							finalDest = fileDir + fileName;
							client.runClient(serverIP, finalDest);
							continue searchFile;
						} // end of second else
					} //end of searchFile
				}// end of first else
			}// end of searchDir
		}// end of first while
		
	}// end of main
}

/*
 * cdDir = fileDir.startsWith("cd");
 * 
 * if (cdDir == true) { newfileDir = fileDir.substring(3);
 * System.out.println("Current Directory: " + newfileDir);
 * System.out.println("Enter file name: "); fileName = input.nextLine();
 * 
 * if (cdDir = fileName.startsWith("cd")) { continue search; } else { finalDest
 * = newfileDir + fileName; client.runClient(serverIP, finalDest); } }// end of
 * if else {
 */