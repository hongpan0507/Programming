import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;

public class DaemonTest {
    public static void main(String[] args) {
        try {
            /*
            new WorkerThread().start();
            Thread.sleep(7500);
            */

            //time_instant_test time_test = new time_instant_test();
            //time_test.run();
            HashMap<Integer, String> hash_map_test = new HashMap<Integer, String>(1000);
            for(int i = 0; i < 10; ++i){
                hash_map_test.put(i, "test");
            }
            System.out.println(hash_map_test.size());
            System.out.println(hash_map_test.get(1));
        } catch (Exception e) {
            System.out.println(e);
        }


    }
}



class time_instant_test {
    boolean new_time = true;
    Instant t1 = Instant.now();
    Instant t2 = Instant.now();

    public time_instant_test () {

    }

    public void run () {
        try {
            boolean new_time = true;
            Instant t1 = Instant.now();
            Instant t2 = Instant.now();
            while (true) {
                if (new_time == true) {
                    t1 = Instant.now();
                    new_time = false;
                }
                Thread.sleep(1);
                t2 = Instant.now();
                long ms = Duration.between(t1, t2).toMillis();
                if (ms > 999) {
                    System.out.println(t2);
                    new_time = true;
                }
            }
        } catch (Exception e) {

        }
    }
}

class WorkerThread extends Thread {
    public WorkerThread() {
        //setDaemon(false) ;   // When false, (i.e. when it's a user thread),
        // the Worker thread continues to run.
        // When true, (i.e. when it's a daemon thread),
        // the Worker thread terminates when the main
        // thread terminates.
    }
    public void run() {
        int count=0 ;
        while (true) {
            System.out.println("Hello from Worker "+count++) ;
            try {
                sleep(5000);
            } catch (InterruptedException e) {}
        }
    }
}