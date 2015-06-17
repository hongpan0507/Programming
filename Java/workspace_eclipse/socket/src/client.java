import java.io.*;
import java.net.*;
import java.util.Scanner;

public class client {
	public static void main(String args[]){
	
		//variable declaration
		int PortNumber = 2013;
		Socket MyClient = null;
		ObjectInputStream ServerInput = null;
		//ObjectOutputStream ClientOutput = null;
		PrintWriter ClientOutput = null;
		String response;
		String UserInput;
		
		//setup IO and socket
		try{
			MyClient = new Socket("127.0.0.1",PortNumber); // create client socket
			ServerInput = new ObjectInputStream(MyClient.getInputStream()); // create input stream to receive response from the server
			//ClientOutput= new ObjectOutputStream(MyClient.getOutputStream());	//create output stream to send info to the server
			ClientOutput = new PrintWriter(MyClient.getOutputStream(), true);
		}	//end of try
		
		catch(UnknownHostException e){
			System.err.println("Unknown Host");
		}	//end of UnknownHost catch
		catch(IOException e){
			System.err.println("No connection");
		}	//end of IO catch
		
		//service part
		while(true) {
			//if(MyClient != null && ServerInput != null && ClientOutput != null){
				try{
					Scanner ClientInput = new Scanner(System.in); 
					System.out.print("Cleint: ");
					UserInput = ClientInput.next();
					
					ClientOutput.println(UserInput + "\n"); //send the message to the server
				
					while((response = ServerInput.readLine()) != null) {
						System.out.println("Server: " + response);
						if (response.indexOf("OK") != -1) {break;} //??????????????????????
					}	//end of while
					
	
				}catch(UnknownHostException e){
					System.err.println("Unknown Host");
				}catch(IOException e){
					System.err.println("IOException: " + e);
				}	//end of IO catch
			//}	//end of if
		}	// end of while(true)
	}	//end of main
}	//end of class client
