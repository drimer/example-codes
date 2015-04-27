package test;

//import org.junit.*;
import junit.framework.TestCase;
import src.*;


public class TestGetSum extends TestCase{

    public void testThatWithNoMultiplesReturnsCorrectSum(){
	MultiplesCounter counter = new MultiplesCounter(3, 5, 5);
	int sum = counter.getSum();
	this.assertEquals(8, sum);
    }

    public void testThatWithAFewMultiplesTheSumIsCorrect(){
	MultiplesCounter counter = new MultiplesCounter(2, 3, 8);
	int sum = counter.getSum();
	this.assertEquals(29, sum);
    }
}
