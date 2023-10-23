# 目前进度(图片翻译+表格翻译)

## 1.图片翻译

图片翻译的Api在<font size=3 color="red">**PicTranslate/main.py**</font>里面

![image-20231022200533577](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/1.png)

如果更换需要翻译的图片直接修改filepath就行

![1](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/2.png)

然后这里并没有写成请求的形式，如果以后要作集成，可以使用flask框架，如下：

```python
@app.route('/translatePic',methods=["post"])
def translatePic():
    filepath = './1.png'
    # 打开图片
    img = Image.open(filepath)
    # 创建一个ImageDraw对象
    draw = ImageDraw.Draw(img)
    pass
```

### 翻译前后比对

#### 图片翻译前

![3](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/3.png)

#### 图片翻译后

![new_img](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/new_img.png)

## 2.表格翻译

表格翻译的Api在<font size=3 color="red">**TableTranslate/docx_s/src/Test.java**</font>里面

![image-20231022203914068](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/4.png)

### 表格翻译前后比对

#### 表格翻译前

![table_after](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/table_before.png)

#### 表格翻译后

![table_before](https://wsystorage-1316338016.cos.ap-nanjing.myqcloud.com/instruction/table_after.png)