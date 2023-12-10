import pandas as pd 
import numpy as np 
from sklearn model_selection import train_test_split 
from sklearn. preprocessing import MinMaxScaler 
from sklearn. linear model import LogisticRegression
from sklearn.metrics import accuracy_score, precision score, recall_score, f1_score
data = pd. read_csv ('/content/NSE-Tata-Global-Beverages-Limited.zip' )
data[ 'Label'] = np. where(data[ 'Close' ].shift (-1) > data[ 'Close'], 1, 0)
X = data[ [ 'Close' ]].values
y = data[ 'Label' ].values
X_train, X_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.2, random_state=42)
scaler = MinMaxScaler ()
X_train_scaled = scaler. fit_ transform(X_train)
X_test_scaled = scaler. transform(X_test)
model = LogisticRegression()
model. fit(X_train_scaled, y_train)
y_pred = model predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score (y_test, y_pred)
f1 = f1_score (y_test, y_pred)
print (f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, Fl-Score: {f1:.2f}")
