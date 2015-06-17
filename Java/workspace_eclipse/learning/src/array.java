class array {
	public static void main(String[] args){
		System.out.println("Index\tValue");
		
		int bear[]={32,34,13,12,51};
		int sum=0;
		
		for(int counter=0; counter<bear.length; counter++){
			System.out.println(counter + "\t" + bear[counter]);
			sum+=bear[counter];
		}
		System.out.println("the sum: "+sum);
	}
}
