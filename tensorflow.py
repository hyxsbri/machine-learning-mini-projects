import pandas as pd

df = pd.read_csv('/Users/hyosasiburi/Desktop/py/알고리즘/gpascore.csv')
df = df.dropna()

import numpy as np
import tensorflow as tf

model = tf.keras.models.Sequential([
tf.keras.layers.Dense(64, activation = 'tanh'),
tf.keras.layers.Dense(128, activation = 'tanh'),
tf.keras.layers.Dense(1, activation = 'sigmoid'),
])

model.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])

X = []
for i, rows in df.iterrows():
    X.append([rows['gre'], rows['gpa'], rows['rank']])

y = df['admit'].values
model.fit(np.array(X),np.array(y), epochs = 1000)

pred = model.predict([[750,3.70,3], [400,2.2, 1]])
print(pred)