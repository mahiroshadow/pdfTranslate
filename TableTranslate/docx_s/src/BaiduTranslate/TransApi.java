package BaiduTranslate;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import java.util.HashMap;
import java.util.Map;

public class TransApi {
    private static final String TRANS_API_HOST = "http://api.fanyi.baidu.com/api/trans/vip/translate";

    private String appid;
    private String securityKey;

    public TransApi(String appid, String securityKey) {
        this.appid = appid;
        this.securityKey = securityKey;
    }

//    {"from":"zh","to":"en","trans_result":[{"src":"\u7ed3\u675f\u65e5\u671f","dst":"End date"}]}

    public String getTransResult(String query, String from, String to) {
        Map<String, String> params = buildParams(query, from, to);
        String resJson=HttpGet.get(TRANS_API_HOST, params);
        JSONObject res=JSONObject.parseObject(resJson);
        String resTrans=JSON.parseArray(res.getString("trans_result")).getJSONObject(0).getString("dst");
        return resTrans;
    }

    private Map<String, String> buildParams(String query, String from, String to) {
        Map<String, String> params = new HashMap<String, String>();
        params.put("q", query);
        params.put("from", from);
        params.put("to", to);

        params.put("appid", appid);

        // 随机数
        String salt = String.valueOf(System.currentTimeMillis());
        params.put("salt", salt);

        // 签名
        String src = appid + query + salt + securityKey; // 加密前的原文
        params.put("sign", MD5.md5(src));

        return params;
    }

}
