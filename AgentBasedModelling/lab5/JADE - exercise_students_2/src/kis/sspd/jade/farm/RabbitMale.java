package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;
import kis.sspd.jade.exercise1.Forgetful;


@SuppressWarnings("serial")
public class RabbitMale extends Agent {
	protected int age = 0;
	static int lifetime = 10;
	static int adultAge = 2;
	protected AID parentAID;
	protected String reason;
	protected int procreationCooldown = 3;
	
	protected void setup() {
		System.out.println("Male " + getLocalName() + " appeared on the farm.");
		addBehaviour(new Live());
		addBehaviour(new Listen(this, 1000));
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
				message.setContent(getName());
				message.addReceiver(parentAID);
				send(message);
			}
			if (procreationCooldown <= 0 && age >= adultAge) {
				myAgent.addBehaviour(new Court());
			}
			procreationCooldown--;

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
				switch(message.getPerformative()) {
					case ACLMessage.INFORM:
						reason = "Natural death";
						myAgent.doDelete();
						break;
					case ACLMessage.REQUEST:
                        if(message.getContent().equals("Are you a female?")) {
                            return;
                        } else {
                            ACLMessage reply = new ACLMessage(ACLMessage.REQUEST);
                            reply.addReceiver(message.getSender());
                            System.out.println("Ok, guess I'll be eaten? " + getLocalName());
                            reply.setContent("OK!");
                            send(reply);
                            reason = "Eaten";
                            doDelete();
                        }
						break;
				}
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

	private class TryToHaveChildren extends OneShotBehaviour {

		protected AID female;

		public TryToHaveChildren(AID sender) {
			female = sender;
		}

		public void action() {
			System.out.println("Making small rabbits now #" + getLocalName());
			procreationCooldown = 3;
			ACLMessage procreationMessage = new ACLMessage(ACLMessage.INFORM);
			procreationMessage.setContent("Lets make sum love Gurl");
			procreationMessage.addReceiver(female);
			send(procreationMessage);
		}
	}
	
	@SuppressWarnings("unused")
	private class Court extends OneShotBehaviour {
		public void action() {

			ACLMessage request = new ACLMessage(ACLMessage.REQUEST);
			request.setContent("randomRabbitName");
			request.addReceiver(parentAID);
			send(request);
			ACLMessage response = myAgent.blockingReceive(1000);
			if(response != null) {
				myAgent.addBehaviour(new TryToHaveChildren(myAgent.getAID(response.getContent().split("@")[0])));
			}
		}
	}
	
	protected void takeDown(){
		System.out.println("Male " + getLocalName() + " is dying.");
	}
}
