import java.io.File;
import java.util.Scanner;

public class deleteFile {

	private int fileTotal = 0;
	//private boolean fileCheck = true;
	
	// constructor
	public deleteFile() {

	}// end of constructor

	public void run(String pathName, String deleteFile) {
		fileSearch(filePath(pathName), deleteFile);
		System.out.println("Number of files deleted: " + fileTotal);
		//fileTotal = 0;
	}// end of run()

	private String filePath(String winPathName) {
		String pathName = null;
		//String winPathName = null;

		//System.out.print("Enter File Path: ");
		//Scanner input = new Scanner(System.in);
		//winPathName = input.nextLine();
		// input.close();	
		winPathName = winPathName.trim();
		pathName = winPathName.replace("\\", "/");
		if (pathName.endsWith("/") && pathName.length() > 3) {
			pathName = pathName.substring(0, (pathName.length() - 1));
			return pathName;
		} else {
			return pathName;
		}
	}// end of filePath()
	
	//Search for specific file
	private void fileSearch(String pathName, String deleteFile){
		String newPathName = null;
		
		File searchFile = new File(pathName);
		for(int i = 0; i < searchFile.list().length; i++){
			if(searchFile.list()[i].equals(deleteFile)){
				File newFile = new File(searchFile.getPath() + "/" + searchFile.list()[i]);
				newPathName = filePath(newFile.getPath());
				fileDestory(newPathName);
				//System.out.println(newPathName);
			}
		}
	}//end of fileSearch()
	
	// Destory all the files and folders
	private void fileDestory(String pathName) {
		String fileName = null;
		String fileArray[] = null;
		int fileCount = 0;

		File currentFile = new File(pathName);
		if (currentFile.isDirectory()) {
			fileCount = currentFile.list().length;
			fileArray = currentFile.list();
			//if(currentFile.list().length == 0) {currentFile.delete();} // comment this out if keep parent folder
			for (int i = 0; i < fileCount; i++) {
				fileName = pathName + "/" + fileArray[i];
				File newFile = new File(fileName);
				while (newFile.isDirectory()) {
					if (newFile.list().length > 0) {
						fileDestory(newFile.getPath());
					} else {
						newFile.delete();
					}
				}// end of while
				if (newFile.isFile()) {
					if (newFile.delete()) {
						fileTotal++;
					} else {
						System.out.println("Fail to delete: ");
						System.out.println(newFile.getPath());
					}// end of else
				}// end of if()
			}// end of for()
		} else if (currentFile.isFile()) {
			if (currentFile.delete()) {
				fileTotal++;
			} else {
				System.out.println("Fail to delete: ");
				System.out.println(currentFile.getPath());
			}// end of else
		}//end of else if()
	}// end of fileSearch()
}// end of deleteFile()