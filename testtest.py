# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os

# importar o arquivo csv em um df
text_file = open("C:/Users/tar/Desktop/entrada.txt", "r")

#df = text_file.read().split(' ')


df = text_file.read()
all_summary= " ".join(s for s in df)


#print("Quantidade de Palavras: {}".format(len(df)))
stopwords = set(STOPWORDS)
stopwords.update(["Fato Sobre","relacionamento","BEM VINDOS","SEJAM BEM","pra","mim","removed","ao","Ao", "de", "era", "uma","para","por","da", "meu", "em", "voc�", "de", "os", "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "�", "com", "n�o", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ele", "das", "tem", "�", "seu", "sua", "ou", "ser", "quando", "muito", "h�", "nos", "j�", "est�", "eu", "tamb�m", "s�", "pelo", "pela", "at�", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", "ter", "seus", "quem", "nas", "me", "esse", "eles", "est�o", "voc�", "tinha", "foram", "essa", "num", "nem", "suas", "meu", "�s", "minha", "t�m", "numa", "pelos", "elas", "havia", "seja", "qual", "ser�", "n�s", "tenho", "lhe", "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", "voc�s", "vos", "lhes", "meus", "minhas","teu", "tua","teus","tuas","nosso", "nossa","nossos","nossas","dela", "delas", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou","est�","estamos","est�o","estive","esteve","estivemos","estiveram","estava", "est�vamos", "estavam", "estivera", "estiv�ramos", "esteja", "estejamos", "estejam", "estivesse", "estiv�ssemos", "estivessem", "estiver", "estivermos", "estiverem", "hei", "h�", "havemos", "h�o", "houve", "houvemos", "houveram", "houvera", "houv�ramos", "haja", "hajamos", "hajam", "houvesse", "houv�ssemos", "houvessem", "houver", "houvermos", "houverem", "houverei", "houver�", "houveremos", "houver�o", "houveria", "houver�amos", "houveriam", "sou", "somos", "s�o", "era", "�ramos", "eram", "fui", "foi", "fomos", "foram", "fora", "f�ramos", "seja", "sejamos", "sejam", "fosse", "f�ssemos", "fossem", "for", "formos", "forem", "serei", "ser�", "seremos", "ser�o", "seria", "ser�amos", "seriam", "tenho", "tem", "temos", "t�m", "tinha", "t�nhamos", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", "tiv�ramos", "tenha", "tenhamos", "tenham", "tivesse", "tiv�ssemos","tivessem","tiver","tivermos","tiverem","terei","ter�","teremos","ter�o","teria","ter�amos","teriam"])

#print(df)

# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1600, height=800).generate(df)
                      
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

plt.imshow(wordcloud);
wordcloud.to_file("C:/Users/tar/Desktop/whatsapp_summary_wordcloud.png")
os.startfile("C:/Users/tar/Desktop/whatsapp_summary_wordcloud.png")