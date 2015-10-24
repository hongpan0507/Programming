package edu.tamu.ecen424;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Send extends Thread {
	private ObjectOutputStream oStream;
	private Socket sock;
	private String message = "";
	
	public Send(Socket socket) throws IOException {
		sock = socket;
		oStream = new ObjectOutputStream(sock.getOutputStream());
		oStream.flush();
	} // end of constructor

	public void run() {
		try {
			Scanner keyboard = new Scanner(System.in);
			while (message != "\\disconnect") {
				message = keyboard.nextLine();
				oStream.writeObject(message);
			} // end of while
			System.out.println("The server has been disconnected");
			keyboard.close();
			oStream.close();
		} catch (IOException e) {
			System.out.println("Error occurred when sending message" + e);
		} // end of try block
	} // end of run
}
