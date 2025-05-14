import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class sales:
     def __init__(self,lr,ite):
          self.lr=lr
          self.ite=ite
          self.w=None
          self.b=None

     def sales_prediction(self,x,y):
        x=np.array(x)
        y=np.array(y)

        n_sam,n_fea=x.shape

        self.w=np.zeros(n_fea)
        self.b=0

        for i in range(self.ite):
          y_pred=np.dot(x,self.w)+self.b

          dw=(1/n_sam)*np.dot(x.T,(y_pred-y))
          db=(1/n_sam)*np.sum((y_pred-y))

          self.w-=self.lr*dw
          self.b-=self.lr*db

     def predict(self,x):
         x=np.array(x)
         return np.dot(x,self.w)+self.b
     
def sales_prediction():
    df=pd.read_csv(r"D:\Downloads\archive (2)\advertising.csv")
    y=df["Sales"]
    x=df.drop(columns=["Sales"])
    
    preprocessor=ColumnTransformer(transformers=[("num",StandardScaler(),x.columns)])

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    x_train = preprocessor.fit_transform(x_train)
    x_test = preprocessor.transform(x_test)

    sm=sales(0.01,200)

    sm.sales_prediction(x_train,y_train)

    tv_exp=float(input("Enter the expenditure on TV advertising: "))
    np_exp=float(input("Enter the expenditure on NewsPaper advertising: "))
    radio_exp=float(input("Enter the expenditure on Radio advertising: "))

    total_exp=pd.DataFrame({"TV":[tv_exp],"Newspaper":[np_exp],"Radio":[radio_exp]})
    total_exp=preprocessor.transform(total_exp)

    pred_price=sm.predict(total_exp)

    print(f"Total Sales is {pred_price}")

if __name__=="__main__":
    sales_prediction()