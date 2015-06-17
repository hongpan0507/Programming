package edu.tamu.ecen424.firstapp;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends Activity {
	
	//Defining a button, an editext box, and a text view.
	private Button b1;
	private EditText ed1;
	private TextView tx1; 
	private String msg;
	
	public void dispActivity(View view){
		startActivity(new Intent(this,DispActivity.class));	//intent is the screen that pops up
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		//Here, I have associated the b1 with the ID button1, ed1 with the ID typebox, 
		// and tx1 with the ID textView2.  Note that textView1 (see xml file) is used to displaya  fixed message.
		b1 = (Button) findViewById(R.id.button1);
		ed1 = (EditText) findViewById(R.id.typebox);
		tx1 = (TextView) findViewById(R.id.textView2);
		
		//Here is the Button functionality.  Note how the entire functionality is within the listener.
		b1.setOnClickListener(new View.OnClickListener() {
		    public void onClick(View v) {
	        System.out.println("Inside Button\n");
	        
	       //Here is the Edit text functionality.
	        msg = ed1.getText().toString();
	        
	      //Toast can be used to display on screen for a short duration
	        Context context = getApplicationContext(); 
	        int duration = Toast.LENGTH_SHORT;
	        Toast toast = Toast.makeText(context, msg, duration); //Toasting message entered
	        toast.show();
	        
	      //Also Display stuff on the Textview
			tx1.setText(msg);
	        }
	    });		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
}
