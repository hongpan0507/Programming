package edu.tamu.ecen424.MP5;

import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.util.Log;
import android.view.GestureDetector;
import android.view.GestureDetector.OnDoubleTapListener;
import android.view.GestureDetector.OnGestureListener;
import android.view.Menu;
import android.view.MotionEvent;
import android.widget.ImageView;

public class ClientActivity extends Activity implements OnGestureListener, OnDoubleTapListener{
	
	Handler updateConversationHandler;
	Thread clientThread = null;
	// input stream
	public DataInputStream diStream = null;
	// output stream
	private ObjectInputStream iStream = null;
	public FileOutputStream foStream = null;
	private GestureDetector gd;
	public static int xCoord = 1366/2;
	public static int yCoord = 768/2;
	public static int move = 0;
	public static String right = "1";
	public static String left = "2";
	public static String down = "3";
	public static String up = "4";
	public static boolean right_bool = false;
	public static boolean left_bool = false;
	public static boolean down_bool = false;
	public static boolean up_bool = false;
	public static double xraw = 0;
	public static double yraw = 0;
	public static double double_tab = 0;
	public static double previous_tab = 0;
	
	public byte[] buffer = new byte[1024];
	public String imageName = "1.PNG";
	public long imageSize = 0;
	public int SizeCount = 0;
	public static int Count = 0;
	public Socket sock;
	public int port = 2013;
	static String ServerIP = "10.201.76.142";
	static String TAG = "ServerActivity";
	static String temp = null;
	static String path = null;
	static File image = null;
	static File sdCard =null;
	static File dir = null;
	static ImageView img;
	Bitmap bm = null;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_client);
		
		/*
		findViewById(R.id.right_butt).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v1) {
				right_bool = true;
			}
		});
		findViewById(R.id.left_butt).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v1) {
				left_bool = true;
			}
		});
		*/

		
		gd = new GestureDetector(this);
		img = (ImageView)findViewById(R.id.ImageView);
/*		Intent intent = getIntent();
		Bundle extras = intent.getExtras();
		port = extras.getInt("portNumb");
		ServerIP = extras.getString("IP_Address");*/
		ServerIP = "10.201.76.142";
		port = 2013;

		updateConversationHandler = new Handler();
		this.clientThread = new Thread(new ClientThread());
		this.clientThread.start();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.client, menu);
		return true;
	}
	
	public void onStop(){
		super.onStop();
		try{
			sock.close();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}	//end of onStop()
	
	public class ClientThread implements Runnable{
		@Override
		public void run() {
			try{
				sock = new Socket(ServerIP, port);
				if(sock != null){
					ServerIP = sock.getInetAddress().getHostName();
					MouseMoveThread MouseMove = new MouseMoveThread(sock);
					new Thread(MouseMove).start();
					diStream = new DataInputStream(sock.getInputStream());
					Log.d("ServerActivity",ServerIP+" connected!");
					sdCard = Environment.getExternalStorageDirectory();
					dir = new File(sdCard.getAbsolutePath()+"/remote_desk_test");
					if(!(dir.exists())){
						dir.mkdir();
					}
					while (true) {
						imageName = diStream.readUTF();
						image = new File(dir,imageName);
						foStream = new FileOutputStream(image);
						
						imageSize = diStream.readLong();
						// receiving image
						while (imageSize > 0 && (SizeCount = diStream.read(buffer, 0,(int) Math.min(buffer.length, imageSize))) != -1) {
							foStream.write(buffer, 0, SizeCount);
							imageSize -= SizeCount;
						}
						Log.d("ServerActivity",":::: "+image.getAbsolutePath());
						Log.d("ServerActivity"," "+xraw+ " "+yraw);
						Log.d("ServerActivity"," "+double_tab);
						path = image.getAbsolutePath();
						updateConversationHandler.post(new updateUIThread(path));
					}
				}
			} catch(IOException e) {
				e.printStackTrace();
			} //end of try catch
		}	//end of run
	}	//end of server thread
	
	public class MouseMoveThread implements Runnable{
		private Socket clientSocket;
		private ObjectOutputStream outgoing;
		//constructor
		public MouseMoveThread(Socket clientSock){
			this.clientSocket = clientSock;
			try {
				outgoing = new ObjectOutputStream(new BufferedOutputStream(this.clientSocket.getOutputStream()));
				outgoing.flush();
			} catch(IOException e) {
				e.printStackTrace();
			}
		}//end of constructor
		
		@Override
		public void run() {
			while(!Thread.currentThread().isInterrupted()) {
				try {
					String xTemp = String.valueOf((int)xraw);
					String yTemp = String.valueOf((int)yraw);
					
					outgoing.writeObject(xTemp);
					outgoing.flush();
					outgoing.writeObject(yTemp);
					outgoing.flush();
					if(previous_tab != double_tab ){
						previous_tab = double_tab;
						outgoing.writeObject("y");
						outgoing.flush();
					} else {
						outgoing.writeObject("n");
						outgoing.flush();
					}
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
		}	//end of run
	}	//end of MouseMoveThread
	
	public class updateUIThread implements Runnable{
		private String ImagePath = null;
		public updateUIThread(String path){
			this.ImagePath = path;
		}
		@Override
		public void run() {
			bm = BitmapFactory.decodeFile(ImagePath);
			img.setImageBitmap(bm);
		}
	}//end of updateUIThread

	@Override
	public boolean onTouchEvent(MotionEvent event){
		//TODO Auto-generated method stub
		return gd.onTouchEvent(event);
	}
	@Override
	public boolean onDown(MotionEvent arg0) {
		// TODO Auto-generated method stub
		xraw = arg0.getRawX();
		yraw = arg0.getRawY();	
		return true;
	}

	@Override
	public boolean onFling(MotionEvent arg0, MotionEvent arg1, float arg2,
			float arg3) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public void onLongPress(MotionEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public boolean onScroll(MotionEvent arg0, MotionEvent arg1, float arg2,
			float arg3) {
		// TODO Auto-generated method stub
		xraw = arg1.getRawX();
		yraw = arg1.getRawY();
		return true;
	}

	@Override
	public void onShowPress(MotionEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public boolean onSingleTapUp(MotionEvent arg0) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean onDoubleTap(MotionEvent arg0) {
		// TODO Auto-generated method stub
		double_tab = arg0.getEventTime();
		return true;
	}

	@Override
	public boolean onDoubleTapEvent(MotionEvent arg0) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean onSingleTapConfirmed(MotionEvent arg0) {
		// TODO Auto-generated method stub
		return false;
	}
}
