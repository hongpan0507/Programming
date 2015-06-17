package edu.tamu.ecen424.MP5;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;

import android.app.Activity;
import android.content.Intent;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class ServerActivity extends Activity {
	ServerSocket serverSocket;
	Socket socket;
	Handler updateConversationHandler;
	Thread serverThread = null;

	int port = 2013;
	int maxClient = 10;
	
	public EditText edit;
	public TextView ReceivedText;
	public TextView SentText;
	public TextView server_startup;
	public TextView client_connection;
	public TextView portNumb;
	public TextView maxConnection;
	static String TAG = "ServerActivity";
	static InetAddress ClientIP = null;
	static String ServerIP = null;
	static String RecMessage = null;
	static String SendMessage = "";
	static boolean send_bool = false;
	String IP_temp = null;
	String temp = null;
	
	static int ServerPort = 2013;
	static String permission = "2013";
	static String password = "2013";
	static String pw_ack = "%Granted%";
	
	byte[] IncomingData = new byte [20];
	byte[] OutgoingData = new byte [20]; // In Java, 1 char = 2 bytes
	int MaxSize = 10;	//number of characters in one outgoing packet
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_server);
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
		maxClient = extras.getInt("maxClient");
		
		WifiManager wifi = (WifiManager) getSystemService(WIFI_SERVICE);
		WifiInfo info = wifi.getConnectionInfo();
		int IP = info.getIpAddress();
		ServerIP = String.format(
				   "%d.%d.%d.%d",
				   (IP & 0xff),
				   (IP >> 8 & 0xff),	//shift first, then bit wise and
				   (IP >> 16 & 0xff),
				   (IP >> 24 & 0xff));
		Log.d(TAG,ServerIP);
		edit = (EditText) findViewById(R.id.editText1);
		ReceivedText = (TextView) findViewById(R.id.rec_message);
		SentText = (TextView) findViewById(R.id.sent_message);
		server_startup = (TextView) findViewById(R.id.startupID);
		client_connection = (TextView) findViewById(R.id.connectionID);
		maxConnection = (TextView) findViewById(R.id.max);
		portNumb = (TextView) findViewById(R.id.port);
		
		updateConversationHandler = new Handler();
		this.serverThread = new Thread(new ServerThread());
		this.serverThread.start();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.server, menu);
		return true;
	}
	
	public void cheat(int k){
		switch(k){
			case 0:
				server_startup.setText("Server @ "+ ServerIP);
				break;
			case 1:
				portNumb.setText("Port Number: " + port);
				break;
			case 2:
				maxConnection.setText("Max Clients allowed: " + maxClient);
				break;
			case 3:
				client_connection.setText(ClientIP + "is connected");
				break;
			//more cases goes here
			default: //optional
		}
	}
	
	public void onStop(){
		super.onStop();
		try{
			serverSocket.close();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}	//end of onStop()
	
	public class ServerThread implements Runnable{
		@Override
		public void run() {
			try{
				DatagramSocket ServerSocket = new DatagramSocket(ServerPort);
				DatagramPacket incomingDP;
				DatagramPacket outgoingDP;
				incomingDP = new DatagramPacket(IncomingData, IncomingData.length);
				cheat(0);
				cheat(1);
				cheat(2);
				while(true){
					ServerSocket.receive(incomingDP);
					permission = new String(incomingDP.getData(),0,0,incomingDP.getLength());
					ClientIP = incomingDP.getAddress();
					port = incomingDP.getPort();
					
					if(permission.equals(password)){
						System.out.println(ClientIP + " is connected");
						OutgoingData = pw_ack.getBytes();
						outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,port);
						ServerSocket.send(outgoingDP);
						
						while(!SendMessage.equals("%abort")){
							if(send_bool == true){
								int len = SendMessage.length();
								
								int packet_numb = (int) Math.ceil((double)len/(double)MaxSize);
								System.out.println("packet number: " + packet_numb);
								String payload_numb = Integer.toString(packet_numb);
								OutgoingData = payload_numb.getBytes();
								outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,port);
								ServerSocket.send(outgoingDP);
							
								if( len <= MaxSize){
									OutgoingData = SendMessage.getBytes();
									outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,port);
									ServerSocket.send(outgoingDP);
								} else {
									for(int i = 0; i < len; i = i + MaxSize){
										if((len - i) <= MaxSize){
											temp = SendMessage.substring(i, len);
										} else {
											temp = SendMessage.substring(i, i+MaxSize-1);
										}
										OutgoingData = temp.getBytes();
										outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,port);
										ServerSocket.send(outgoingDP);
										ServerSocket.receive(incomingDP);
										RecMessage = new String(incomingDP.getData(),0,0,incomingDP.getLength());
										RecMessage = "Packet "+RecMessage+" sent successfully";
										updateConversationHandler.post(new updateUIThread(RecMessage));
									}	//end of for
								}	//end of else								
								send_bool = false;
							}
						} 
						
					} else {
						OutgoingData = "wrong_pw".getBytes();
						outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,port);
						ServerSocket.send(outgoingDP);
						}	//end of else 
				}
			} catch(IOException e) {
				e.printStackTrace();
			} //end of try catch
		}
	}	//end of server thread
	
	public class updateUIThread implements Runnable{
		private String message;
		public updateUIThread(String mess){
			this.message = mess;
		}
		@Override
		public void run() {
			cheat(3);
			ReceivedText.setText(ReceivedText.getText().toString()+message+"\n");
		}
	}//end of updateUIThread
}

