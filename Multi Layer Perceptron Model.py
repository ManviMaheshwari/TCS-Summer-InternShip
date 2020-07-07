# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UXTPYWdpMFY_ewjK4LiEQ9bIc_ly37Hd
"""

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb

max_features=5000
maxlen=100
batch_size=64
embedding_dims=16
filters=128
kernel_size=3
hidden_size=128
epochs=5

(x_train, y_train), (_, _) = imdb.load_data(num_words=max_features)

x_train= sequence.pad_sequences(x_train, maxlen=maxlen)

model=Sequential()
model.add(Embedding(max_features, embedding_dims, input_length=maxlen))
model.add(Conv1D(filters,kernel_size, padding='valid',activation='relu', strides=1))
model.add(GlobalMaxPooling1D())
model.add(Dense(128,activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])

model.fit(x_train, y_train,batch_size=batch_size, epochs=epochs)