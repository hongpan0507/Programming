import java.io.*;
import java.net.*;
import java.awt.*;	//Contains all of the classes for creating user interfaces and for painting graphics and images
import java.awt.event.*;	//Provides interfaces and classes for dealing with different types of events fired by AWT components. 
import javax.swing.*;

public class client extends JFrame{
	private JTextField userText;
	private JTextArea chatWindow;
	private ObjectOutputStream output;
	private ObjectInputStream input;
	private Socket connection;
	private String serverIP;
	private int PortNumber = 2013;
	
	//constructor
	public client(String host){
		super("Instant Messager - client");
		serverIP = host;
		userText = new JTextField();
		userText.setEditable(false);
		userText.addActionListener(
			new ActionListener(){
				public void actionPerformed(ActionEvent event){
					sendMessage(event.getActionCommand());
					userText.setText("");
				}//end of actionPerformed
			}	//end of ActionListerner 
		); // end of addActionListener
		add(userText, BorderLayout.NORTH);
		chatWindow = new JTextArea();
		add(new JScrollPane(chatWindow), BorderLayout.CENTER);
		setSize(300, 300);
		setVisible(true);
	} // end of constructor
	
	//connect to server
	public void runClient(){
		try{
			waitingConnection();
			streamSetup();
			chatting();
		}catch(EOFException eofError){
			showMessage("\n connection terminated by client");
		}catch(IOException IOError){
			IOError.printStackTrace();
		}finally{
			cleanUp();
		}//end of finally		
	}//end of runClient
	
	//waitingConnection()
	private void waitingConnection() throws IOException{
		showMessage("Waiting for connection...\n");
		connection = new Socket(InetAddress.getByName(serverIP), PortNumber);
		showMessage(connection.getInetAddress().getHostName() + " connected...");
	} //end of waitingConnection
	
	//streamSetup()
	private void streamSetup() throws IOException{
		output = new ObjectOutputStream(connection.getOutputStream());
		output.flush();
		input = new ObjectInputStream(connection.getInputStream());
		showMessage("\nStream is set up...");
	}//end of streamSetup
	
	//chatting()
	private void chatting() throws IOException{
		String message = "\nConnection is ready...";
		showMessage(message);
		ableToType(true);
		do{
			try{
				message = (String) input.readObject();	//reading input from the server
				showMessage("\n" + message);
			}catch(ClassNotFoundException notFound){
				showMessage("\ninvalid message from the server");
			}
		}while(!message.equals("Server: END"));
	}//end of chatting
	
	//cleanUp
	private void cleanUp() {
		showMessage("\n Connection terminated \n");
		ableToType(false);
		try{
			output.close();
			input.close();
			connection.close();
		}catch(IOException IOError){
			IOError.printStackTrace();
		}
	}	//end of cleanUp
	
	//sendMessage()
	private void sendMessage(String message){
		try{
			output.writeObject(message);
			output.flush();
			showMessage("\nClient: " + message);
		}catch(IOException IOError){
			chatWindow.append("\n Error: message is not sent");
		}
	}//end of sendMessage
	
	//showMessage()
	private void showMessage(final String text){
		SwingUtilities.invokeLater(
				new Runnable(){
					public void run(){
						chatWindow.append(text);
					}
				}
		);
	}//end of showMessage
	
	//ableToType()
	private void ableToType(final boolean tof){
		SwingUtilities.invokeLater(
				new Runnable(){
					public void run(){
						userText.setEditable(tof);
					}
				}
		);
	}//end of ableToType
} //end of class client