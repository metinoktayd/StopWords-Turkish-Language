import os

txt=open("turkish.txt","r")
stopwords=[]
for i in txt:
    i=i[0:-1]
    stopwords.append(i)