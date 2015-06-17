package edu.tamu.ecen424.MP6_UDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPClient {
	public static void main(String[] args) throws IOException {
		Scanner input =new Scanner(System.in);
		String SendMessage = "none";
		String ReceiveMessage = "none";
		String CompleteMessage = "";
		String permission = "connecting";
		String ack = "";
	    DatagramSocket ClientSocket = new DatagramSocket();
	    DatagramPacket OutgoingDP;
	    DatagramPacket IncomingDP;
	    InetAddress IPAddress = InetAddress.getByName("10.201.75.202");
	    int ServerPortNumb = 2013;
	    byte[] IncomingData = new byte[20];
	    byte[] OutgoingData = new byte[20];
	    
	    System.out.println("Connecting to " + IPAddress);
	    IncomingDP = new DatagramPacket(IncomingData, IncomingData.length);
	    
	    while(!(permission.equals("%Granted%"))){
	    	System.out.print("Password: ");
	    	SendMessage = input.nextLine();
	    	OutgoingData = SendMessage.getBytes();
	    	OutgoingDP = new DatagramPacket(OutgoingData, OutgoingData.length, IPAddress, ServerPortNumb);
	    	ClientSocket.send(OutgoingDP);
	    	ClientSocket.receive(IncomingDP);
	    	permission = new String(IncomingDP.getData(),0,0,IncomingDP.getLength());
	    	//permission = new String(IncomingDP.getData());
	    }	
	    
	    System.out.println("Connection established");
	    System.out.println("Waiting for server to send message");
	    
	    while(!ReceiveMessage.equals("%abort")){
	    	//if(ClientSocket.isConnected()) System.out.println("++++++");
	    	ClientSocket.receive(IncomingDP);
	    	ReceiveMessage = new String(IncomingDP.getData(),0,0,IncomingDP.getLength());
	    	int mess_numb = Integer.parseInt(ReceiveMessage);
	    	System.out.println("Server is about to send: "+mess_numb+" packets");
	    	for(int count = 0; count < mess_numb; count++){
	    		ack = Integer.toString(count);
	    		OutgoingData = ack.getBytes();
	    		OutgoingDP = new DatagramPacket(OutgoingData, OutgoingData.length, IPAddress, ServerPortNumb);
	    		ClientSocket.receive(IncomingDP);
	    		System.out.println("Packet "+count+" Received");
	    		ClientSocket.send(OutgoingDP);
	    		ReceiveMessage = new String(IncomingDP.getData(),0,0,IncomingDP.getLength());
	    		CompleteMessage = CompleteMessage + ReceiveMessage;
	    	}
	    	System.out.println(IPAddress + ": " + CompleteMessage);
	    	CompleteMessage = "";
	    }
	    ReceiveMessage = "none";
	    ClientSocket.close();
	    System.out.println("Disconnected from server");	     
	}
}
