import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler 
from keras models import Sequential 
from keras. layers import LSTM, Dense
df = pd.read csv("/content/NSE-Tata-Global-Beverages-Limited.esy")
df[ "Date"] = pd.to_datetime(df.Date, format="%y-%m-%d" )
scaler = MinMaxScaler ()
scaled data = scaler fit transform(df[[ 'Close' ]].values)
x_train, y_train = [],[]
x_train.append(scaled_data[i-60:i, 0])
y_train. append (scaled_data[i, 0])
x_train, Y_train = np.array(x_train), np.array (y_train)
x_train = np.reshape(x_train, (x_train.shape(0), x_train, shape[1], 1))
model = Sequential()
model.add (LSTM(units=50, return_sequences=True, input_shape=(x_train.shape(1), 1)))
model.add (LSTU(units=50))
model.add (Dense (1) )
model.compile(loss= 'mean_squared _error', optinizer-'adam') 
model.fit(x_train, Y_train, epochs=10, batch_size=1, verbose=2)
inputs = scaler.transform(df[len(df)-len(x_train) -60:][ ['Close']].values)
x_test = [inputs[i-60:i, 0] for i in range(60, inputs.shape[0]) ]
x_test = np.array(x_test)
x_test = np.zeshape(x_test, (x_test.shape[0], x_test.shape([1], 1)) )
closing_price = model.predict(x_test)
closing_price = scaler.inverse_transform(closing_price)
plt.figure(figsize=（16, 8））
plt.plot(df["Close"], label='Actual Close Price')
plt. plot(np.arange(len(df)-len(closing_price),len(df)),closing_price,label='Predicted CLose Price')
plt. legend()
plt. show()
