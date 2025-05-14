import numpy as np
import pandas as pd

data = pd.read_csv("D:\Downloads\dirty_cafe_sales.csv", encoding='latin1')

#print(data.isnull().sum())

data['Quantity']=pd.to_numeric(data['Quantity'], errors='coerce')
data['Quantity'].fillna(data['Quantity'].mean(),inplace=True)

data['Item'].fillna(data['Item'].mode()[0],inplace=True)

data['Price Per Unit']=pd.to_numeric(data['Price Per Unit'], errors='coerce')
data['Price Per Unit'].fillna(data['Price Per Unit'].mean(),inplace=True)

data['Total Spent']=pd.to_numeric(data['Total Spent'],errors='coerce')
data['Total Spent'].fillna(data['Total Spent'].mean(),inplace=True)

data['Payment Method'].fillna(data['Payment Method'].mode()[0],inplace=True)

data['Location'].fillna(data['Location'].mode()[0],inplace=True)

data['Transaction Date'].fillna(data['Transaction Date'].mode()[0],inplace=True)

print(data.isnull().sum())

print(data)
