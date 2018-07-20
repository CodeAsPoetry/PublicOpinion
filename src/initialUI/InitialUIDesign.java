package initialUI;

import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

@SuppressWarnings("serial")
public class InitialUIDesign extends JFrame {
	
	private JPanel jpanel_operate;
	private JPanel jpanel_input;
	private JPanel jpanel_info; 
	
	public void createUI() {
		this.setTitle("與情分析系统");
		this.setSize(1000, 600);
		this.setLocationRelativeTo(null);
		this.setResizable(false);
		this.setLayout(null);
		this.setDefaultCloseOperation(3);
		
		this.jpanel_operate = new JPanel();
		this.jpanel_input = new JPanel();
		this.jpanel_info = new JPanel();
		
		this.jpanel_operate.setPreferredSize(new Dimension(200,600));
		this.jpanel_operate.setBounds(0, 0, 200, 600);
		this.jpanel_operate.setBackground(Color.CYAN);
		
		this.jpanel_input.setPreferredSize(new Dimension(800,200));
		this.jpanel_input.setBounds(200,0,800,200);
		this.jpanel_input.setBackground(Color.YELLOW);
		
		this.jpanel_info.setPreferredSize(new Dimension(800,400));
		this.jpanel_info.setBounds(200,200,800,400);
		this.jpanel_info.setBackground(Color.BLUE);
		
		this.add(jpanel_operate);
		this.add(jpanel_input);
		this.add(jpanel_info);
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {

			public void run() {
				try {
					InitialUIDesign initUI = new InitialUIDesign();
					initUI.createUI();
					initUI.setVisible(true);
					
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			}
		});

	}


	

}
