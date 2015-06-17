package edu.tamu.ecen424;

import java.net.*;
import java.io.*;
import java.util.*;

public class Client {
	public static void main(String[] args) {
		String ServerIP;
		int portNumb = 2013;
		System.out.print("Enter server IP address: ");
		Scanner keyBoard = new Scanner(System.in);
		ServerIP = keyBoard.next();
		setup(ServerIP, portNumb);
		keyBoard.close();
	}

	private static void setup(String IP, int port) {
		try {
			Socket sock = new Socket(IP, port);
			Send outgoing = new Send(sock);
			outgoing.start();
			//Receive incoming = new Receive(sock, IP, port);
			//incoming.start();
			System.out.println("Connection to " + IP + " @ "+ port +" is ready");
			//incoming.join();
			outgoing.join();
			sock.close();
		} catch (Exception e) {
			System.out.println("Error occurred during setup");
		} // end of catch block
	} // end of setup
}
