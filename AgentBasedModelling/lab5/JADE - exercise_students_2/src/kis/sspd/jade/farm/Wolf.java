package kis.sspd.jade.farm;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.OneShotBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

@SuppressWarnings("serial")
public class Wolf extends Agent {
	protected int age = 0;
	protected AID parentAID;
	static int adultAge = 2;
	protected boolean waiting = false;

	protected void setup(){
		System.out.println("Wolf " + getLocalName() + " is getting closer to the farm.");
		addBehaviour(new Live());
		addBehaviour(new GetHungry());
        addBehaviour(new Listen(this, 1000));

        parentAID = (AID) getArguments()[0];
	}
	
	
	private class Live extends CyclicBehaviour {
		public void action() {
			block(1000);
			age += 1;
			if (age == adultAge) {
				System.out.println("Awwwwww! I'm adult now #" + getLocalName());
			}
		}
	}
	
	private class GetHungry extends CyclicBehaviour {
		public void action() {
            block(1000);
			ACLMessage request = new ACLMessage(ACLMessage.REQUEST);
			request.setContent("randomRabbitName");
			request.addReceiver(parentAID);
			send(request);
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
                    case ACLMessage.UNKNOWN:
                        break;
                    case ACLMessage.INFORM:
                        String rabbitName = message.getContent();
                        if (rabbitName != null) {
                            System.out.println("I'm gonna eat'ya litte rabbit! #" + rabbitName);
                            ACLMessage dinnerPlans = new ACLMessage(ACLMessage.REQUEST);
                            dinnerPlans.setContent("I'm gonna eat'ya litte rabbit!");
                            dinnerPlans.addReceiver(myAgent.getAID(rabbitName.split("@")[0]));
                            send(dinnerPlans);
                        break;
                    }
                }
            }
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
