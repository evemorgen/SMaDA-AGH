package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class RabbitFemale extends Agent {
	protected int age = 0;
	protected AID parentAID;
	static int lifetime = 10;
	static int adultAge = 2;
	protected String reason;

	public boolean isAdult() {
		return age >= adultAge;
	}


	
	protected void setup(){
		System.out.println("Female " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Listen(this, 1000));

		parentAID = (AID) getArguments()[0];
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			age += 1;
			if (age == adultAge) {
				System.out.println("Hey look, I'm adult female now! #" + getLocalName());
			}
			if (age == lifetime + 1) {
				ACLMessage message = new ACLMessage(ACLMessage.INFORM);
				message.setContent(getName());
				message.addReceiver(parentAID);
				send(message);
			}
			//TODO
		}
	}

	private class Listen extends TickerBehaviour {

		public Listen(Agent a, long period) {
			super(a, period);
		}

		@Override
		protected void onTick() {
			ACLMessage message = myAgent.receive();
			if(message != null) {
				switch (message.getPerformative()) {
					case ACLMessage.INFORM:
						if (message.getContent().equals("Lets make sum love Gurl")) {
							myAgent.addBehaviour(new BreedNewRabbits());
						} else {
							myAgent.doDelete();
						}
						break;
					case ACLMessage.REQUEST:
						if(message.getContent().equals("Are you a female?")) {
							ACLMessage reply = message.createReply();
							reply.setPerformative(ACLMessage.INFORM);
							reply.setContent("HECK YEAH.");
							if(isAdult()) {
								send(reply);
							}
						}
				}
			}
		}
	}
	
	@SuppressWarnings("unused")
	private class BreedNewRabbits extends OneShotBehaviour {
		public void action() {
			System.out.println("Making littie rabbits #" + getLocalName());
			ACLMessage breedMessage = new ACLMessage(ACLMessage.REQUEST);
			breedMessage.setContent("breedRabits");
			breedMessage.addReceiver(parentAID);
			send(breedMessage);
		}
	}
	
	protected void takeDown(){
		System.out.println("Famale " + getLocalName() + " is dying.");
	}
}
