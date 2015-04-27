package src;

public class MultiplesCounter {
    private int a;
    private int b;
    private int limit;

    public MultiplesCounter(){
	this.a = 3;
	this.b = 5;
	this.limit = 1000;
    }

    public MultiplesCounter(int a, int b, int limit){
	this.a = a;
	this.b = b;
	this.limit = limit;
    }

    public int getSum(){
	return this.a + this.b;
    }
}
