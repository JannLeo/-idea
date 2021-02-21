# -*- coding = utf-8 -*-
# @Time : 2021/2/20 14:46
# @Author : 刘俊楠
# @Fire : test_cloud.py
# @Software : PyCharm

import jieba   #分词
from wordcloud import Wordcloud     #词云
from matplotlib import pyplot as plt  #绘图，数据可视化
from PIL import Image  #图片处理
import numpy as np  #矩阵运算
import sqlite3  #数据库


con = sqlite3.connect('movie.db')
cur=con.cursor()
sql = 'select introduction from movie250'
data=cur.execute(sql)
for item in data:
    text=text+item[0]
