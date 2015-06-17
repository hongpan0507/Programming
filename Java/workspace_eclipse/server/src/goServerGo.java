import javax.swing.JFrame;

public class goServerGo {
	public static void main(String args[]){
		server firstServer = new server();
		firstServer.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		firstServer.runServer();
	}//end of main
}
