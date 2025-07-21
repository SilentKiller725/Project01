
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
from data_cleaning import cleaning_data

def feature_engineering(df):
    
    df['Log_Amount']=np.log(df['Amount']+1)

    scaler=StandardScaler()
    df[['Scaled_Time','Scaled_Amount']]=scaler.fit_transform(df[['Time','Amount']])
    
    df.drop(['Time','Amount','Log_Amount'],axis=1,inplace=True)

    return df

def save_data(df):
    op_path=file_path = os.path.join(os.path.dirname(__file__), "..", "data", "engi_creditcard.csv")
    df.to_csv(op_path,index=False)

if __name__ == "__main__":
    df= cleaning_data()
    #print(df.head())
    df = feature_engineering(df)
    save_data(df)