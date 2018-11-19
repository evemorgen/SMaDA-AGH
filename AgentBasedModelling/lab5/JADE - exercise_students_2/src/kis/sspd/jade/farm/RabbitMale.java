package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;


@SuppressWarnings("serial")
public class RabbitMale extends Agent {
	protected int age = 0;
	static int lifetime = 10;
	static int adultAge = 2;
	protected AID parentAID;
	
	protected void setup(){
		System.out.println("Male " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Listen());
		addBehaviour(new Behave());
		parentAID = (AID) getArguments()[0];

	}
	
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			age += 1;
			if (age == adultAge) {
				System.out.println("Hey look, I'm adult male now! #" + getLocalName());
			}
			if (age == lifetime  + 1) {
				ACLMessage message = new ACLMessage(ACLMessage.INFORM);
				message.setContent(getLocalName());
				message.addReceiver(parentAID);
				send(message);
			}
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
	
	private class Behave extends CyclicBehaviour {
		public void action() {
			//TODO
		}
	}
	
	@SuppressWarnings("unused")
	private class GetOlder extends OneShotBehaviour {
		public void action() {
			//TODO
			age += 1;
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
