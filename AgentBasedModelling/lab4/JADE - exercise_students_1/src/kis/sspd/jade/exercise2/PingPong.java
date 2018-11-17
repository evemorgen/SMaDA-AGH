package kis.sspd.jade.exercise2;

import jade.core.Agent;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;

@SuppressWarnings("serial")
public class PingPong extends Agent {

	AgentController agent1Controller;
	AgentController agent2Controller;
	
	protected void setup() {
		
		System.out.println(getAID().getLocalName() + ": Show me your Ping-Pong.");
		try {
			String pongSecondName = "Pong";
			String pongFirstName  = "Ping";
			Object arguments[] = new Object[1];
			arguments[0] = pongSecondName;
			agent1Controller = getContainerController().createNewAgent(pongSecondName, "kis.sspd.jade.exercise2.Pong", null);
			agent1Controller.start();
			agent2Controller = getContainerController().createNewAgent(pongFirstName, "kis.sspd.jade.exercise2.Ping", arguments);
			agent2Controller.start();
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
	}
	
	protected void takeDown() {
		try {
			agent1Controller.kill();
			agent2Controller.kill();
		} catch (StaleProxyException e) {
			e.printStackTrace();
		}
		System.out.println("PingPong never dies.");
	}
}
