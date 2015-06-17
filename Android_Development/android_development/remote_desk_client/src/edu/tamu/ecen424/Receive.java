package edu.tamu.ecen424;

import java.io.*;
import java.net.Socket;

public class Receive extends Thread{
	// input stream
	private DataInputStream diStream = null;
	// output stream
	private FileOutputStream foStream = null;

	private byte[] buffer = new byte[1024];
	private String imageName = "1.PNG";
	private long imageSize = 0;
	private int SizeCount = 0;
	private int Count = 0;
	private Socket sock;
	private String ServerIP = "";
	
	public Receive(Socket socket) throws IOException {
		sock = socket;	
	}

	public void run() {
		try {
			diStream = new DataInputStream(sock.getInputStream());
			ServerIP = sock.getInetAddress().getHostName();
			System.out.println(ServerIP + " Connected");
			System.out.println("Connection to " + ServerIP + " is ready");

			while (true) {
				imageName = diStream.readUTF();
				foStream = new FileOutputStream("C:/Users/hp/Desktop/received/"
						+ imageName);
				imageSize = diStream.readLong();

				// receiving image
				while (imageSize > 0
						&& (SizeCount = diStream.read(buffer, 0,
								(int) Math.min(buffer.length, imageSize))) != -1) {
					foStream.write(buffer, 0, SizeCount);
					imageSize -= SizeCount;
				}
				++Count;
				System.out.println(imageName + "Received");
				if (Count > 10) {
					break;
				}
			}
			foStream.close();
			sock.close();
		} catch (Exception e1) {
			e1.printStackTrace();
		} // end of try block
	} // end of run
}
