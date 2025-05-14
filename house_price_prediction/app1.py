import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

house_data={
    'size_sqft':[2000,2500,3000,4000],
    'price':[400000,500000,550000,700000]
}

df=pd.DataFrame(house_data)

X=df[['size_sqft']]
Y=df['price']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

test_house = 1750
predicted_price = model.predict([[test_house]])[0]
print(f"\nPredicting price for {test_house} sqft house:")
print(f"Predicted price: ${predicted_price:.2f}")