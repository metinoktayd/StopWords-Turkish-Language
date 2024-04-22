import streamlit as st
import sqlite3
import datetime
import pandas as pd
import numpy as np

#su-anki-zaman
date=datetime.datetime.now()

#sql-olusturma
conn=sqlite3.connect("stopwords.sqlite3")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stopwordssql(stopwords TEXT,date TEXT)")
conn.commit()

#tüm-stopwords
all_stopwords=["mu","onlar","seksen","ama","trilyon","buna",
              "bizim","beyden","yirmi","iki","seni","doksan","dört","bunun",
              "ki","nereye","hem","milyon","kez","otuz","elli","bizi","da","sekiz",
              "ve","çok","bu","veya","ya","onların","ona","bana","yetmiş","milyar",
              "senden","birşeyi","dokuz","yani","kimi","beyler","kim","neden","senin",
              "yedi","niye","üç","bey","mi","tüm","onlari","bunda","ise","hep","buna","bin","ben",
              "ondan","kimden","belki","ne","bundan","gibi","de","onlardan","sizi","sizin",
              "daha","niçin","bunda","bunu","beni","ile","bu","sizden","defa","biz","için","dahi",
              "siz","nerde","kime","birşey","birkez","her","biri","on","mü","diye","acaba","sen","en",
              "hepsi","bir","bizden","sanki","benim","nerede","onu","benden","yüz","birkaç","çünkü","nasıl",
              "hiç","katrilyon","fakat","lakin","ancak","acaba","ama","aslında","az","bazı","belki",
              "biri","birkaç","birşey","biz","bu","çok","çünkü","da","daha","de","defa","diye",
              "eğer","en","gibi","hem","hep","hepsi","her","hiç","için","ile","ise","kez","ki",
              "kim","mı","mu","mü","nasıl","ne","neden","nerde","nerede","nereye","niçin","niye",
              "o","sanki","şey","siz","şu","tüm","ve","veya","ya","yani","nereye","a","acaba","altı","altmış",
              "ama","ancak","arada","artık","asla","aslında","aslında","ayrıca","az","bana","bazen","bazı","bazıları",
              "belki","ben","benden","beni","benim","beri","beş","bile","bilhassa","bin","bir","biraz","birçoğu","birçok",
              "biri","birisi","birkaç","birşey","biz","bizden","bize","bizi","bizim","böyle","böylece","bu","buna","bunda",
              "bundan","bunlar","bunları","bunların","bunu","bunun","burada","bütün","çoğu","çoğunu","çok","çünkü","da","daha",
              "dahi","dan","de","defa","değil","diğer","diğeri","diğerleri","diye","doksan","dokuz","dolayı","dolayısıyla","dört",
              "e","edecek","eden","ederek","edilecek","ediliyor","edilmesi","ediyor","eğer","elbette","elli","en","etmesi","etti",
              "ettiği","ettiğini","fakat","falan","filan","gene","gereği","gerek","gibi","göre","hala","halde","halen","hangi",
              "hangisi","hani","hatta","hem","henüz","hep","hepsi","her","herhangi","herkes","herkese","herkesi","herkesin",
              "hiç","hiçbir","hiçbiri","i","ı","için","içinde","iki","ile","ilgili","ise","işte","itibaren","itibariyle",
              "kaç","kadar","karşın","kendi","kendilerine","kendine","kendini","kendisi","kendisine","kendisini","kez",
              "ki","kim","kime","kimi","kimin","kimisi","kimse","kırk","madem","mi","mı","milyar","milyon","mu","mü",
              "nasıl","ne","neden","nedenle","nerde","nerede","nereye","neyse","niçin","nin","nın","niye","nun","nün",
              "o","öbür","olan","olarak","oldu","olduğu","olduğunu","olduklarını","olmadı","olmadığı","olmak","olması",
              "olmayan","olmaz","olsa","olsun","olup","olur","olur","olursa","oluyor","on","ön","ona","önce","ondan",
              "onlar","onlara","onlardan","onları","onların","onu","onun","orada","öte","ötürü","otuz","öyle","oysa",
              "pek","rağmen","sana","sanki","sanki","şayet","şekilde","sekiz","seksen","sen","senden","seni","senin",
              "şey","şeyden","şeye","şeyi","şeyler","şimdi","siz","siz","sizden","sizden","size","sizi","sizi","sizin",
              "sizin","sonra","şöyle","şu","şuna","şunları","şunu","ta","tabii","tam","tamam","tamamen","tarafından",
              "trilyon","tüm","tümü","u","ü","üç","un","ün","üzere","var","vardı","ve","veya","ya","yani","yapacak",
              "yapılan","yapılması","yapıyor","yapmak","yaptı","yaptığı","yaptığını","yaptıkları","ye","yedi","yerine",
              "yetmiş","yi","yı","yine","yirmi","yoksa","yu","yüz","zaten","zira"]


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



#kelime-silme
c.execute("CREATE TABLE IF NOT EXISTS silinenkelimeler(kelime TEXT,tarih TEXT)")
conn.commit()
st.subheader("Kelime Silme")
kelimesil=st.text_area("Silinecek Kelimeleri virgül koyarak bitişik bir biçimde yazın.",placeholder="bir,haftamız,var")
btndel=st.button("Kelimeleri Sil")
if btndel:
    kelimesil=kelimesil.split(",")
    for kelimesilfor in kelimesil:
        if kelimesilfor in all_stopwords:
            st.write(f":red[Silinen Kelime:] :green[{kelimesilfor}]")
            all_stopwords.remove(kelimesilfor)
            c.execute("INSERT INTO silinenkelimeler VALUES(?,?)", (kelimesilfor, date))
            conn.commit()
        elif kelimesilfor not in all_stopwords:
            st.write(f":red[Böyle Bir Kelime Bulunamadı:] :green[{kelimesilfor}]")


#tekrar-eden-kelimeleri-silme
stopwords = list(set(all_stopwords))

#stopwords
st.subheader("Kelimelerin Son Hali (Array Olarak)")
st.write(stopwords)

#kelimeleri-ekrana-yazdirma
kelimegor=""
for kelimegorfor in stopwords:
    kelimegor=kelimegor+", "+kelimegorfor
kelimegor=kelimegor[1:]

#veri-tabanina-kayit-etme
c.execute("INSERT INTO stopwordssql VALUES(?,?)",(kelimegor[1:],date))
c.execute("SELECT * FROM stopwordssql")
stopwordssql=c.fetchall()
conn.commit()

st.subheader("Kelimelerin Son Hali (Sql Olarak)")
st.table(stopwordssql[-1])










