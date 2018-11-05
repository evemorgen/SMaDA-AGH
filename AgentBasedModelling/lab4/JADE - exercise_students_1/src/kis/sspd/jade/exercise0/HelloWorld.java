package kis.sspd.jade.exercise0;

import jade.core.Agent;

@SuppressWarnings("serial")
public class HelloWorld extends Agent{
	
	public void setup(){    
        System.out.println("Hello Word! My name is: " + getName()); 
	}
}
