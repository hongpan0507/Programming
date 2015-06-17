package edu.tamu.ecen424;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

public class Receive extends Thread{
	private ObjectInputStream iStream;
	private Socket sock;
	private String message = "";
	private String ServerIP = "";
	private int portNumb = 0;
	
	public Receive(Socket socket, String IP, int port) throws IOException{
		sock = socket;
		iStream = new ObjectInputStream(sock.getInputStream());
		ServerIP = IP;
		portNumb = port;
	}	//end of constructor
	
	public void run(){
		try{
			while(message != "disconnect"){
				message = (String) iStream.readObject();
				System.out.print("\nServer @ " + ServerIP + " + " + portNumb + ": ");
				System.out.println(message);
			}	//end of while
			System.out.println("Connection terminated by the client @ " + ServerIP + " + " + portNumb);
			iStream.close();
		} catch (Exception e) {
			System.out.println("Error occurred when receiving message");
		}	//end of try block
	}	//end of run	
}
