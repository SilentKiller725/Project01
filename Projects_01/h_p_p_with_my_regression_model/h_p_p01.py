
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder

class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.w = None
        self.b = None

    def fit(self, x, y):
        x = np.array(x)
        y = np.array(y)
        n_samples, n_features = x.shape
        
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.iterations):
            y_predicted = np.dot(x, self.w) + self.b 

            dw = (1 / n_samples) * np.dot(x.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, x):
        x = np.array(x)
        return np.dot(x, self.w) + self.b

    
def house_price_prediction():
    df=pd.read_csv(r"D:\Downloads\archive (1)\Housing.csv")
    y=df["price"]
    x=df.drop(columns=["price"])

    categorical_fea=["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]
    numerical_fea=x.columns.difference(categorical_fea)

    preprocessor = ColumnTransformer([
    ("num", StandardScaler(),numerical_fea),
    ("cat", OneHotEncoder(),categorical_fea),
     ])

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=55)

    new_x_train=preprocessor.fit_transform(X_train)
    new_x_test=preprocessor.transform(X_test)

    LR_model=LinearRegression()

    LR_model.fit(new_x_train,y_train.values)

    new_house = pd.DataFrame({
        'area': [8225],
        'bathrooms': [5],
        'bedrooms': [6],
        'stories': [3],
        'parking': [2],
        'mainroad': ['yes'],
        'guestroom': ['no'],
        'basement': ['yes'],
        'hotwaterheating': ['yes'],
        'airconditioning': ['yes'],
        'prefarea': ['no'],
        'furnishingstatus': ['furnished'],
    })

    new_house_transformed = preprocessor.transform(new_house)

    predicted_price=LR_model.predict(new_house_transformed)

    print(f"The price of new house is {predicted_price}")

if __name__=="__main__":
    house_price_prediction()