# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:44:07 2022

@author: cnhhdn
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]

times=0
cache_cryosleep = ""
cache_transported=""
cryo_disappear = 0
discryo_disappear = 0
cryo_stillhere = 0
discryo_stillhere = 0
path_train = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/train.csv"

with open(path_train) as file:  
    for line in file:
        data = line.split(",")
        cryosleep = data[2]
        transported = data[13]
        
        #跳过描述值
        if times==0:
            times= times+1
            print(cryosleep)
            continue
        if times==1:
            #令 cache_cryosleep = "false"
            cache_cryosleep = cryosleep
            cache_transported = transported
            times= times+1
        #说明未在休眠状态下
        if cryosleep==cache_cryosleep:
            #消失
            if transported != cache_transported:
                discryo_disappear+=1
            #未消失
            else:
                discryo_stillhere+=1
        #说明在休眠状态下  
        elif cryosleep==""  :
            continue
        else:
            #消失
            if transported != cache_transported:
                cryo_disappear+=1
            #未消失
            else:
                cryo_stillhere+=1
        
print(discryo_disappear)
#print(discryo_stillhere)
print(cryo_disappear)
#print(cryo_stillhere)
rate =[0,0]
allmember = discryo_disappear+discryo_stillhere+cryo_disappear+cryo_stillhere
discryo_member = discryo_disappear+discryo_stillhere
cryo_member = cryo_disappear+cryo_stillhere
rate[0]=discryo_disappear/discryo_member
rate[1]=cryo_disappear/cryo_member

x = ["未休眠","休眠"]
plt.bar(x,rate,align="center",color="rgb",hatch=" ",ec='gray')
plt.xlabel(u"是否休眠与消失概率关系")
plt.ylabel(u"消失概率/%")
plt.show()

















"""     
for i in range(family_count):
    print(family_number[i])"""  