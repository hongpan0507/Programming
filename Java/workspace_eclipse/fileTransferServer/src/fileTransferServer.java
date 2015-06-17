import java.net.*;
import java.io.*;

public class fileTransferServer {
	private ServerSocket server;
	private Socket connection;
	private int PortNumber = 2013;
	private int MaxClient = 100;
	private InputStream inStream;
	private OutputStream outStream;
	private DataInputStream diStream;
	private byte[] buffer = new byte[1024];
	private String fileName;
	private long fileSize;
	private long fixedSize;
	private final int ToMB = 1048576;
	//constructor
	public fileTransferServer(){
		
	}//end of constructor
	
	//run the server for file transfer
	public void runServer(){
		try{
			server = new ServerSocket(PortNumber, MaxClient);
			while(true){
				waitingConnection();
				streamSetup();
				fileTransfer();
			}//end of while
		}catch(IOException io){
			io.printStackTrace();
		}finally{
			cleanUp();
		}//end of finally	
	}//end of runServer		
	
	//set up socket 
	private void waitingConnection() throws IOException{
		System.out.println("waiting for connection...\n");
		connection = server.accept();
		System.out.println(connection.getInetAddress().getHostName() + " connected!");
	}//end of waitingConnection()

	//set up stream
	private void streamSetup() throws IOException{
		inStream = connection.getInputStream();
		diStream = new DataInputStream(inStream);
		fileName = diStream.readUTF();
		outStream = new FileOutputStream("C:/Users/hp/Desktop/received/" + fileName);		
	}//end of streamSetup()
	
	//file transfer
	private void fileTransfer() {
		Thread receiveFile = new Thread() {
			public void run() {
				try {
					int count = 0;
					fileSize = diStream.readLong();
					
					fixedSize = fileSize / ToMB;
					while (fileSize > 0 && (count = diStream.read(buffer, 0, (int)Math.min(buffer.length, fileSize))) != -1) {
						outStream.write(buffer, 0, count);
						fileSize -= count;
					}
					outStream.close();
					System.out.println("File Name: " + fileName);
					System.out.println("File Size: " + fixedSize + "MB");
					System.out.println("Received!");
				} catch (IOException e) {
					e.printStackTrace();
				}//end of catch
			}// end of run()
		};// end of readRunnable
		receiveFile.start(); // start the thread
	}// end of fileTransfer
	
	
	private void cleanUp(){
		try{
			inStream.close();
			diStream.close();
			connection.close();
		}catch(IOException e){
			e.printStackTrace();
		}//end of catch
	}//end of cleanUp
}//end of fileTransferServer
