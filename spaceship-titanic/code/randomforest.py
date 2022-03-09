from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
    
# Load data
path_train = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/trainCHVD.csv"
path_test = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/testCHVD.csv"
data = pd.read_csv(path_train) 
test_data = pd.read_csv(path_test) 

# 删除缺少值的那一行
data = data.dropna(axis=0)
# Choose target and features
y = data.Transported
features = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck']
#features = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck','members']
X = data[features]

test_feature = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck']
#test_feature = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck','members']
test = test_data[test_feature]

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(X, y)
preds = forest_model.predict(test)

all_transported=[]
for i in range(len(preds)):
    print(preds[i])
    if preds[i]>0.5:
            all_transported.append(True)        
        #说明在休眠状态下
    else:
        all_transported.append(False)  

       
sol=pd.read_csv('C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/sample_submission.csv')
sol.head()
sol['Transported']=all_transported
sol.head()
sol.to_csv('./submissionCHVD.csv',index=False)


