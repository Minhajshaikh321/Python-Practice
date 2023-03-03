from typing import Dict


count=0
f=open("Chemistry.txt","r")
f2=open("chemistrymod.txt","w")
for x in f:
    c=x.replace(" ","_").strip()
    count+=1
    d=c + "=" + str(count)
    f2.write(d+"\n")
a=dict