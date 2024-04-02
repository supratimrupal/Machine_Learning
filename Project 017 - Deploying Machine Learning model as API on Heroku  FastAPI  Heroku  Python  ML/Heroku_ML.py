
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # CROSS ORIGIN RESOURCE SHARING
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
     
# loading ML model 

diabetes_model=pickle.load(open('saved_models/diabetes_pred_trained_model.sav','rb')) #reading in binary mode


@app.post('/diabetes_prediction')

def diabetes_pred(input_parm : model_input ):
    input_data = input_parm.json()
    input_dict = json.loads(input_data)
    preg = input_dict['Pregnancies']
    glu = input_dict['Glucose']
    bp = input_dict['BloodPressure']
    st = input_dict['SkinThickness']
    insulin = input_dict['Insulin']
    bmi = input_dict['BMI']
    dpf = input_dict['DiabetesPedigreeFunction']
    age = input_dict['Age']
    
    input_list = [preg,glu,bp,st,insulin,bmi,dpf,age]
    diab_diagnosis = diabetes_model.predict([input_list])
    if(diab_diagnosis[0] == 1):
        return 'Test Result Positive'
    else:
        return 'Test Result Negative'
       
        
       