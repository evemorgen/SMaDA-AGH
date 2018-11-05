package kis.sspd.jade.exercise2;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class Pong extends Agent {
	
	private String textToPrint = "Pong!";
	
	protected void setup() {
		addBehaviour(new BounceBack(this, 1000));
		System.out.println(getAID().getLocalName() + " ready.");
	}

	protected void takeDown() {
		System.out.println("Pong down. I repeat. Pong down!");
	}

	private class BounceBack extends TickerBehaviour {

		public BounceBack(Agent a, long period) {
			super(a, period);
		}

		protected void onTick() {
			
			ACLMessage message = myAgent.receive();
			if (message != null) {
				System.out.println(textToPrint);
				ACLMessage reply = message.createReply();
				send(reply);
			}
		}
	}
}
