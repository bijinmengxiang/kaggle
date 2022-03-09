from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
    
# Load data
path = "C:/Users/cnhhdn/Desktop/kaggle/spaceship-titanic/data/trainCHVD.csv"

data = pd.read_csv(path) 
 
print(pd.isna(data).any())

# 删除缺少值的那一行
data = data.dropna(axis=0)

# Choose target and features
y = data.Transported
features1 = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck']
features2 = ['CryoSleep','HomePlanet',  'VIP', 'Destination','Age']
X1 = data[features1]
X2 = data[features2]

train_X1, val_X1, train_y1, val_y1 = train_test_split(X1, y,random_state = 0) 
train_X2, val_X2, train_y2, val_y2 = train_test_split(X2, y,random_state = 0) 

forest_model1 = RandomForestRegressor(random_state=1)
forest_model2 = RandomForestRegressor(random_state=1)
forest_model1.fit(train_X1, train_y1)
forest_model2.fit(train_X2, train_y2)

preds1 = forest_model1.predict(val_X1)
preds2 = forest_model2.predict(val_X2)

print(mean_absolute_error(val_y1, preds1))#包含消费
print(mean_absolute_error(val_y2, preds2))#不包含消费
