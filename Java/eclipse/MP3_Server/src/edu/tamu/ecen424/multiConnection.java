package edu.tamu.ecen424;

import java.net.*;
import java.io.*;

public class multiConnection extends Thread {
	private Socket sock;
	private String ClientIP = "";
	private int portNumb = 0;

	public multiConnection(Socket serv_sock, int port) {
		sock = serv_sock;
		portNumb = port;
	}

	public void run() {
		try {
			ClientIP = sock.getInetAddress().getHostName();
			System.out.println(ClientIP + " Connected");
			ObjectOutputStream oStream = new ObjectOutputStream(sock.getOutputStream());
			oStream.flush();
			ObjectInputStream iStream = new ObjectInputStream(sock.getInputStream());
			System.out.println("Connection to " + ClientIP + " is ready");
			System.out.println("Type in messages, and hit enter to send");
			Receive incoming = new Receive(iStream, ClientIP, portNumb);
			Send outgoing = new Send(oStream);
			incoming.start();
			outgoing.start();
			incoming.join();
			outgoing.join();
			iStream.close();
			oStream.close();
			sock.close();
		} catch (IOException e1) {
			System.out.println("Error occurred when using multiClient" + e1);
		} catch (Exception e2){
			System.out.println("Error occurred when threads join" + e2);
		} // end of try block
	} // end of run
}
