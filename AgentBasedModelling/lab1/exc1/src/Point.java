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
        if(currentState == 0) {
            nextState = getLiveNeighborCount() == 3 ? 1 : 0;
        } else {
            nextState = getLiveNeighborCount() == 3 || getLiveNeighborCount() == 2 ? 1 : 0;
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
