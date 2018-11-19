package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;

@SuppressWarnings("serial")
public class Wolf extends Agent {
	protected int age = 0;
	protected AID parentAID;
	static int adultAge = 2;
	
	protected void setup(){
		System.out.println("Wolf " + getLocalName() + " is getting closer to the farm.");
		addBehaviour(new Live());
		System.out.println("YELLO1");
		addBehaviour(new GetHungry());
		System.out.println("YELLO2");
		parentAID = (AID) getArguments()[0];
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			System.out.println("YELLO3");
			block(1000);
			age += 1;
			System.out.println("YELLO4");
			if (age > adultAge) {
				System.out.println("Awwwwww! I'm adult now #" + getLocalName());
			}
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
