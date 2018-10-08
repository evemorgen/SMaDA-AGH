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
        long count = getLiveNeighborCount();
        if(currentState == 0) {
            // cities
            nextState = count > 3 && count < 9 ? 1 : 0;
            // coral
            // nextState = count > 2 && count < 4 ? 1 : 0;

        } else {
            // cities
            nextState = count > 1 && count < 6 ? 1 : 0;
            // coral
            // nextState = count > 3 && count < 9 ? 1 : 0;
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
