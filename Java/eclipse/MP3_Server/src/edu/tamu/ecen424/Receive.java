package edu.tamu.ecen424;

import java.io.*;

public class Receive extends Thread{
	private ObjectInputStream iStream;
	private String message = "";
	private String ClientIP = "";
	private int portNumb = 0;
	
	public Receive(ObjectInputStream Stream, String IP, int port){
		iStream = Stream;
		ClientIP = IP;
		portNumb = port;
	}	//end of constructor
	
	public void run(){
		try{
			while(message != "disconnect"){
				message = (String) iStream.readObject();
				System.out.print("\nClient @ " + ClientIP + " + " + portNumb + ": ");
				System.out.println(message);
			}	//end of while
			System.out.println("Connection terminated by the client @ " + ClientIP + " + " + portNumb);
			iStream.close();
		} catch (Exception e) {
			System.out.println("Error occurred when receiving message");
		}	//end of try block
	}	//end of run	
}
