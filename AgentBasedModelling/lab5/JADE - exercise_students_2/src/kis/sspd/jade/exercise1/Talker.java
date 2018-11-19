package kis.sspd.jade.exercise1;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class Talker extends Agent {
	
	private String annocement = "I'm telling everybody everywhere that the annoncement...";
	private String receiver;
	
	protected void setup(){
		Object[] arguments = getArguments();
		receiver = arguments[0].toString();
		System.out.println("Talker " + getAID().getLocalName()+ " is talking a microphone.");
		
		addBehaviour(new Talk());
	}
	
	protected void takeDown(){
		System.out.println("Talker " + getAID().getLocalName()+ " is going to say never more.");
	}
	
	private class Talk extends OneShotBehaviour {

		public void action() {
			ACLMessage message = new ACLMessage(ACLMessage.INFORM);
			message.setContent(annocement);
			message.addReceiver(new AID(receiver, AID.ISLOCALNAME));
			send(message);
		}
		
	}

}
