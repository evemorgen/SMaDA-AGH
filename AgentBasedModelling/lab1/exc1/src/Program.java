import javax.swing.JFrame;

public class Program extends JFrame {

	private static final long serialVersionUID = 1L;
	private GUI gof;

	public Program() {
		setTitle("Game of Life");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		gof = new GUI(this);
		gof.initialize(this.getContentPane());

		this.setSize(800, 600);
		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Program();
	}

}
