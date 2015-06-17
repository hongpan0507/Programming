package edu.tamu.ecen424.firstapp;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class FileActivity extends Activity {
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_file);
		
		addListenerOnButton();
	}
	public void addListenerOnButton(){
		final ImageView image = (ImageView) findViewById(R.id.imageView1);
		int i = 0;
		Button button = (Button) findViewById(R.id.ChangeImage);
		button.setOnClickListener(new View.OnClickListener() {
		    public void onClick(View v) {
		    	image.setImageResource(R.drawable.ic_launcher);
		    }
	    });
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.file, menu);
		return true;
	}
}
