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
	private TextView maxText;
	private EditText edit;
	private Button butt1;
	private Button butt2;
	String temp = null;
	int port = 2013;
	int maxClient = 2;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {	//set up the server
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		//text = (TextView) findViewById(R.id.textView1);
		portText = (TextView) findViewById(R.id.portID);
		maxText = (TextView) findViewById(R.id.maxID);
		edit = (EditText) findViewById(R.id.editText1);
		butt1 = (Button) findViewById(R.id.Send);
		butt2 = (Button) findViewById(R.id.button2);
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
				maxText.setText("Max number of Clients: " + temp);
				maxClient = Integer.parseInt(temp);
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
		Intent i = new Intent(this,ServerActivity.class);
		Bundle extras = new Bundle();
		extras.putInt("portNumb", port);
		extras.putInt("maxClient", maxClient);
		i.putExtras(extras);
		startActivity(i);	//intent is the screen that pops up
	}	
}