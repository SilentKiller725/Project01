import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def model_training(df):
   print("Columns before drop:", df.columns)
   x = df.drop(['Class'], axis=1)
   print("Columns after drop:", x.columns)

   y=df['Class']
   
   x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=21)

   model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
   model.fit(x_train,y_train)

   y_pred=model.predict(x_test)
   y_prob=model.predict_proba(x_test)[:1]
   
   op_path1=file_path = os.path.join(os.path.dirname(__file__), "..", "model", "fraud_model.pkl") 
   joblib.dump(model, op_path1)

if __name__=="__main__":
   op_path=file_path = os.path.join(os.path.dirname(__file__), "..", "data", "engi_creditcard.csv") 
   df=pd.read_csv(op_path)
   model_training(df)
   
   
