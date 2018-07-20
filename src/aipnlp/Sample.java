package aipnlp;

import java.util.HashMap;

import org.json.JSONObject;

import com.baidu.aip.nlp.AipNlp;

public class Sample {
    //设置APPID/AK/SK
    public static final String APP_ID = "10909192";
    public static final String API_KEY = "j3A4pypCDzWkcUexTESmB5zm";
    public static final String SECRET_KEY = "UouaOSXsare7m392YVQodt2wprELH0Ai";

    public static void main(String[] args) {
        // 初始化一个AipNlp
        AipNlp client = new AipNlp(APP_ID, API_KEY, SECRET_KEY);

        // 调用接口
//        String text = "苹果是一家伟大的公司";
        String text = "二营长，你他娘的意大利...面给友军端上来尝尝。"; 
        // 传入可选参数调用接口
        HashMap<String, Object> options = new HashMap<String, Object>();
        
        // 情感倾向分析
        JSONObject res = client.sentimentClassify(text, options);
        System.out.println(res.toString(2));
        // "sentiment": 表示情感极性分类结果, 0:负向，1:中性，2:正向
        //"confidence": 表示分类的置信度
    }
}
