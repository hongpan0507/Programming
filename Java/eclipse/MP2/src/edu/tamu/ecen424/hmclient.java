package edu.tamu.ecen424;

import java.io.*;

import java.net.*;

import java.util.Scanner;

 

public class hmclient {

    public static void main(String[] args) throws IOException {

        

    String status = "blah";

    Socket socket;

        int newsocket = Integer.parseInt(args[0]);

        String hostname = args[1];

        try {

            socket = new Socket(hostname, newsocket);

            System.out.println("Connected to server.");

            BufferedReader fromServer = null; 

            fromServer = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            System.out.println("Waiting for message from server.");

            String message = fromServer.readLine();

            System.out.println("Recieved message from server.");

            System.out.println("Server: " + message);    

            Scanner status_input = new Scanner(System.in);

            PrintWriter toServer = null;

            String oldmsg = message;

            int count = 0;

            while(!message.equals("Sorry, you lost :c") && !message.equals("Yay, you won c:")) {

            System.out.println("Guess a letter.");

            status = status_input.next();

            toServer = new PrintWriter(socket.getOutputStream(), true);

            toServer.println(status);

            System.out.println("Guess sent.");

            message = fromServer.readLine();

                System.out.println("Status update: " + message);

                //if no change in message (i.e. incorrect guess), update count

                if(oldmsg.equals(message)) {

                count = count + 1;

                }

                //if message is complete, grab end message

                if (hmclient.checkComp(message) == 0 || count == 6) {

                message = fromServer.readLine();

                }

                oldmsg = message;

            }

            System.out.println(message);

            fromServer.close();

            socket.close();

        } 

        catch (UnknownHostException e) {

            System.err.println("Don't know about host: localhost.");

            System.exit(1);

        } catch (IOException e) {

            System.err.println("Couldn't get I/O for the connection to: localhost.");

            System.exit(1);

        }

    }

    public static int checkComp (String message) {

    char[] charArray = message.toCharArray();

    int stgsize = message.length();

    int msgCheck = 0;

    for (int i = 0; i < stgsize; i++){

    //check to see if it's punctuation

    if (Character.toString(charArray[i]).equals("-")) {

    msgCheck = msgCheck + 1;

    }

    else {

    msgCheck = msgCheck + 0;

    }

    }

    return msgCheck;

    }

}