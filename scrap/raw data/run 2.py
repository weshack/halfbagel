import os
from scrap import scrap
print os.getcwd()
f=open('links.txt','r')
c=f.read()
f2=open('data2.json','w')
d=c.split('\n')
d=d[:-1]
bigj=[]
for link in d:
        link='http://www.wesleyan.edu/reslife/'+link[3:]
        print link
        json=scrap(link)
        bigj.append(json)
f2.write(str(bigj))
f2.close()
f.close()
  
