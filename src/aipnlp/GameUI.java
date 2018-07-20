package aipnlp;

import java.awt.Dimension;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.ScrollPaneConstants;

import com.baidu.aip.nlp.AipNlp;

public class GameUI {
	
	private JFrame jframe;
	
	private JPanel jpanel_operate;
	private JPanel jpanel_input;
	private JPanel jpanel_info; 
	
	private JButton jbu_split;
	private JButton jbu_vec;
	private JButton jbu_recognize;
	
	private JTextPane jtextpane_chineseInput;
	private JLabel jlabel_chineseInput;
	
	private JTextPane jtextpane_resultInfo;
	private JLabel jlabel_resultInfo;
	
	public void createUI() {
		AipNlp client = AipNLP.getClent();
		this.jframe = new JFrame();
		this.jframe.setTitle("情绪识别可视化");
		this.jframe.setSize(800,600);
		this.jframe.setResizable(false);
		this.jframe.setLocationRelativeTo(null);
		this.jframe.setLayout(null);
		this.jframe.setDefaultCloseOperation(3);
		
		
		this.jpanel_operate = new JPanel();
		this.jpanel_input = new JPanel();
		this.jpanel_info = new JPanel();
		
		this.jpanel_operate.setPreferredSize(new Dimension(200,600));
		this.jpanel_operate.setBounds(0, 0, 200, 600);
		
		this.jpanel_input.setPreferredSize(new Dimension(600,200));
		this.jpanel_input.setBounds(200,0,600,200);
		
		this.jpanel_info.setPreferredSize(new Dimension(600,400));
		this.jpanel_info.setBounds(200,200,600,400);
		
		this.jframe.add(jpanel_operate);
		this.jframe.add(jpanel_input);
		this.jframe.add(jpanel_info);
		
		
		this.jbu_split = new JButton("文本分词");
		this.jbu_split.setPreferredSize(new Dimension(120,30));
		this.jbu_split.setBounds(40,20,120,30);
		
		
		this.jbu_vec = new JButton("词向量生成");
		this.jbu_vec.setPreferredSize(new Dimension(120,30));
		this.jbu_vec.setBounds(40,70,120,30);
		
		
		this.jbu_recognize = new JButton("情绪识别");
		this.jbu_recognize.setPreferredSize(new Dimension(120,30));
		this.jbu_recognize.setBounds(40,120,120,30);
		
		
		this.jpanel_operate.setLayout(null);
		this.jpanel_operate.add(jbu_split);
		this.jpanel_operate.add(jbu_vec);
		this.jpanel_operate.add(jbu_recognize);
		
		
		int v= ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS;//总显示垂直滚动条
		int h= ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS;//总显示水平滚动条
		
		this.jlabel_chineseInput = new JLabel("中文文本输入");
		this.jlabel_chineseInput.setPreferredSize(new Dimension(80,30));
		this.jlabel_chineseInput.setBounds(10, 10, 80, 30);
		
		this.jtextpane_chineseInput = new JTextPane();
		this.jtextpane_chineseInput.setFont(new Font("黑体",Font.BOLD,16));
		JScrollPane sp_chineseInput = new JScrollPane(this.jtextpane_chineseInput,v,h);
		sp_chineseInput.setPreferredSize(new Dimension(580,150));
		sp_chineseInput.setBounds(10, 40, 580, 150);
		
		
		this.jpanel_input.setLayout(null);
		this.jpanel_input.add(jlabel_chineseInput);
		this.jpanel_input.add(sp_chineseInput);
		
		
		
		this.jlabel_resultInfo = new JLabel("处理结果显示");
		this.jlabel_resultInfo.setPreferredSize(new Dimension(80,30));
		this.jlabel_resultInfo.setBounds(10,10,80,30);
		
		this.jtextpane_resultInfo = new JTextPane();
		this.jtextpane_resultInfo.setEditable(false);
		this.jtextpane_resultInfo.setFont(new Font("黑体",Font.BOLD,16));
		JScrollPane sp_resultInfo = new JScrollPane(this.jtextpane_resultInfo,v,h);
		sp_resultInfo.setPreferredSize(new Dimension(580,350));
		sp_resultInfo.setBounds(10, 40, 580, 350);
		
		this.jpanel_info.setLayout(null);
		this.jpanel_info.add(sp_resultInfo);
		this.jpanel_info.add(jlabel_resultInfo);
		
		MyActionListener mylistener = new MyActionListener(client,this.jtextpane_chineseInput,this.jtextpane_resultInfo);
		this.jbu_split.addActionListener(mylistener);
		this.jbu_vec.addActionListener(mylistener);
		this.jbu_recognize.addActionListener(mylistener);
		
		this.jframe.setVisible(true);
	}

	public static void main(String[] args) {
		GameUI gameUI = new GameUI();
		gameUI.createUI();
	}

}
