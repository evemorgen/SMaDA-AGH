public class Point {

	public Point nNeighbor;
	public Point wNeighbor;
	public Point eNeighbor;
	public Point sNeighbor;
	public float nVel;
	public float eVel;
	public float wVel;
	public float sVel;
	public float pressure;
        public static Integer []types ={0,1,2};
        public int type;

	public Point() {
		clear();
                type = 0;
	}

	public void clicked() {
		pressure = 1;
	}
	
	public void clear() {
		// TODO: clear velocity and pressure
            nVel = eVel = wVel = sVel = pressure = type = 0;
	}

	public void updateVelocity() {
		// TODO: velocity update
            nVel = nVel - (nNeighbor.pressure - pressure);
            wVel = wVel - (wNeighbor.pressure - pressure);
            eVel = eVel - (eNeighbor.pressure - pressure);
            sVel = sVel - (sNeighbor.pressure - pressure);
	}

	public void updatePresure() {
		// TODO: pressure update
            pressure = pressure - (float)(0.5)*(nVel + wVel + eVel + sVel);
	}

	public float getPressure() {
		return pressure;
	}
}
