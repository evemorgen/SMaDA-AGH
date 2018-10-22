import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

public class Point {

    public ArrayList<Point> neighbors;
    public static Integer []types ={0,1,2,3};
    public int type;
    public int staticField;
    public boolean isPedestrian;

    public Point() {
        type=0;
        staticField = 100000;
        neighbors= new ArrayList<Point>();
    }
    
    public void clear() {
        staticField = 100000;
        
    }

    public boolean calcStaticField() {
        int min_value = Collections.min(neighbors, Comparator.comparing(s -> s.staticField)).staticField + 1;
        if(staticField > min_value) {
            staticField = min_value;
            return true;
        }
        return false;
    }
    
    public void move(){
    }

    public void addNeighbor(Point nei) {
        neighbors.add(nei);
    }
}
