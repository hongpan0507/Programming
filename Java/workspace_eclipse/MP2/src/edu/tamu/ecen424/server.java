package edu.tamu.ecen424;

import java.io.BufferedReader;
//import java.util.Scanner;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;
 
public class server {
    public static void main(String[] args) throws IOException {
 
  
        int newsocket = Integer.parseInt(args[0]);
        int clientnum = Integer.parseInt(args[1]);
        int clientcount = 0;
        Thread[] thrd = new Thread[clientnum];
        try {
            ServerSocket serverSocket = new ServerSocket(newsocket);
            System.out.println("new socket has been opened.");
            while(clientcount < clientnum)
            {
            	System.out.println("Waiting for client...");
            	Socket clientSocket = serverSocket.accept();
            	System.out.println("Client has connected.");
            	thrd[clientcount] = new Thread(new ClientHandler2(clientSocket));
            	thrd[clientcount].start();
            	clientcount = clientcount + 1;
            	System.out.println("Number of clients connected: " + clientcount);
            }
            while(clientnum > 0){
            	thrd[clientnum].join();
            	clientnum = clientnum-1;
            }
            serverSocket.close();
            System.out.println("Server has been exited.");
        } 
        catch (IOException e) {
            System.err.println("Could not listen on port.");
            System.exit(1);
        }
        catch (InterruptedException e) {};
    }
}

class ClientHandler2 implements Runnable {
	Socket socket;
	PrintWriter out;
	String inputLine = " ";
	String blanks;
	String oldblanks;
	char guess;
	int count = 0;
	String endmessage;

	ClientHandler2(Socket s) {
		socket = s;
	}

	@Override
	public void run() {
	
		try {
			out = new PrintWriter(socket.getOutputStream(), true);
			Scanner message_input = new Scanner(System.in);
			System.out.println("Write a message.");
            String message = message_input.next();
			System.out.println(message);

			//String message = "Salutations.";
            System.out.println("Sending message to player.");
            
            blanks = ClientHandler2.getblanks(message);
            System.out.println(blanks);
            
            out.println(blanks);
            System.out.println("Message has been sent.");
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            while(count < 6 && !blanks.equals(message)) 
            {
            	inputLine = new String(in.readLine());
            	guess = inputLine.charAt(0);
            	oldblanks = blanks;
            	blanks = ClientHandler2.msgcheck(message, blanks, guess);
            	System.out.println(blanks);
            	if (blanks.equals(oldblanks)) {
            		count = count+1;
            	}
            	System.out.println("Player guessed: " + inputLine);
            	System.out.println("Current count is: " + count);
            	out.println(blanks);
            }   
            if (blanks.equals(message)) {
            	endmessage = "Yay, you won c:";
            }
            else {
            	endmessage = "Sorry, you lost :c";
            }
            out.println(endmessage);
            
            in.close();
            out.close();
            socket.close();   
            System.out.println("Socket has been closed.");
            
		} catch (IOException e) {
			System.out.println("PrintStream Error");
		}
	}
	
    public static String msgcheck(String message, String blankmsg, char guess) {
    	//algorithm to check for matches stored in updatestg
    	char[] charArray = message.toCharArray();
    	char[] blnkArray = blankmsg.toCharArray();
    	int stgsize = message.length();
    	
    	for (int i = 0; i < stgsize; i++){
    		//check for matches
    		if(Character.toString(charArray[i]).equals(Character.toString(guess))){
    			blnkArray[i] = charArray[i];
    		}
    		else {
    		}
    	}
    	String updatestg = new String(blnkArray);
    	return updatestg;
    }
    
    public static String getblanks(String message) {
    	int stgsize;
    	char[] charArray = message.toCharArray();
    	char[] blnkArray = message.toCharArray();
    	stgsize = message.length();
    	for (int i = 0; i < stgsize; i++){
    		//check to see if it's punctuation
    		if (Character.toString(charArray[i]).equals(".") || Character.toString(charArray[i]).equals(",") || Character.toString(charArray[i]).equals("'") || Character.toString(charArray[i]).equals("?") || Character.toString(charArray[i]).equals(" ")) {
    			blnkArray[i] = charArray[i];
    		}
    		else {
    			String oneBlank = "-";
    			blnkArray[i] = oneBlank.charAt(0);
    		}
    	}
    	String blanks = new String(blnkArray);
    	return blanks;
    }
}