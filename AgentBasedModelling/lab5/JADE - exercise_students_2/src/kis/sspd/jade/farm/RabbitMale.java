package kis.sspd.jade.farm;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;


@SuppressWarnings("serial")
public class RabbitMale extends Agent {
	protected int age = 0;
	static int lifetime = 10;
	static int adultAge = 2;
	
	protected void setup(){
		System.out.println("Male " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Behave());
	}
	
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			//TODO
		}
	}
	
	private class Behave extends CyclicBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class GetOlder extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class TryToHaveChildren extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class Court extends OneShotBehaviour {
		public void action() {
			//TODO
		}
	}
	
	protected void takeDown(){
		System.out.println("Male " + getLocalName() + " is dying.");
	}
}
