# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:44:07 2022

@author: cnhhdn
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]

times=0
Earth_member = 0
Europa_member = 0
Mars_member = 0
Earth_transported = 0
Europa_transported = 0
Mars_transported = 0

path_train = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/train.csv"

with open(path_train) as file:  
    for line in file:
        data = line.split(",")
        homeplanet = data[4]
        transported = data[13]
        
        #跳过描述值
        if times==0:
            times= times+1
            #print(homeplanet)
            continue
        elif times==1:
            cache_transported = transported
            times= times+1
        
        if homeplanet=="TRAPPIST-1e":
            Earth_member+=1
            if transported!=cache_transported:
                Earth_transported+=1
                
        elif homeplanet=="PSO J318.5-22":
            Europa_member+=1
            if transported!=cache_transported:
                Europa_transported+=1
                
        elif homeplanet=="55 Cancri e":
            Mars_member+=1
            if transported!=cache_transported:
                Mars_transported+=1
            

        
rate = [0,0,0]   
rate[0]=Earth_transported/Earth_member  
rate[1]=Europa_transported/Europa_member  
rate[2]=Mars_transported/Mars_member  
print(rate)
x = ["TRAPPIST-1e","PSO J318.5-22","55 Cancri e"]
plt.bar(x,rate,align="center",color="rgb",hatch=" ",ec='gray')
plt.xlabel(u"母星与消失概率关系")
plt.ylabel(u"消失概率/%")
plt.show()

















"""     
for i in range(family_count):
    print(family_number[i])"""  