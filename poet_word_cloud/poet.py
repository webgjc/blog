#coding:utf-8
#python3.5
#引入库文件
from wordcloud import WordCloud
import jieba
ss=""
f=open('poetry.txt',encoding='utf-8')
#读取每首诗并去掉标题
#进行分词并存储
for i in f.readlines():
    l=i[i.find(':')+1:-1]
    s=jieba.cut(l,cut_all=False)
    for j in s:
        if j==':' or j=='，' or j=='。':
            continue
        else:
            ss+=j+" "
print("finish read poet txt")
#引入中文字体文件
font="C:/Windows/Fonts/simfang.ttf"
#构建词云并保存
#如需展示的话可以用matplotlib，具体可以看wordcloud文档
word=WordCloud(width=4000,height=2000,font_path=font,max_words=2000,max_font_size=500).generate(ss)
word.to_file('filename.png')
print("finish word cloud")