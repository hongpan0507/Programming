package edu.tamu.ecen424;

import java.io.*;
import java.util.Scanner;

public class Send extends Thread {
	private ObjectOutputStream oStream;
	private String message = "";
	
	public Send(ObjectOutputStream Stream) {
		oStream = Stream;
	} // end of constructor

	public void run() {
		try {
			Scanner keyboard = new Scanner(System.in);
			while (message != "\\disconnect") {
				message = keyboard.nextLine();
				oStream.writeObject(message);
				oStream.flush();
			} // end of while
			System.out.println("The client has been disconnected");
			keyboard.close();
			oStream.close();
		} catch (IOException e) {
			System.out.println("Error occurred when sending message" + e);
		} // end of try block
	} // end of run
}
