package kis.sspd.jade.farm;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;

@SuppressWarnings("serial")
public class RabbitFemale extends Agent {
	protected int age = 0;
	static int lifetime = 10;
	static int adultAge = 2;
	
	protected void setup(){
		System.out.println("Female " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Listen());
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			//TODO
		}
	}
	
	private class Listen extends CyclicBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class BreedNewRabbits extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	protected void takeDown(){
		System.out.println("Famale " + getLocalName() + " is dying.");
	}
}
