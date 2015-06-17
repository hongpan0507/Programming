import java.awt.AWTException;
import java.awt.Robot;
import java.util.Scanner;


public class test {
	public static int xCoord = 00;
	public static int yCoord = 500;
	public static int move = 0;
	public static void main(String[] args) {
		try{
			Scanner input = new Scanner(System.in);
			Robot robot = new Robot();
			while(true){
				switch(move){
				case 1:	//move right
					
					break;
				case 2:	//move left
					break;
				case 3: //move up
					break; 
				case 4:	//move down
					break;	
				default: //stop moving
						break;
				}
				xCoord = input.nextInt();
				yCoord = input.nextInt();
				robot.mouseMove(xCoord, yCoord);
				robot.delay(100);
				
			}
		}catch(AWTException e){
			System.out.println(e);
		}
	}
	
	public static void moveRight(){
		if(xCoord < 1366) 
			xCoord = xCoord+10;
	}
	public static void moveLeft(){
		if(xCoord > 0) 
			xCoord = xCoord-10;
	}
	public static void moveUp(){
		if(yCoord < 768) 
			yCoord = yCoord-10;
	}
	public static void moveDown(){
		if(yCoord > 0) 
			yCoord = yCoord+10;
	}
	
}
