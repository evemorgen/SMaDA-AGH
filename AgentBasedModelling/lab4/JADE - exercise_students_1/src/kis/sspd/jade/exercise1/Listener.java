package kis.sspd.jade.exercise1;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class Listener extends Agent {
	
	protected void setup() {
		System.out.println("Listener " + getAID().getLocalName()+ " is ready.");
		
		addBehaviour(new Listen());
	}
	
	protected void takeDown() {
		System.out.println("Listener " + getAID().getLocalName()+ " is not going to listen anybody anymore.");
	}
	
	private class Listen extends CyclicBehaviour {
		public void action() {
			ACLMessage message = myAgent.receive();
			if (message != null) {
				System.out.println("Somebody is talking!");
				System.out.println(message.getSender().getLocalName() + " is saing: " + message.getContent());
			}
		}
	}
	
}
