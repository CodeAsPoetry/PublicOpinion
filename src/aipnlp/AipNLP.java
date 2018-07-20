package aipnlp;

import com.baidu.aip.nlp.AipNlp;

public class AipNLP {
	
	public static final String APP_ID = "10909192";
    public static final String API_KEY = "j3A4pypCDzWkcUexTESmB5zm";
    public static final String SECRET_KEY = "UouaOSXsare7m392YVQodt2wprELH0Ai";
    
    private static AipNlp client =null;
    
	static{
		client = new AipNlp(APP_ID, API_KEY, SECRET_KEY);
	}
	
	public static AipNlp getClent(){
		return client;
	}


}
