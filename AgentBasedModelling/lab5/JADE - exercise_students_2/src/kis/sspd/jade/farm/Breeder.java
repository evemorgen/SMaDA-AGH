package kis.sspd.jade.farm;

import java.util.ArrayList;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;

@SuppressWarnings("serial")
public class Breeder extends Agent {
	final static String studentsMail = ""; /// Preferred AGH's mail
	final static String studentsName = "";
	final static String studentsId = "";
	
	private ArrayList<AgentController> rabbits = new ArrayList<AgentController>();
	Integer nextRabbitNumber = 0;
	private ArrayList<AgentController> wolfs = new ArrayList<AgentController>();
	Integer nextWolfNumber = 0;

	protected void setup() {
		if (studentsMail.isEmpty() || studentsName.isEmpty() || studentsId.isEmpty()) {
			System.out.println("Student's data empty! Please input your mail, name and id.");
		}
		
		addBehaviour(new ListenBehaviour());
		System.out.println("Breeder " + getLocalName() + " is ready.");
	}

	private class ListenBehaviour extends CyclicBehaviour {
		public void action() {
			ACLMessage message = myAgent.blockingReceive();
			int aim = message.getPerformative();
			if (message != null) {
				switch (aim) {
				case ACLMessage.REQUEST:
					switch (message.getContent()) {
					case "breedRabits":
						breedRabits();
						break;
					case "enticeWolf":
						enticeWolf();
						break;
					case "randomRabbitName":
						passNameOfRandomRabbit(message);
						break;
					}
					break;
				case ACLMessage.INFORM:
					removeRabbit(message);
					break;
				default:
					ACLMessage reply = message.createReply();
					reply.setPerformative(ACLMessage.NOT_UNDERSTOOD);
					send(reply);
				}
			}
			if (nextRabbitNumber == 100)
			{
				myAgent.doDelete();
			}
		}
	}

	private void passNameOfRandomRabbit(ACLMessage message) {
		try {
			ACLMessage reply = message.createReply();
			if (rabbits.size() > 0) {
				reply.setPerformative(ACLMessage.INFORM);
				Integer rabitNumber = Double.valueOf(
						Math.random() * rabbits.size()).intValue();
				reply.setContent(rabbits.get(rabitNumber).getName());
				send(reply);
			} else {
				reply.setPerformative(ACLMessage.UNKNOWN);
				send(reply);
			}
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}

	public void removeRabbit(ACLMessage message) {
		try {
			String rabbitName = message.getContent();
			AgentController rabbit2Remove = null;
			for (AgentController rabbit : rabbits) {
				if (rabbit.getName().equals(rabbitName)){
					rabbit2Remove = rabbit;
				}
			}
			rabbits.remove(rabbit2Remove);
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}

	private void breedRabits() {
		int bunniesNumber = Double.valueOf(Math.random() * 4.0 + 3.0)
				.intValue();
		for (int iterator = 0; iterator < bunniesNumber; iterator++) {
			if (Math.random() < 0.5)
				breedMale();
			else
				breedFemale();
		}
	}

	private void breedMale() {
		try {
			String rabbitName = nextRabbitNumber.toString();
			nextRabbitNumber++;
			AgentController rabit = getContainerController().createNewAgent(
					rabbitName, "kis.sspd.jade.farm.RabbitMale", null);
			rabit.start();
			rabbits.add(rabit);
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}

	private void breedFemale() {
		try {
			String rabbitName = nextRabbitNumber.toString();
			nextRabbitNumber++;
			AgentController rabit = getContainerController().createNewAgent(
					rabbitName, "kis.sspd.jade.farm.RabbitFemale", null);
			rabit.start();
			rabbits.add(rabit);
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}

	private void enticeWolf() {
		try {
			String wolfName = nextWolfNumber.toString();
			nextWolfNumber++;
			AgentController wolf = getContainerController().createNewAgent(
					wolfName, "kis.sspd.jade.farm.Wolf", null);
			wolf.start();
			wolfs.add(wolf);
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}

	protected void takeDown() {
		try {
			for (AgentController rabbit : rabbits)
				rabbit.kill();
			for (AgentController wolf : wolfs)
				wolf.kill();
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
		System.out.println("The farm is now closed.");
	}
}
