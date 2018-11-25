package kis.sspd.jade.exercise1;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;

@SuppressWarnings("serial")
public class Forgetful extends Agent {
	protected void setup() {
		
		System.out.println("I'm " + getAID().getLocalName()+ " and I would like to show you something.");
		
		addBehaviour(new CyclicBehaviour1());		
		addBehaviour(new CyclicBehaviour2());
	}
	
	private class SingleBehaviour extends OneShotBehaviour {
		public void action() {
			System.out.println("Here it is!");
			goSleep(1000);
		}
	}
	private class CyclicBehaviour1 extends CyclicBehaviour {
		public void action() {
			System.out.println("Where had I lost its?...");
			goSleep(1000);
			//myAgent.addBehaviour(new SingleBehaviour());
		}	
	}
	private class CyclicBehaviour2 extends CyclicBehaviour {
		public void action() {
			System.out.println("I'm going to find...");
			goSleep(1000);
			myAgent.addBehaviour(new SingleBehaviour());
		}	
	}
	
	private void goSleep(long howLongInMilliseconds){
		try {
			Thread.sleep(howLongInMilliseconds);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
