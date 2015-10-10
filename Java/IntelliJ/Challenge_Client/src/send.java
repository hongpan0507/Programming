/**
 * Created by hpan on 1/29/15.
 */

import java.io.ObjectOutputStream;
import java.io.IOException;
import java.util.Scanner;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class send extends Thread {
    private ObjectOutputStream output_stream = null;
    private String message = "";

    // constructor
    public send(ObjectOutputStream _output_stream) {
        output_stream = _output_stream;
    }

    public void run() {
        try {
            JSONObject complete_data = new JSONObject();
            JSONArray temp_loc = new JSONArray();
            JSONArray temp_orien = new JSONArray();
            temp_loc.add(0, "2.5");
            temp_loc.add(1, "3.5");
            complete_data.put("Location", temp_loc);
            temp_orien.add(0,"4.5");
            temp_orien.add(1,"5.5");
            temp_orien.add(2,"6.5");
            complete_data.put("Orientation", temp_orien);
            complete_data.put("Wifi", "7.5");
            while (message != ".disconnect") {
                output_stream.writeObject(complete_data.toString());
                //output_stream.flush();
                Thread.sleep(100);
            } // end of while
            System.out.println("The client has been disconnected");
            output_stream.close();
        } catch (IOException e) {
            System.out.println("send message error" + e);
        } catch (InterruptedException IE) {
            System.out.println("sleep error" + IE);
        }
    } // end of run
}
