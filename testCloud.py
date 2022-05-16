# -*- coding: utf-8 -*-
# @Time : 2022/5/16 3:04 下午
# @Author : 陆智超
# @File : testCloud.py
# @Software : PyCharm



import jieba                           # 分词
from matplotlib import pyplot as plt   # 绘图，数据可视化
from wordcloud import WordCloud        # 词云
from PIL import Image                  # 图片处理
import numpy as np                     # 矩阵运算
import sqlite3                         # 数据库


# 准备词云所需要的文字（词）
conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    # print(item[0])
    text = text + item[0]
# print(text)
cur.close()
conn.close()



# 分词
cut = jieba.cut(text)
string = " ".join(cut)
print(len(string))




img = Image.open('static/assets/img/img_ciyun.jpg')      # 打开遮罩图片
img_array = np.array(img)      # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask = img_array,
    font_path="Hiragino Sans GB.ttc"
)
wc.generate_from_text(string)




# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴

# plt.show()        # 显示生成的词云图片

# 输出词云图片到文件
plt.savefig('static/assets/img/word_ciyun.jpg',dpi=500)


