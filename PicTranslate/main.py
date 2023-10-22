from PIL import Image, ImageDraw, ImageFont
from config import *
import requests
import random
import json
from hashlib import md5
from paddleocr import PaddleOCR, draw_ocr, PPStructure, save_structure_res
import math
import time
import tabula
import pandas as pd
import fitz
import os
# import office
import cv2
import flask
# from PyPDF2 import PdfReader, PdfWriter
from PyPDF4 import PdfFileReader, PdfFileWriter


'''
# pdf转换为图片
def pdf2image(pdfPath, imagePath):
    # office.pdf.pdf2imgs(pdf_path=pdfPath, out_dir=imagePath)
    office.pdf.pdf2docx(pdfPath, output_path='test.docx')
'''

# def getPdfStruct():
#     save_folder = './output'
#     img_path = './image/10.jpg'
#     table_engine = PPStructure(show_log=True)
#     image = cv2.imread(img_path)
#     result = table_engine(image)
#     save_structure_res(result, save_folder,
#                        os.path.basename(img_path).split('.')[0])

# 翻译pdf中的图片信息


@app.route('/translatePic', methods=["post"])
def translatePic():
    filepath = './1.png'
    # 打开图片
    img = Image.open(filepath)
    # 创建一个ImageDraw对象
    draw = ImageDraw.Draw(img)
    # 设置英文字体文件和大小
    # font = ImageFont.truetype("Arial.ttf", 10)

    # 利用百度paddleocr识别文字与其的坐标
    ocr = PaddleOCR(
        use_angle_cls=True, lang="ch"
    )  # need to run only once to download and load model into memory
    result = ocr.ocr(filepath, cls=True)

    # 构建句子字典
    sentence_dict = dict()
    index = 0
    for item in result[0]:
        # 判断是否为存数字，如果不是就翻译
        try:
            float(item[1][0])
        except ValueError:
            sentence_dict[str(index)] = {'sentence': '', 'location': []}
            sentence_dict[str(index)]['sentence'] = item[1][0]
            sentence_dict[str(index)]['location'].append(item[0][0][0])
            sentence_dict[str(index)]['location'].append(item[0][0][1])
            sentence_dict[str(index)]['location'].append(item[0][2][0])
            sentence_dict[str(index)]['location'].append(item[0][2][1])
            index += 1
    for key in sentence_dict.keys():
        # 绘制占位矩形
        draw.rectangle((sentence_dict[key]['location'][0],
                        sentence_dict[key]['location'][1],
                        sentence_dict[key]['location'][2],
                        sentence_dict[key]['location'][3]),
                       fill=(255, 255, 255))
        # 绘制文本
        draw.text((sentence_dict[key]['location'][0],
                   sentence_dict[key]['location'][1]),
                  chi2Eng(sentence_dict[key]['sentence']),
                  fill=(0, 0, 0))
        time.sleep(1)
    img.save("new_img.png")


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


# 调用百度翻译api接口
def chi2Eng(query):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'appid': appid,
        'q': query,
        'from': from_lan,
        'to': to_lan,
        'salt': salt,
        'sign': sign
    }
    r = requests.post(api_path, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]['dst']


# 翻译pdf中的其他部分
# def translateOtherWord():
#     # 打开一个PDF文件
#     pdf_reader = PdfFileReader(open("test.pdf", "rb"))
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(pdf_reader.getPage(15))

#     pdf_writer.removeText()
#     pdf_writer.write('output.pdf')

# pdf_writer.write("output.pdf")

if __name__ == '__main__':
    translatePic()
