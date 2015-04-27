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
	int sum = 0;

	int current_value = this.a;
	while (current_value <= this.limit) {
	    sum += current_value;
	    current_value += this.a;
	}

	current_value = this.b;
	while (current_value <= this.limit) {
	    sum += current_value;
	    current_value += this.b;
	}

	return sum;
    }
}
