# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:26:58 2024

@author: Admin
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading ML model 

diabetes_model=pickle.load(open('E:/Journey/My DS/Project 14 - Multiple Disease Prediction using Machine Learning in Python Streamlit Web App - Deployment/saved_models/diabetes_pred_trained_model.sav','rb')) #reading in binary mode
heart_disease_model=pickle.load(open('E:/Journey/My DS/Project 14 - Multiple Disease Prediction using Machine Learning in Python Streamlit Web App - Deployment/saved_models/heart_disease_pred_trained_model.sav','rb')) #reading in binary mode
parkinsons_model=pickle.load(open('E:/Journey/My DS/Project 14 - Multiple Disease Prediction using Machine Learning in Python Streamlit Web App - Deployment/saved_models/parkinsons_disease_pred_trained_model.sav','rb')) #reading in binary mode

#sidebar for navigating
#https://icons.getbootstrap.com/ for icons
with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System', 
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'], 
                         icons=['prescription2', 'heart-pulse-fill','capsule'], menu_icon="building-add", 
                         default_index=2)
    
                                                                

# Diabetes Prediction Page
if (selected =='Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    # Getting input Data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    # getting the input data from the user
    col1, col2, col3 ,col4 = st.columns(4)

    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
        
    with col2:    
        Glucose=st.text_input('Glucose level')
        
    with col3:     
        BloodPressure=st.text_input('Blood Pressure Value')
        
    with col4:    
        SkinThickness=st.text_input('Skin Thickness Value')
        
    with col1:    
        Insulin=st.text_input('Insulin level')
        
    with col2:    
        BMI=st.text_input('BMI Value')
        
    with col3:    
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Func Val') 
        
    with col4:    
        Age=st.text_input('Age of the Person')    
    
    #Code for Prediction
    diab_diagnosis = ''
    
    #Creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if(diab_diagnosis[0] == 1):
            diab_diagnosis = 'Test Result Positive'
        else:
            diab_diagnosis = 'Test Result Negative'
        
    st.success(diab_diagnosis)
    
    
    
    
    
    

# Heart Disease Prediction Page
if (selected =='Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    #Creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_diagnosis = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if(heart_diagnosis[0] == 1):
            heart_diagnosis = 'Test Result Positive'
        else:
            heart_diagnosis = 'Test Result Negative'
        
    st.success(heart_diagnosis)





# Parkinsons Prediction Page

if (selected =='Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction using ML')    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP RAP')

    with col2:
        PPQ = st.text_input('MDVP PPQ')

    with col3:
        DDP = st.text_input('Jitter DDP')

    with col4:
        Shimmer = st.text_input('MDVP Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer APQ5')

    with col3:
        APQ = st.text_input('MDVP APQ')

    with col4:
        DDA = st.text_input('Shimmer DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_diagnosis = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        if(parkinsons_diagnosis[0] == 1):
            parkinsons_diagnosis = 'Test Result Positive'
        else:
            parkinsons_diagnosis = 'Test Result Negative'
        
    st.success(parkinsons_diagnosis)    
    
    
    
    
    
    
    
    
    
    