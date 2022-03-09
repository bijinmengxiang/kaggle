首先对下载数据进行分析

由于可能产生的版权或者一系列的问题，就不将数据集放置在此。

你可以从kaggle的网站上下载数据集。url：https://www.kaggle.com/c/spaceship-titanic/data

"""从官网摘录的字段描述 from https://www.kaggle.com/c/spaceship-titanic/data"""

"""
train.csv - Personal records for about two-thirds (~8700) of the passengers, to be used as training data.
PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.（乘客的ID 共由六位数字组成，前四位为团队编号，代表可能为一同参加的旅行）
HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.（乘客所属母星）
CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.（是否处于休眠状态）
Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard.（乘客的床铺位置）
Destination - The planet the passenger will be debarking to.（乘客目的地）
Age - The age of the passenger.（乘客年龄）
VIP - Whether the passenger has paid for special VIP service during the voyage.（乘客是否为VIP客户）
RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.（乘客在船上各类的消费数量）
Name - The first and last names of the passenger.（乘客姓名）
Transported - Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.（乘客是否进入异次元空间）

test.csv - Personal records for the remaining one-third (~4300) of the passengers, to be used as test data. Your task is to predict the value of Transported for the passengers in this set.（测试集除了不提供Transported属性外，其他与训练集相同）
"""

数据集中包含训练集，测试集与示例提交样本（未进行摘录）。训练集与测试集中的样本属性相同且在某些特定属性中含有缺失值。

首先我们假设所有属性均独立，所以我们需要对各属性是否对乘客进入异次元空间有影响做出分析。

我们分析了“乘客一同参加的旅行团队的成员数量find_connection_in id.py”，“乘客所属母星find_connection_in HomePlanet.py”，“是否处于休眠状态find_connection_in cryosleep.py”，“乘客目的地find_connection_in destination.py”，“乘客是否为VIP客户find_connection_in VIP.py”属性对于乘客是否进入异次元空间的影响。

运行find_connection_in id.py我们得到：
![image](https://user-images.githubusercontent.com/46309653/157363548-48b35f71-b0b2-4dac-b7ad-b717cf37647f.png)
此处说明乘客一同参加的旅行团队的成员数量与乘客是否进入异次元空间有一定影响

运行find_connection_in HomePlanet.py我们得到：
![image](https://user-images.githubusercontent.com/46309653/157363760-3efed50e-6be2-47df-af41-8185aa9639f6.png)
此处说明乘客所属母星与乘客是否进入异次元空间有一定影响

运行find_connection_in cryosleep.py我们得到：
![image](https://user-images.githubusercontent.com/46309653/157363839-8d68f38a-300e-47e1-a43d-51ee37bb62c3.png)
此处说明乘客是否处于休眠状态与乘客是否进入异次元空间有大量影响

运行find_connection_in destination.py我们得到：
![image](https://user-images.githubusercontent.com/46309653/157363918-bef72a32-bbd6-4494-85d8-1b52f23d6437.png)
此处说明乘客目的地与乘客是否进入异次元空间有一定影响

运行find_connection_in VIP.py我们得到：
![image](https://user-images.githubusercontent.com/46309653/157363918-bef72a32-bbd6-4494-85d8-1b52f23d6437.png)
此处说明乘客是否为VIP客户与乘客是否进入异次元空间有一定影响


