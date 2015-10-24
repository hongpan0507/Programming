import java.io.*;
import java.net.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class arduinoClient extends JFrame {
	private JTextField outText;
	private JTextArea outWindow;
	private Socket connection;
	private DataInputStream input;
	private DataOutputStream output;
	private String serverIP = "192.168.1.177";
	private int portNumber = 2013;
	private String frequency;

	// constructor
	public arduinoClient() {
		super("autoTuner");
		outText = new JTextField();
		outText.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				sendMsg(event.getActionCommand());
				outText.setText(""); // reset user text window to blank
			}
		});//end of action listener
		add(outText, BorderLayout.SOUTH);
		outWindow = new JTextArea();
		add(new JScrollPane(outWindow));
		setSize(300, 600);
		setVisible(true);
	}// end of constructor
	
	public void run(){
		waitConnection();
		streamSetup();
		receiveMsg();
	}//end of run()
	
	public void waitConnection() {
		try {
			System.out.println("waiting for connection...");
			connection = new Socket(InetAddress.getByName(serverIP), portNumber);
			System.out.println("Connection from: "
					+ connection.getInetAddress().getHostAddress());
			streamSetup();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}// end of waitConnection()

	private void streamSetup() {
		try {
			input = new DataInputStream(connection.getInputStream());
			output = new DataOutputStream(connection.getOutputStream());
		} catch (IOException e) {
			e.printStackTrace();
		}// end of catch
		System.out.println("Connection is ready!");
	}// end of streamSetup()

	public void receiveMsg() {
		try {
			while(true){
			frequency = input.readLine();
			String freqStr = new String("\n" + frequency);
			showMessage(freqStr);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}// end of receiveMsg()

	public void sendMsg (String message) {
				try {
					output.writeBytes(message);
					output.flush();
				} catch (IOException e) {
					e.printStackTrace();
				}
				showMessage("\nPC: " + message);
	}// end of sendMsg

	private void showMessage(final String text){
		SwingUtilities.invokeLater(
				new Runnable(){
					public void run(){
						outWindow.append(text);
					}	//eof run
				}	//eof Runnable
		); //eof invokeLater
	}	//eof showMessage
	
	public void cleanUp() {
		try {
			output.close();
			connection.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}// end of arduinoClient
