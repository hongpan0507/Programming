package edu.tamu.ecen424.MP6_UDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPServer {
	public static void main(String[] args) throws Exception {
		int ServerPort = 2013;
		int ClientPort = 0;
		String ReceiveMessage = "none";
		String SendMessage = "none";
		String permission = "2013";
		String password = "2013";
		String pw_ack = "%Granted%";
		InetAddress ClientIP = null;
		Scanner keyboard2 = new Scanner(System.in);
		byte[] IncomingData = new byte [20];
		byte[] OutgoingData = new byte [20]; // In Java, 1 char = 2 bytes
		int MaxSize = 10;	//number of characters in one outgoing packet
		
		DatagramSocket ServerSocket = new DatagramSocket(ServerPort);
		DatagramPacket incomingDP;
		DatagramPacket outgoingDP;
		
		String serverIP = InetAddress.getLocalHost().getHostAddress();
		System.out.println("Server IP: " + serverIP);
		System.out.println("Waiting for incoming connection...");
		incomingDP = new DatagramPacket(IncomingData, IncomingData.length);

		while(true){
			try{
				
				ServerSocket.receive(incomingDP);
				
				//permission = new String(incomingDP.getData());
				//System.out.println(permission);
				//permission = new String(incomingDP.getData(),0,0,incomingDP.getLength());
				ClientIP = incomingDP.getAddress();
				ClientPort = incomingDP.getPort();
				if(permission.equals(password)){
					System.out.println(ClientIP + " is connected");
					//OutgoingData = pw_ack.getBytes();
					//outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,ClientPort);
					//ServerSocket.send(outgoingDP);
					
					
					System.out.println("Type in message and hit Enter to send");
					while(!SendMessage.equals("%abort")){
						//if(ServerSocket.isConnected()) System.out.println("++++++");
						SendMessage = keyboard2.nextLine();
						int len = SendMessage.length();
						int packet_numb = (int) Math.ceil((double)len/(double)MaxSize);
						System.out.println("packet number: " + packet_numb);
						String payload_numb = Integer.toString(packet_numb);
						OutgoingData = payload_numb.getBytes();
						outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,ClientPort);
						ServerSocket.send(outgoingDP);
						String temp = null;
						
						if( len <= MaxSize){
							OutgoingData = SendMessage.getBytes();
							outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,ClientPort);
							ServerSocket.send(outgoingDP);
						} else {
							for(int i = 0; i < len; i = i + MaxSize){
								if((len - i) <= MaxSize){
									temp = SendMessage.substring(i, len);
								} else {
									temp = SendMessage.substring(i, i+MaxSize-1);
								}
								OutgoingData = temp.getBytes();
								outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,ClientPort);
								ServerSocket.send(outgoingDP);
								ServerSocket.receive(incomingDP);
								ReceiveMessage = new String(incomingDP.getData(),0,0,incomingDP.getLength());
								System.out.println("Packet "+ReceiveMessage+" sent successfully");
							}	//end of for
						}	//end of else
					}	//end of while
					SendMessage = "none";
					System.out.println("Disconnected from " + ClientIP);
				} else {
					System.out.println(ClientIP+" attempted to connect with wrong pw:" + permission);
					OutgoingData = "wrong_pw".getBytes();
					outgoingDP = new DatagramPacket(OutgoingData,OutgoingData.length,ClientIP,ClientPort);
					ServerSocket.send(outgoingDP);
					}	//end of else
			} catch(IOException e) {
				System.err.println(e);
			}
		}	//end of while
	}	//end of main
}
