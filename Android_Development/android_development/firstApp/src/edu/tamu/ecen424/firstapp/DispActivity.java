package edu.tamu.ecen424.firstapp;

import java.io.File;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

public class DispActivity extends Activity {
	

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_disp);
		findViewById(R.id.return_button).setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				finish();	//finish activity and go back to the main menu
			}
		});
		
		Button btn1=(Button) findViewById(R.id.button1);
		btn1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Intent intent = new Intent(DispActivity.this, FileActivity.class);
				startActivity(intent);
			}
		});
		
		File folder = new File("./Removable/MicroSD/TAMU/ECEN424/");
		File[] listOfFiles = folder.listFiles();
		String name[] = new String[listOfFiles.length];{
			for(int i=0;i<listOfFiles.length;i++){
				name[i]=listOfFiles[i].getName();
			}
		}
		ListView list = (ListView)findViewById(R.id.listView1);
		ArrayAdapter<String> adapter=new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, name);
		list.setAdapter(adapter);
		list.setOnItemClickListener(new OnItemClickListener(){
			public void onItemClick(AdapterView<?> av, View v, int pos, long id){
				Toast.makeText(DispActivity.this, av.getItemAtPosition(pos).toString(), Toast.LENGTH_SHORT).show();
			}
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.disp, menu);
		return true;
	}
}
