import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.tokenize import sent_tokenize
from pymongo import MongoClient
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.LIVECHATDATABASE
mycal= db["Messages"]
c = 0
bien = 0
tmp1 ="1"
tmp2 ="2"
tam1 =""
tam2 =""
tam3=""
numberkey = 0
numberarr = 0
arr =[[]]
sa =""
def Sosanh(tongpos) :
    if tongpos > 0 :
        print ("pos")
    else :
        print ("neg")
        
#
def tong(arr) :
    tongpos = 0.0
    for i in arr :
        
        tongpos = tongpos + stmSentence(i)
        
    return tongpos
    
#
def stmSentence(str) :
    tongpos = 0.0
    zz = sent_tokenize(str)
    
    for i in zz :
        blod1 = TextBlob(i)
        tongpos = tongpos + blod1.sentiment.polarity
    
    return tongpos/len(zz)
for i in mycal.find() :
    stri = str(i)
    sang = stri.split(", '")
    for j in sang :
        sang1 = j.replace("'","")
        
        sang2 = sang1.split(":",1)
        
        if sang2[0] in "primary_key" :
            sa = sang2[1].strip()
            #print(sa)
        if sang2[0] in "textMessage" :
            tam1 = sang2[1].strip()
            #print(tam1)
        if sang2[0] in "sender_role" :
            oke = sang2[1].replace("}","")
            tam3 = oke.strip()
            #print(tam3)
        if sa not in "" and tam1 not in "" and tam3 not in "" :
            s = sa + " " + tam3 + " " + tam1
            bien = 0
            print(s)
            if len(arr) > 1 :
                #print(s)
                for i in range(len(arr)) :
                    if i < len(arr)-1 :
                        line = arr[i][0]
                        
                        linen = line.split(" ")
                            #print(linen[0])
                        if linen[0] in sa :
                                
                            arr[i].append(s)
                            sa = ""
                            tam1 =""
                            tam3 = ""
                            bien = 1
                            
                    if i == len(arr)-1  and bien == 0:
                        arr.append([])
                        arr[c].append(s)
                        c = c +1
                        sa = ""
                        tam1 =""
                        tam3 = ""
                        bien =0
            else :
                
                arr.append([])
                arr[c].append(s)
                c = c +1
                sa = ""
                tam1 =""
                tam3 = ""
for i in arr :
    print(i)
#tach file
for i in range(len(arr)-1) :
    tongpos = 0
    arrcus= []
    arrad=[]
    h1 = ""
    h2 =""
    tam1 =""
    tam2 =""
    
    for j  in range(len(arr[i])) :
        
        len2 = arr[i][j]
        tmp = arr[i][j].split(" ",2)
        h1 = tmp[1]
        h2 = tmp[2]
        if tmp[1] in "admin" :
            if tam1 in "" :
                tam1 = tmp[2].strip()
            else :
                tam1 = tam1.strip() + " . " + tmp[2]
            if tam2 not in "" :
                arrcus.append(tam2)
                tam2=""
            
        else :
            if tam2 in "" :
                tam2 = tmp[2].strip()
            else :
                tam2 = tam2.strip() + " . " + tmp[2]
            if tam1 not in "" :
                arrad.append(tam1)
                tam1 = ""
    if h1 in "admin" :
        arrad.append(h2)
    else :
        arrcus.append(h2)
        
    
    tongpos = tong(arrad) +tong(arrcus)*2
    
    print(i)
    print("Ket qua cuoi cung")
    Sosanh(tongpos)

    print(tongpos)

#QuangSang 31/7/2019
#fix readfile json
#QuangSang 5/8/2019
#fix readfile mongoDB
#QuangSang 7/8/2019
#error correction not received :

