import java.awt.FlowLayout;	//how things are placed
import javax.swing.JFrame; //basic window
import javax.swing.JLabel;

public class GUI extends JFrame{
	private JLabel item1;
	
	public GUI(){
		super("the title bar");
		setLayout(new FlowLayout());
		
		item1 = new JLabel("this is a thing ");
		item1.setToolTipText("This is gonna show up on hover");
		add(item1);
		
	}
}
