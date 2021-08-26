# 用于带坐标系的绘图
from matplotlib import pyplot as plt
# 根据字符串的词语出现的评论生成频率
from wordcloud import WordCloud
# 对字符串进行识别分割
import jieba
# 图片处理常用库
from PIL import Image
# 数组和矩阵运算
import numpy as np
# sqllite处理数据库
import sqlite3

# 获取数据源
def get_data():
    """获取数据源"""
    conn = sqlite3.connect("movie.db")
    cursor = conn.cursor()
    sql = """select instruction from movie_250"""
    data = cursor.execute(sql)
    text = ""
    for item in data:
        text += item[0]
    cursor.close()
    conn.close()
    return text

# 对数据进行处理
def deal_data(text):
    """对数据进行处理"""
    # 对字符串进行切割分离词语,根据语境进行分割
    cut = jieba.cut(text)
    list1 = list(cut)
    s1 = ''
    # 过滤列表,根据需要过滤显示的字段
    list2 = ['的','人','是','了','你','我','和','电影','就是','都','让','一个','不','在','被','与','最','没有','要','才','这样',
             '就','有','没有','给','不是','不会','也','比','一种','一部','大','小']
    for item in list1:
        if item not in list2:
            s1 += item + ' '
    return s1

# 根据传入的图片和字符串,生成词云图片
def get_word_cloud(background_img,str,word_cloud_img):
    """根据传入的图片和字符串,生成词云图片"""
    img = Image.open(background_img)
    # 图片转化为数组
    ima_array = np.array(img)
    wc = WordCloud(
        background_color='white',
        # 背景图
        mask=ima_array,
        font_path="Songti.ttc"
    )
    # 生成词云
    wc.generate_from_text(str)
    # 绘制图片
    figure = plt.figure(figsize=(4,4),dpi=400)
    plt.imshow(wc)
    # 不显示坐标轴
    plt.axis('off')
    # 保存生成文件
    plt.savefig(word_cloud_img)
    # 显示词云图片
    plt.show()

def main():
    # 背景图片地址
    background_img = 'tree.png'
    # 生成的词云图片地址
    word_cloud_img = "word_cloud.jpg"
    # 数据源,只要是字符串即可,这里正好有上个项目的数据
    text = ""
    text = get_data()
    # print(text)
    str = deal_data(text)
    # print(str)
    get_word_cloud(background_img,str,word_cloud_img)

if __name__ == '__main__':
    main()