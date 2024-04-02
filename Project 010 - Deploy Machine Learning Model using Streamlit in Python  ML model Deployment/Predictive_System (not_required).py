# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:43:36 2024

@author: Admin
"""

import numpy as np
import pickle

loaded_model=pickle.load(open('E:/Journey/My DS/Project 10 - Deploy Machine Learning Model using Streamlit in Python  ML model Deployment/trained_model.sav','rb')) #reading in binary mode

input_data = (6,103,72,32,190,37.7,0.324,55)

#changing list to numpy array
input_data_np_arr=np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_np_arr.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
if(prediction[0]==1):
  print('Person has diabetes.')
else:
  print('Person does not have diabetes.')
