package src;

import src.MultiplesCounter.*;


public class Main {

    public static void main(String [] args){
	MultiplesCounter counter = new MultiplesCounter(3, 5, 1000);
	System.out.println("The sum of multiples is:");
	System.out.println(counter.getSum());
    }
}
