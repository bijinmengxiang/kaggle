# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:44:07 2022

@author: cnhhdn
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"]=["SimHei"]
family = 0
family_count = 0 #家庭成员数量临时变量
family_member = {} #家庭成员数量
family_transported = {}  #家庭编号
last_family_name = ""
times=0
flag_true = 0
flag_disappear = 0
#flag_disappear = 0
last_disappear = ""
path_train = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/train.csv"
path_test = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/test.csv"
with open(path_train) as file:  
    for line in file:
        data = line.split(",")
        transported = data[13]
        #提取家庭成员个数
        #跳过描述值
        if times==0:
            times= times+1
            #print(line[0:4])
            continue
        #将False存入cache_transported
        elif times==1:
            cache_transported = transported
            #print(line[0:4])
            times= times+1
            last_family_name = line[0:4]
        
        #如果这个人消失了
        if transported != cache_transported:
            flag_disappear = 1
            
        
        if last_family_name == line[0:4]:
            family_count+=1 
            #last_transported = false
            if transported != cache_transported:
                flag_true+=1
          
        else:
            if last_disappear != cache_transported:
                flag_true+=1  
            family_member[family] = family_count
            family_transported[family] = flag_true
            flag_true=0
            last_family_name = line[0:4]
            family_count =1
            family +=1
        last_disappear = transported
        flag_disappear=0
#print(family_member)        
#print(family_transported)
 
member_max = 8 #最大成员数       
members_transported = [0,0,0,0,0,0,0,0]
allmembers = [0,0,0,0,0,0,0,0]
rate = [0,0,0,0,0,0,0,0]

for i in range(len(family_member)):
    if family_member[i]==1:
        allmembers[0]+=1
        members_transported[0]+=family_transported[i]
    if family_member[i]==2:
        allmembers[1]+=2
        members_transported[1]+=family_transported[i]
    if family_member[i]==3:
        allmembers[2]+=3
        members_transported[2]+=family_transported[i]
    if family_member[i]==4:
        allmembers[3]+=4
        members_transported[3]+=family_transported[i]
    if family_member[i]==5:
        allmembers[4]+=5
        members_transported[4]+=family_transported[i]
    if family_member[i]==6:
        allmembers[5]+=6
        members_transported[5]+=family_transported[i]
    if family_member[i]==7:
        allmembers[6]+=7
        members_transported[6]+=family_transported[i]
    if family_member[i]==8:
        allmembers[7]+=8
        members_transported[7]+=family_transported[i]
    
print(allmembers)
print(members_transported)
for i in range(8):
    rate[i] = members_transported[i]/allmembers[i]
print(rate)
x = range(1,9)
plt.bar(x,rate,align="center",color="rgb",hatch=" ",ec='gray')
plt.xlabel(u"团队包含人数")
plt.ylabel(u"消失概率/%")
plt.show()

















"""     
for i in range(family_count):
    print(family_number[i])"""  