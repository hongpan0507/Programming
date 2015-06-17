package edu.tamu.ecen424;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

public class moveMouse extends Thread {
	public static int xCoord = 1366/2;
	public static int yCoord = 768/2;
	public static int move = 0;
	private Socket sock;
	private ObjectInputStream iStream = null;
	public static int xMin = 50;
	public static int yMin = 100;
	public static int xMax = 1200;
	public static int yMax = 700;
	
	public moveMouse(Socket socket){
		sock = socket;
	}
	public void run() {
		try{
			Robot robot = new Robot();
			String temp1 = "";
			String temp2 = "";
			String temp3 = "";
			robot.mouseMove(xCoord, yCoord);
			iStream = new ObjectInputStream(sock.getInputStream()); 
			System.out.println("Mouse move ready");
			while(true){
				temp1 = (String)iStream.readObject();
				temp2 = (String)iStream.readObject();
				temp3 = (String)iStream.readObject();
				int xTemp = Integer.parseInt(temp1);
				int yTemp = Integer.parseInt(temp2);
				int x = moveX(xTemp);
				int y = moveY(yTemp);
				//robot.delay(10);
				if(temp3.equals("y")) {
					robot.mousePress(InputEvent.BUTTON1_MASK);
					robot.mouseRelease(InputEvent.BUTTON1_MASK);
					//robot.mousePress(InputEvent.BUTTON1_MASK);
					//robot.mouseRelease(InputEvent.BUTTON1_MASK);
				}
				//System.out.println("mouse position: " + "("+x+","+y+")");
				robot.mouseMove(x, y);
				//robot.delay(50);
			}
		} catch(AWTException | IOException | ClassNotFoundException e){
			System.out.println("At mouse move thread: " + e);
		}
	}	//end of run
	
	
	// 1366 * 768 is my screen resolution only
	public static int moveX(int x){
		int xRaw = 1366*(x-xMin)/(xMax-xMin);
		return xRaw;
	}
	public static int moveY(int y){
		int yRaw = 768*(y-yMin)/(yMax-yMin);
		return yRaw;
	}
}
