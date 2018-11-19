package kis.sspd.jade.farm;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;

@SuppressWarnings("serial")
public class Wolf extends Agent {
	protected int age = 0;
	static int adultAge = 2;
	
	protected void setup(){
		System.out.println("Wolf " + getLocalName() + " is getting closer to the farm.");
		addBehaviour(new Live());
		addBehaviour(new GetHungry());
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			//TODO
		}
	}
	
	private class GetHungry extends CyclicBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class GetOld extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class EatBunny extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	protected void takeDown(){
		System.out.println("Wolf " + getLocalName() + " is daying.");
	}	
}
