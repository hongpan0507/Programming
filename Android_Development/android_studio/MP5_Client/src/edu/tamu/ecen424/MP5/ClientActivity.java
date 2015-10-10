package edu.tamu.ecen424.MP5;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class ClientActivity extends Activity {
	
	Socket socket;
	Handler updateConversationHandler;
	Thread clientThread = null;

	int port = 2013;
	static String serverIP = "192.168.0.100";
	static String RecMessage = null;
	static String SendMessage = null;
	static boolean send_bool = false;
	static String TAG = "ServerActivity";
	static String temp = null;
	
	public EditText edit;
	public TextView ReceivedText;
	public TextView SentText;
	public TextView client_startup;
	public TextView client_connection;
	public TextView portNumb;
	public TextView IP;
		
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_client);
		
		edit = (EditText) findViewById(R.id.editText1);
		ReceivedText = (TextView) findViewById(R.id.rec_message);
		SentText = (TextView) findViewById(R.id.sent_message);
		client_startup = (TextView) findViewById(R.id.startupID);
		client_connection = (TextView) findViewById(R.id.connectionID);
		IP = (TextView) findViewById(R.id.serverIP);
		portNumb = (TextView) findViewById(R.id.port);
		
		findViewById(R.id.return_button).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v1) {
				finish();	//finish activity and go back to the main menu
			}
		});
		findViewById(R.id.clear_butt).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v2) {
				ReceivedText.setText("");
				SentText.setText("");
			}
		});
		findViewById(R.id.send_butt).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v3) {
				SendMessage = edit.getText().toString();
				SentText.setText(SentText.getText().toString() + SendMessage+ "\n");
				send_bool = true;
			}
		});
		
		Intent intent = getIntent();
		Bundle extras = intent.getExtras();
		port = extras.getInt("portNumb");
		serverIP = extras.getString("IP_Address");
		
		updateConversationHandler = new Handler();
		this.clientThread = new Thread(new ClientThread());
		this.clientThread.start();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.client, menu);
		return true;
	}
	
	public void cheat(int k){
		switch(k){
			case 0:
				client_startup.setText("Client is running...");
				break;
			case 1:
				portNumb.setText("Port Number: " + port);
				break;
			case 2:
				IP.setText("Server IP Address: " + serverIP);
				break;
			case 3:
				client_connection.setText(serverIP + "is connected");
				break;
			//more cases goes here
			default: //optional
		}
	}
	
	public void onStop(){
		super.onStop();
		try{
			socket.close();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}	//end of onStop()
	
	public class ClientThread implements Runnable{
		@Override
		public void run() {
			try{
				socket = new Socket(serverIP, port);
				if(socket != null){
					cheat(0);
					cheat(1);
					cheat(2);
					serverIP = socket.getInetAddress().getHostName();
				    SendThread send = new SendThread(socket);
				    new Thread(send).start();
				    ReceiveThread receive = new ReceiveThread(socket);
				    new Thread(receive).start();
				}
			} catch(IOException e) {
				e.printStackTrace();
			} //end of try catch
		}	//end of run
	}	//end of server thread
	
	public class SendThread implements Runnable{
		private Socket clientSocket;
		private ObjectOutputStream outgoing;
		//constructor
		public SendThread(Socket clientSock){
			this.clientSocket = clientSock;
			try {
				outgoing = new ObjectOutputStream(new BufferedOutputStream(this.clientSocket.getOutputStream()));
				outgoing.flush();
			} catch(IOException e) {
				e.printStackTrace();
			}
		}//end of constructor
		
		@Override
		public void run() {
			while(!Thread.currentThread().isInterrupted()) {
				try{
					if(send_bool == true){
						outgoing.writeObject(SendMessage);
						outgoing.flush();
						send_bool = false;
					}
					//updateConversationHandler.post(new updateUIThread(message));
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
		}	//end of run
	}	//end of ReceiveThread
		
	public class ReceiveThread implements Runnable{
		private Socket clientSocket;
		private ObjectInputStream incoming;
		//constructor
		public ReceiveThread(Socket clientSock){
			this.clientSocket = clientSock;
			try {
				incoming = new ObjectInputStream(new BufferedInputStream(this.clientSocket.getInputStream()));
			} catch(IOException e) {
				e.printStackTrace();
			}
		}//end of constructor
		
		@Override
		public void run() {
			while(!Thread.currentThread().isInterrupted()) {
				try{
					RecMessage = (String)incoming.readObject();
					updateConversationHandler.post(new updateUIThread(RecMessage));
				} catch(IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}	//end of run
	}	//end of ReceiveThread
	
	public class updateUIThread implements Runnable{
		private String message;
		public updateUIThread(String mess){
			this.message = mess;
		}
		@Override
		public void run() {
			cheat(3);
			ReceivedText.setText(ReceivedText.getText().toString()+serverIP+": "+message+"\n");
		}
	}//end of updateUIThread
}
