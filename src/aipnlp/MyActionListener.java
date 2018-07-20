package aipnlp;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;

import javax.swing.JTextPane;

import org.json.JSONArray;
import org.json.JSONObject;

import com.baidu.aip.nlp.AipNlp;

public class MyActionListener implements ActionListener {
	
	private AipNlp client;
	private JTextPane jtextpane_chineseInput;
	private JTextPane jtextpane_resultInfo;
	
	private String[] words;
	private String str_input="";
	
	public MyActionListener(AipNlp client, JTextPane jtextpane_chineseInput, JTextPane jtextpane_resultInfo) {
		this.client = client;
		this.jtextpane_chineseInput = jtextpane_chineseInput;
		this.jtextpane_resultInfo = jtextpane_resultInfo;
		
	}


	public void actionPerformed(ActionEvent e) {
		this.str_input = jtextpane_chineseInput.getText();
		if(e.getActionCommand().equals("文本分词")) {
	
			HashMap<String, Object> options = new HashMap<String, Object>();
		    JSONObject res = client.lexer(str_input, options);		    
		    JSONArray items = (JSONArray)res.get("items");
		    words = new String[items.length()];
		    String info ="\n";
		    for(int i=0;i<items.length();i++) {
		    	JSONObject job = items.getJSONObject(i);
		    	info += (String) job.get("item")+" ";
		    }
		    
		    info+="\n";
		    jtextpane_resultInfo.setText(jtextpane_resultInfo.getText()+info);
		   
	    

		}
		
		if(e.getActionCommand().equals("词向量生成")) {
			 
			for(int i=0;i<words.length;i++) {
				HashMap<String, Object> options = new HashMap<String, Object>();
			    JSONObject res = client.wordEmbedding(words[i], options);	
			    System.out.print(res.toString());
			}
		}
		
		if(e.getActionCommand().equals("情绪识别")) {
			
		    HashMap<String, Object> options = new HashMap<String, Object>();
		    
		    JSONObject res = client.sentimentClassify(str_input, options);
		    JSONArray items = (JSONArray)res.get("items");
		    String info ="";
		    for(int j=0;j<items.length();j++) {
		    	JSONObject job = items.getJSONObject(j);
		    	info += " sentiment:"+job.get("sentiment").toString()+"\n positive_prob:"+job.get("positive_prob").toString()+"\n negative_prob:"+job.get("negative_prob").toString()+"\n confidence:"+job.get("confidence").toString()+"\n";
		    }
		    info = "\n [0:负向，1:中性，2:正向] \n"+ info;
		    jtextpane_resultInfo.setText(jtextpane_resultInfo.getText()+info);
		}

	}

}
