package kis.sspd.jade.exercise2;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.OneShotBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class Ping extends Agent {
	
	private String text2Print = "Ping!";
	private String receiver;
	
	protected void setup() {
		Object[] arguments = getArguments();
		receiver = arguments[0].toString();
		
		addBehaviour(new LetsStart());
		System.out.println(getAID().getLocalName() + " ready.");
	}

	protected void takeDown() {
		System.out.println("Ping down. I repeat. Ping down!");
	}

	private class LetsStart extends OneShotBehaviour {

		public void action() {
			
			System.out.println(text2Print);
			
			ACLMessage message = new ACLMessage(ACLMessage.INFORM);
			message.addReceiver(new AID(receiver, AID.ISLOCALNAME));
			send(message);
			
			myAgent.addBehaviour(new Return(myAgent,1000));
		}
	}
	
	private class Return extends TickerBehaviour {

		public Return(Agent a, long period) {
			super(a, period);
		}

		protected void onTick() {
			ACLMessage message = myAgent.receive();
			if (message != null) {
				System.out.println(text2Print);

				ACLMessage reply = message.createReply();
				send(reply);
			}
		}
	}
}
