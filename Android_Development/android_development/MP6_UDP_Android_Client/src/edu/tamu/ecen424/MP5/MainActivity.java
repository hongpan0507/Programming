package edu.tamu.ecen424.MP5;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity {
	//private TextView text;
	private TextView portText;
	private TextView IPText;
	private TextView PWText;
	private EditText edit;
	private Button butt1;
	private Button butt2;
	private Button butt3;
	String temp = null;
	String Password = "2015";
	String IP_Address = null;
	int port = 2013;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {	//set up the server
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		//text = (TextView) findViewById(R.id.textView1);
		portText = (TextView) findViewById(R.id.portID);
		IPText = (TextView) findViewById(R.id.maxID);
		PWText = (TextView) findViewById(R.id.pw_text);
		edit = (EditText) findViewById(R.id.editText1);
		butt1 = (Button) findViewById(R.id.Send);
		butt2 = (Button) findViewById(R.id.button2);
		butt3 = (Button) findViewById(R.id.pw_butt);
		butt1.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				temp = edit.getText().toString();
				portText.setText("Port Number: " +temp);
				port = Integer.parseInt(temp);
			}
		});
		butt2.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				temp = edit.getText().toString();
				IPText.setText("Server IP Address: " + temp);
				IP_Address = temp;
			}
		});
		butt3.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				temp = edit.getText().toString();
				PWText.setText("Server Password: " + temp);
				Password = temp;
			}
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	public void ServerActivity(View view){	//start up the server
		Intent i = new Intent(this,ClientActivity.class);
		Bundle extras = new Bundle();
		extras.putInt("portNumb", port);
		extras.putString("IP_Address", IP_Address);
		extras.putString("Password", Password);
		i.putExtras(extras);
		startActivity(i);	//intent is the screen that pops up
	}	
}