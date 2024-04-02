# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:26:58 2024

@author: Admin
"""
import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('E:/Journey/My DS/Project 10 - Deploy Machine Learning Model using Streamlit in Python  ML model Deployment/trained_model.sav','rb')) #reading in binary mode

#creating a function for prediction
def diabetes_prediction(input_data):
    
    #input_data = (6,103,72,32,190,37.7,0.324,55)

    #changing list to numpy array
    input_data_np_arr=np.asarray(input_data)

    # reshape the np array as we are predicting for one instance
    input_data_reshaped = input_data_np_arr.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    if(prediction[0] == 1):
      return 'Test Result Positive'
    else:
      return 'Test Result Negative'



def main():
    
    # Providing a title for user interface
    st.title('Diabetes Prediction Web App')
    
    # Getting input Data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('Skin Thickness Value')    
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')       
    Age=st.text_input('Age of the Person')
    
    #Code for Prediction
    diagnosis = ''
    
    #Creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
        
    
if __name__ == '__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    