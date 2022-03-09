# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:44:07 2022

@author: cnhhdn
"""
import pandas as pd
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
#path_train = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/train.csv"
path_test = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/test.csv"
with open(path_test) as file:  
    for line in file:
        data = line.split(",")
        #transported = data[13]
        #提取家庭成员个数
        #跳过描述值
        if times==0:
            times= times+1
            #print(line[0:4])
            continue
        #将False存入cache_transported
        elif times==1:
            #cache_transported = transported
            #print(line[0:4])
            times= times+1
            last_family_name = line[0:4]
        
        #如果这个人消失了
        """
        if transported != cache_transported:
            flag_disappear = 1
        """    
        
        if last_family_name == line[0:4]:
            family_count+=1 
            #last_transported = false
            """if transported != cache_transported:
                flag_true+=1"""
          
        else:
            """if last_disappear != cache_transported:
                flag_true+=1  """
            family_member[family] = family_count
            family_transported[family] = flag_true
            flag_true=0
            last_family_name = line[0:4]
            family_count =1
            family +=1
        """last_disappear = transported"""
        flag_disappear=0
#print(family_member)        
#print(family_transported)
 
member_max = 8 #最大成员数       
members_transported = [0,0,0,0,0,0,0,0]
allmembers = [0,0,0,0,0,0,0,0]
belong_members = []
rate = [0,0,0,0,0,0,0,0]

for i in range(len(family_member)):
    if family_member[i]==1:
        for i in range(1):
            belong_members.append(1)
        
    if family_member[i]==2:
        for i in range(2):
            belong_members.append(2)
    if family_member[i]==3:
        for i in range(3):
            belong_members.append(3)
    if family_member[i]==4:
        for i in range(4):
            belong_members.append(4)
    if family_member[i]==5:
        for i in range(5):
            belong_members.append(5)
    if family_member[i]==6:
        for i in range(6):
            belong_members.append(6)
    if family_member[i]==7:
        for i in range(7):
            belong_members.append(7)
    if family_member[i]==8:
        for i in range(8):
            belong_members.append(8)
    
print(belong_members)


for i in range(1):
            belong_members.append(1)
sol=pd.read_csv(path_test)
sol.head()
sol['members']=belong_members
sol.head()
sol.to_csv('./data/test_members.csv',index=False)


















"""     
for i in range(family_count):
    print(family_number[i])"""  