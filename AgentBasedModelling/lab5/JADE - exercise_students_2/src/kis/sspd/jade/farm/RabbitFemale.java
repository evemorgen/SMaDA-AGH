package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class RabbitFemale extends Agent {
	protected int age = 0;
	protected AID parentAID;
	static int lifetime = 10;
	static int adultAge = 2;
	
	protected void setup(){
		System.out.println("Female " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Listen());
		parentAID = (AID) getArguments()[0];
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			age += 1;
			System.out.println("Tick! " + getLocalName());
			if (age == adultAge) {
				System.out.println("Hey look, I'm adult female now! #" + getLocalName());
			}
			if (age == lifetime + 1) {
				ACLMessage message = new ACLMessage(ACLMessage.INFORM);
				message.addReceiver(parentAID);
				send(message);
			}
			//TODO
		}
	}
	
	private class Listen extends CyclicBehaviour {
		public void action() {
			ACLMessage message = myAgent.blockingReceive();
			System.out.println(getLocalName() + " received message " + message.toString());
			if(message.getPerformative() ==  ACLMessage.INFORM && message.getContent().equals("time to die!")) {
				myAgent.doDelete();
			}
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
