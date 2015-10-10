import javax.swing.JFrame;

public class goClientGo {
	public static void main(String args[]){
		client firstClient;
		firstClient = new client("127.0.0.1");
		firstClient.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		firstClient.runClient();
	}//end of main
}
