import pandas as pd
import os

def cleaning_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "creditcard.csv")
    df = pd.read_csv(file_path)

    missing=df.isnull().sum()
    # print(missing)

    df=df.drop_duplicates()

    class_1=(df['Class']==1).sum()
    # print(class_1)

    return df

if __name__ == "__main__":
    df=cleaning_data()
    print(df.head())