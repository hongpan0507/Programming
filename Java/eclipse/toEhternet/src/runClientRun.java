import javax.swing.JFrame;

public class runClientRun {
	public static void main(String[] args) {
		Thread go = new Thread() {
			public void run() {	
				arduinoClient Client = new arduinoClient();
				Client.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				Client.run();
			}// end of run()
		};// end of thread write()
		go.start();
	}// end of main
}
