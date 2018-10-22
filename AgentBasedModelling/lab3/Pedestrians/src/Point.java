import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;
import java.util.stream.Collectors;

public class Point {

    public ArrayList<Point> neighbors;
    public static Integer []types ={0,1,2,3};
    public int type;
    public int staticField;
    public boolean isPedestrian;
    public boolean blocked;

    public Point() {
        type=0;
        staticField = 100000;
        neighbors= new ArrayList<Point>();
    }
    
    public void clear() {
        staticField = 100000;
        
    }

    public boolean calcStaticField() {
       return neighbors.stream()
            .map(p -> p.staticField)
            .min(Comparator.naturalOrder())
            .map(x -> x + 1)
            .filter(min -> min < staticField)
            .map(val -> staticField = val)
            .isPresent();
    }
    
    public void move(){
        if(isPedestrian && !blocked) {
            neighbors.stream()
                .filter(p -> p.type == 0)
                .min(Comparator.comparing(p -> p.staticField))
                .ifPresent(p -> {
                    if(p.type == 0) {
                        p.isPedestrian = true;
                        p.blocked = true;
                    }
                    this.isPedestrian = false;
                });
        }
    }

    public void addNeighbor(Point nei) {
        neighbors.add(nei);
    }
}
