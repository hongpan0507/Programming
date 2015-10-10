import java.net.*;
import java.io.*;

public class fileTransferClient {
	private OutputStream outStream = null;
	private FileInputStream fiStream = null;
	private BufferedInputStream biStream = null;
	private DataInputStream diStream = null;
	private DataOutputStream doStream = null;
	private Socket connection = null;
	private int PortNumber = 2013;
	private File currentFile = null;
	private byte[] buffer = null;
	private final int ToMB = 1048576;

	// constructor
	public fileTransferClient() {

	}// end of constructor

	public void runClient(String serverIP, String filePath) {
		try {
			currentFile = new File(filePath);
			waitingConnection(serverIP);
			streamSetup();
			fileTransfer();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			cleanUp();
		}// end of finally
	}// end of runClient

	// setup socket
	private void waitingConnection(String serverIP) throws IOException {
		connection = new Socket(InetAddress.getByName(serverIP), PortNumber);
		System.out.println(connection.getInetAddress().getHostName()
				+ " connected");
	}// end of waitingConnection

	// setup stream
	private void streamSetup() throws IOException {
		fiStream = new FileInputStream(currentFile);
		biStream = new BufferedInputStream(fiStream);
		diStream = new DataInputStream(biStream);
		outStream = connection.getOutputStream();
		doStream = new DataOutputStream(outStream);
	}// end of streamSetup

	// start file transfer
	private void fileTransfer() throws IOException {
		buffer = new byte[(int) currentFile.length()];
		diStream.readFully(buffer, 0, buffer.length);

		doStream.writeUTF(currentFile.getName());
		doStream.writeLong(buffer.length);
		
		doStream.write(buffer, 0, buffer.length);
		doStream.flush();
		System.out.println("File Name: " + currentFile.getName());
		System.out.println("File Size: " + currentFile.length() / ToMB
				+ "MB");
	}// end of fileTransfer

	private void cleanUp() {
		try {
			fiStream.close();
			biStream.close();
			diStream.close();
			outStream.close();
			doStream.close();
			connection.close();			
			System.out.println("transfer completed!");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}// end of cleanUp
}// end of fileTransferClient
