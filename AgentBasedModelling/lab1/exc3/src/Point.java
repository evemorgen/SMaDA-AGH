import java.util.ArrayList;

public class Point {
    private ArrayList<Point> neighbors;
    private int currentState;
    private int nextState;
    private int numStates = 6;
    
    public Point() {
            currentState = 0;
            nextState = 0;
            neighbors = new ArrayList<Point>();
    }

    public void drop() {
        if(Math.random() < 0.05) {
            nextState = 6;
        }
    }

    public void clicked() {
            currentState=(++currentState)%numStates;	
    }
    
    public int getState() {
            return currentState;
    }

    public void setState(int s) {
            currentState = s;
    }

    public void calculateNewState() {
        if(currentState > 0) {
            nextState = currentState -1;
        }
        if(currentState == 0 && neighbors.size() > 0 ) {
            if(neighbors.get(0).getState() > 0) {
                nextState = 6;
            }
        }
    }

    public void changeState() {
            currentState = nextState;
    }
    
    public void addNeighbor(Point nei) {
            neighbors.add(nei);
    }

    public long getLiveNeighborCount() {
        return neighbors.stream()
            .filter(pt -> pt.currentState == 1)
            .count();
    }
}
