import sqlite3
con=sqlite3.connect("veriyeni.db")
db=con.cursor()
cek=db.execute("SELECT * from yen")
listetarih=[]
listeopen=[]
listehigh=[]
listelow=[]
listeclose=[]
for i in cek:
    listetarih.append(i[4])
    listeopen.append(i[0])
    listehigh.append(i[2])
    listelow.append(i[3])
    listeclose.append(i[1])    
ema12liste=[] 
ema26liste=[]
macdliste=[]
signalliste=[]
histogramliste=[]
ema121=sum(listeclose[0:12])/12
ema261=sum(listeclose[0:26])/26
ema12liste.append(ema121)
ema26liste.append(ema261)


b=len(listeclose)
for i in range(0,b):                         
    #hareketli ortalama
    if (i+12)<b:
        ema12liste.append((listeclose[12+i])*(2/13)+ema12liste[i]*(1-(2/13)))
    if (i+26)<b:
        ema26liste.append((listeclose[26+i])*(2/27)+ema26liste[i]*(1-(2/27)))        
for j in range(0,len(ema26liste)):    
    macdliste.append(ema12liste[j+14]-ema26liste[j])
z=len(macdliste)-9
signalliste.append((sum(macdliste[0:9])/9))
for x in range(0,z):
    signalliste.append((macdliste[x+9]*(2/10)+(signalliste[0+x]*(1-(2/10)))))

for y in range(0,len(signalliste)):
    histogramliste.append(macdliste[8+y]-signalliste[y])
