package edu.tamu.ecen424;

import java.net.*;
import java.util.Scanner;

public class Server {
	public static void main(String[] args) {
		ServerSocket server = null;
		Socket sock;
		Scanner keyboard = new Scanner(System.in);
		String buff = "";
		int portNumb = 3322;
		int maxConnection = 10;
		
		try {			
			System.out.print("Enter the port number to listen on: ");
			buff = keyboard.nextLine();
			portNumb = Integer.parseInt(buff);
			System.out.print("Enter the maximum number of clients that is allowed to connect to this server: ");
			buff = keyboard.nextLine();
			maxConnection = Integer.parseInt(buff);
			server = new ServerSocket(portNumb, maxConnection);
			String serverIP = InetAddress.getLocalHost().getHostAddress();
			System.out.println("Server IP: " + serverIP);
			System.out.println("Server has been created to listen on port " + portNumb + " with max # of clients = " + maxConnection);
			System.out.println("waiting for clients to connect...");
			
			while (true) {
				sock = server.accept();
				if (sock != null) {
					multiConnection newConn = new multiConnection(sock, portNumb);
					newConn.start();
				}
			} // end of while
		} catch (Exception e) {
			System.out.println("Error occurred when running server");
		} // end of try block
	} // end of main
}
