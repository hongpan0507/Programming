import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
//import java.util.Scanner;

public class server extends JFrame {
	private JTextField userText;	//the area to type in message before sending
	private JTextArea chatWindow;	//the area that displays the conversation
	private ObjectOutputStream output;
	//private DataInputStream input;	//??????????
	private ObjectInputStream input;
	private ServerSocket server;
	private Socket connection;
	private int PortNumber = 2013;
	private int MaxNum = 100;
	
	//constructor
	public server() {
		super("Instant Messager - server"); //display the title
		userText = new JTextField();
		userText.setEditable(false);	// if not connected to anyone, will not be able to type anything
		userText.addActionListener(
			new ActionListener() {
				public void actionPerformed(ActionEvent event) {
					sendMessage(event.getActionCommand());
					userText.setText("");	//reset user text window to blank
				}	//end of actionPerformed
			}	//end of ActionListener
		);	//end of addActionListener
		add(userText, BorderLayout.NORTH);
		chatWindow = new JTextArea();
		add(new JScrollPane(chatWindow));
		setSize(300,300);
		setVisible(true);
	}	//end of public server
	
	//set up and run the server
	public void runServer() {
		try {
			server = new ServerSocket(PortNumber, MaxNum);	//create a server socket: port=2013, max number: 100
			while(true){
				try{
					waitingConnection();
					streamSetup();
					chatting();
				}catch(EOFException IOEnd){
					showMessage("\n connection ended by server");
				}finally{
					cleanUp();
				}	// end of finally				
			}	//end of while
		}catch(IOException IOError){
			IOError.printStackTrace();
		}	//end of catch
	}	//end of public void runServer
	
	//waitConnnection()
	private void waitingConnection() throws IOException{
		showMessage("Waiting for connection...\n");
		connection = server.accept(); //create a socket when connected
		showMessage(connection.getInetAddress().getHostName() + " connected...");
	}	//end of waitConnection()
	
	//streamSetup()
	private void streamSetup() throws IOException{
		output = new ObjectOutputStream(connection.getOutputStream());
		output.flush();	//pushing all the bytes through
		input = new ObjectInputStream(connection.getInputStream());
		showMessage("\nStream is set up...");
	}	//end of streamSetup
	
	//chatting()
	private void chatting() throws IOException{
		String message = "\nConnection is ready...";
		showMessage(message);
		ableToType(true);
		do{
			try{
				message = (String) input.readObject();
				showMessage("\n" + message);
			}catch(ClassNotFoundException notFound){
				showMessage("\ninvalid message send from the user");
			}
		} while(!message.equals("Client: END"));
	}	//eof private void chatting
	
	//cleanUp()
	private void cleanUp(){
		showMessage("\n Connection terminated \n");
		ableToType(false);
		try{
			output.close();
			input.close();
			connection.close();
		}catch(IOException IOError){
			IOError.printStackTrace();
		}
	}	//eof cleanUp
	
	//sendMessage()
	private void sendMessage(String message){
		try{
			output.writeObject("Sever: " + message);
			output.flush();
			showMessage("\nServer: " + message);
		}catch(IOException IOError){
			chatWindow.append("\n Error: message is not sent");
		}	//end of catch
	}	//eof sendMessage
	
	//showMessage()
	private void showMessage(final String text){	//final??????????????????
		SwingUtilities.invokeLater(
				new Runnable(){
					public void run(){
						chatWindow.append(text);
					}	//eof run
				}	//eof Runnable
		); //eof invokeLater
	}	//eof showMessage
	
	//ableToType()
	private void ableToType(final boolean tof){
		SwingUtilities.invokeLater(
				new Runnable(){
					public void run(){
						userText.setEditable(tof);
					}	//eof run
				}	//eof Runnable
		); //eof invokeLater
	}	//eof ableToType
}	//end of class server
