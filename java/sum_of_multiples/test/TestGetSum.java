package test;

//import org.junit.*;
import junit.framework.TestCase;
import src.*;


public class TestGetSum extends TestCase{

    private MultiplesCounter counter;

    public TestGetSum() {
	this.counter = new MultiplesCounter(3, 5, 6);
    }

    public void testThatWithNoMultiplesReturnsCorrectSum(){
	int sum = this.counter.getSum();
	this.assertEquals(sum, 8);
    }
}
