public class IPCheck {
	private int parseIP = 0;
	//private int count = 0;
	private int rangeCheck = 0;
	private String IP;
	private boolean goodIP = false;

	// constructor
	public IPCheck() {

	}// end of constructor
	
	//start
	public boolean run(String IPAddress){
		validate(IPAddress);
		if (goodIP) {return true;}
		else {return false;}
	}//end of run()
	
	// checking dots + ranger
	private void validate(String IPAddress) {	
		int record = 0;
		
		goodIP = false;
		for (int count = 0; IPAddress.indexOf(".", count) != -1; count = parseIP + 1) {
			record++;	//number of dots
			parseIP = IPAddress.indexOf(".", count);	//dot position
			IP = IPAddress.substring(count, parseIP);	// part of IP address = to the left of dot + to the right of dot
			rangeCheck = Integer.parseInt(IP);	//convert to integer to check for range
			if(rangeCheck < 0 || rangeCheck > 255){
				goodIP = false;
				System.out.println("Out of range");
				break;
			}else if(record == 3){    //checking the last part of IP
				IP = IPAddress.substring(parseIP + 1);
				rangeCheck = Integer.parseInt(IP);
				if(rangeCheck < 0 || rangeCheck > 255){	
					System.out.println("Out of range");
					goodIP = false;
					break;
				}else{
					goodIP = true;
					break;
				}//end of else
			} //end of else if()
		} //end of for()
	} // end of validate
		
		/*
		if (IPAddress.indexOf(".") != -1) { 
			parseIP = IPAddress.indexOf(".");	// first dot position
			IP = IPAddress.substring(0, parseIP);	// first part of IP address = 0 to the left of the first dot
			//System.out.println("first dot position: " + parseIP);
			//System.out.println("First part: " + IP);
			count = parseIP + 1;	// to the right of the first dot
			rangeCheck = Integer.parseInt(IP);	//convert to integer to check for range
			if (rangeCheck >= 0 && rangeCheck <= 255 && IPAddress.indexOf(".", count) != -1) { 
				parseIP = IPAddress.indexOf(".", count);	//second dot position
				IP = IPAddress.substring(count, parseIP); // second part of IP address = to the right of the first dot + to the left of the second dot
				//System.out.println("second dot position: " + parseIP);
				//System.out.println("second part: " + IP);
				count = parseIP + 1;	//to the right of the second dot
				rangeCheck = Integer.parseInt(IP);	//convert to integer to check for range
				if (rangeCheck >= 0 && rangeCheck <= 255 && IPAddress.indexOf(".", count) != -1) { 
					parseIP = IPAddress.indexOf(".", count);	//third dot position
					IP = IPAddress.substring(count, parseIP); // third part of IP address = to the right of the second dot + to the left of the third dot
					//System.out.println("third dot position: " + parseIP);
					//System.out.println("third part: " + IP);
					count = parseIP + 1;	//to the right of the third dot
					rangeCheck = Integer.parseInt(IP);	//convert to integer to check for range
					if(rangeCheck >= 0 && rangeCheck <= 255){
						IP = IPAddress.substring(count); // last part of IP address = to the right of the third dot + to the end
						//System.out.println("last part: " + IP);
						rangeCheck = Integer.parseInt(IP);	//convert to integer to check for range
							if(rangeCheck >= 0 && rangeCheck <= 255){
								return true;
							}else{
								return false;
							}	
					} else{
						return false;
					}
				} else {
					return false;
				}
			} else {
				return false;
			}
		} else {
			return false;
		} // end of else
		*/
	
}
