import BaiduTranslate.TransApi;
import org.apache.poi.xwpf.usermodel.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.List;
import java.util.Properties;

public class Test {

    public static void main(String[] args) throws Exception {

        Properties pro=new Properties();
        //读取配置文件
        pro.load(new FileInputStream("src/baidu.properties"));
        String appkey=pro.getProperty("appkey");
        String appid=pro.getProperty("appid");
        String from=pro.getProperty("from");
        String to=pro.getProperty("to");
        //百度翻译接口
        TransApi api=new TransApi(appid,appkey);
        // 读取docx文件
        XWPFDocument document = new XWPFDocument(new FileInputStream("src\\test.docx"));
        // 遍历表格
        List<XWPFTable> tables = document.getTables();
//            for (XWPFTable table : tables) {
                XWPFTable table = tables.get(0);
                for (XWPFTableRow row : table.getRows()) {
                    for (XWPFTableCell cell : row.getTableCells()) {
                        // 遍历单元格中的段落
                        for (XWPFParagraph paragraph : cell.getParagraphs()) {
                            // 遍历段落中的文本片段
                            for (XWPFRun run : paragraph.getRuns()) {
                                // 获取文本片段的内容
                                String text = run.getText(0);
                                if(containsChineseCharacters(text)) {
                                    String translate_text = api.getTransResult(text, from, to);
                                    run.setText(translate_text,0);
                                    //降低接口访问频率（因为是免费的）
                                    Thread.sleep(1000);
                                }
                            }
                        }
                    }
                }
            document.write(new FileOutputStream("src\\test_1.docx"));
    }


    //判断是否含有中文
    public static boolean containsChineseCharacters(String str) {
        if (str == null) {
            return false;
        }
        String regex = "[\u4e00-\u9fa5]+";
        return str.matches(".*" + regex + ".*");
    }
}
