package kis.sspd.jade.exercise0;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;

@SuppressWarnings("serial")
public class HelloWorld2 extends Agent {

	public void setup() {
		
		System.out.println("Hello Word! My name is " + getName());

		addBehaviour(new TickerBehaviour(this, 6000) {
			protected void onTick() {
				myAgent.doDelete();
			}
		});
	}
	
	protected void takeDown() {
		System.out.println("Goodbye Word - " + getName());
	}
}
