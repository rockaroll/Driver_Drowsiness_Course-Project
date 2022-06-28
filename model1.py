import pandas as pd
import numpy as np
import PySimpleGUI as sg
df=pd.read_excel('D:/2ndyear/Semister-2/DataScience/Cpxl.xlsx')
print(df)
df=df.drop(columns=['Name','Contact','Email','Sl.No'])
print(df)
df=df.dropna()
print(df)
df[df['Capability']==1.6666666666666667]
from matplotlib import pyplot as pld
x=df['Alcohol Level']
y=df['Capability']
pld.scatter(x,y)
pld.xlabel('Alcohol Level')
pld.ylabel('Capability')
pld.show()
x=df['Amount Of sleep']
y=df['Capability']
pld.scatter(x,y)
pld.xlabel('Amount Of Sleep')
pld.ylabel('Capability')
pld.show()
print(df.corr())
da=df.drop(columns=['Descion'])
print(da.corr())
y=da['Capability'].values
x=da.drop(['Capability'],axis=1).values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
from sklearn.linear_model import LinearRegression
ml=LinearRegression()
ml.fit(x_train,y_train)
y_pred=ml.predict(x_test)
print(y_pred)
print(ml.predict([[0,9]]))
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)
import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()
pred_y_df=pd.DataFrame({'Actual Value':y_test,'Predicted Value':y_pred})
print(pred_y_df)
def predict(a,s):
    if ml.predict([[a,s]])>=0.76:
        sg.popup("Congratulations!!You have passed the test.Have a good day.")
    elif ml.predict([[a,s]])>=0.0 and ml.predict([[a,s]])<0.76 or ml.predict([[a,s]])<0 :
        sg.popup("I'm Sorry!!!You weren't able to pass the test")







