import streamlit as st
import sqlite3
import datetime
import pandas as pd
import numpy as np
import os

#su-anki-zaman
date=datetime.datetime.now()

#sql-olusturma
conn=sqlite3.connect("stopwords.sqlite3")
c=conn.cursor()
conn.commit()

#tüm-stopwords
all_stopwords=["ona", "olup", "ettiğini", "olduklarını", "mı", "dan", "nedenle", "niçin", "birçoğu", "itibaren",
               "ye", "sizi", "madem", "bütün", "bile", "buna", "bir", "ta", "orada", "şöyle", "o", "kendine",
               "yaptığını", "artık", "nın", "mü", "ya", "bize", "herkes", "bin", "hep", "e", "asla", "kadar",
               "oldu", "bey", "elbette", "ondan", "onun", "ediliyor", "nerede", "şeye", "a", "sonra", "zaten",
               "oysa", "birşey", "onları", "mu", "ü", "onlari", "ı", "biri", "sekiz", "olmadı", "bundan",
               "ayrıca", "şekilde", "vardı", "milyon", "her", "ötürü", "biraz", "altı", "falan", "benim",
               "itibariyle", "milyar", "yüz", "hem", "bunun", "beyler", "sanki", "edecek", "henüz", "ama",
               "nasıl", "tarafından", "yu", "için", "şunları", "kimisi", "nün", "arada", "şimdi", "yerine",
               "onlardan", "kendini", "birçok", "kaç", "olsa", "ediyor", "gereği", "yaptığı", "onlara", "u",
               "karşın", "kim", "hangi", "edilecek", "kimin", "herkesin", "olmak", "önce", "ise", "birşeyi",
               "bizi", "daha", "diye", "lakin", "bu", "altmış", "böylece", "hiç", "filan", "yirmi", "olarak",
               "yapılan", "seksen", "herkese", "kendilerine", "dolayısıyla", "beyden", "göre", "kimse", "gerek",
               "yani", "nerde", "şunu", "hangisi", "gene", "üzere", "bunları", "olmayan", "zira", "beş",
               "yapıyor", "katrilyon", "burada", "dahi", "tamam", "trilyon", "ki", "çok", "bilhassa", "var",
               "dolayı", "yapmak", "onu", "kez", "diğerleri", "öbür", "de", "ve", "bazen", "kendisine", "benden",
               "hatta", "şayet", "kimi", "olması", "olursa", "dokuz", "nereye", "olur", "ettiği", "bazıları", "ederek",
               "şu", "yoksa", "şey", "niye", "böyle", "veya", "kimden", "kendisini", "kırk", "onlar", "iki",
               "bunlar", "çoğu", "halen", "hiçbir", "kendisi", "neyse", "şeyler", "bazı", "neden", "yapılması",
               "beni", "senden", "birkez", "yaptı", "hani", "hiçbiri", "edilmesi", "yapacak", "yedi", "bunda",
               "etmesi", "bizden", "eden", "eğer", "pek", "ancak", "yi", "da", "olduğunu", "hala", "dört",
               "elli", "senin", "sen", "işte", "en", "şuna", "nun", "sizin", "acaba", "herhangi", "az", "tabii",
               "hepsi", "diğer", "sizden", "siz", "olan", "şeyi", "olmaz", "bunu", "kendi", "olmadığı", "ne", "öte",
               "herkesi", "şeyden", "fakat", "doksan", "on", "etti", "diğeri", "i", "tamamen", "defa", "belki",
               "bunların", "ile", "gibi", "size", "çünkü", "bizim", "kime", "yı", "birisi", "yetmiş", "halde",
               "seni", "otuz", "birkaç", "aslında", "bana", "ilgili", "ön", "çoğunu", "üç", "onların", "oluyor",
               "un", "beri", "ben", "tüm", "içinde", "değil", "nin", "olduğu", "biz", "öyle", "olsun", "sana",
               "tam", "tümü", "ün", "yaptıkları", "rağmen", "yine", "mi"]


#yeni-kelimeleri-ekleme
c.execute("CREATE TABLE IF NOT EXISTS eklenenkelimeler(kelime TEXT,tarih TEXT)")
conn.commit()
st.subheader("Kelime Ekleme")
kelimeekle=st.text_area("Girilecek Yeni Kelimeleri virgül koyarak bitişik bir biçimde yazın.",placeholder="racon,kesmiyorum,kafa,kesiyorum")
btn=st.button("Kelimeleri Ekle")
if btn:
    kelimeekle=kelimeekle.split(",")
    for kelimeeklefor in kelimeekle:
        if kelimeeklefor in all_stopwords:
            st.write(f":red[Bu kelime zaten var:] :green[{kelimeeklefor}]")
        elif kelimeeklefor not in all_stopwords:
            all_stopwords.append(kelimeeklefor)
            st.write(f":red[Eklenen Kelime:] :green[{kelimeeklefor}]")
            c.execute("INSERT INTO eklenenkelimeler VALUES(?,?)",(kelimeeklefor,date))
            conn.commit()

#tekrar-eden-kelimeleri-silme
stopwords = list(set(all_stopwords))


#kelime-silme
c.execute("CREATE TABLE IF NOT EXISTS silinenkelimeler(kelime TEXT,tarih TEXT)")
conn.commit()
st.subheader("Kelime Silme")
kelimesil=st.text_area("Silinecek Kelimeleri virgül koyarak bitişik bir biçimde yazın.",placeholder="bir,haftamız,var")
btndel=st.button("Kelimeleri Sil")
if btndel:
    kelimesil=kelimesil.split(",")
    for kelimesilfor in kelimesil:
        if kelimesilfor in stopwords:
            st.write(f":red[Silinen Kelime:] :green[{kelimesilfor}]")
            stopwords.remove(kelimesilfor)
            c.execute("INSERT INTO silinenkelimeler VALUES(?,?)", (kelimesilfor, date))
            conn.commit()
        elif kelimesilfor not in stopwords:
            st.write(f":red[Böyle Bir Kelime Bulunamadı:] :green[{kelimesilfor}]")


#stopwords
st.subheader("Kelimeler")
st.write(stopwords)

#txt-guncelleme
os.remove("turkish.txt")
stopwordssql=""
expander=st.expander("Kelimeler")
for txt in stopwords:
    ekle=open("turkish.txt","a")
    ekle.write(txt+"\n")
    expander.write(f":green[{txt}]")
    #st.write(f":red[{txt}]")
    stopwordssql=stopwordssql+", "+txt
st.write(stopwordssql[1:])

#stopwords-sql-ekleme
c.execute("CREATE TABLE IF NOT EXISTS stopwords(stopwords TEXT, tarih TEXT)")
c.execute("INSERT INTO stopwords VALUES(?,?)",(stopwordssql[2:],date))
conn.commit()













