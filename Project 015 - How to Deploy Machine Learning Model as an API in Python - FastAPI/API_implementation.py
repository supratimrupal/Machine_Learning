import json
import requests

url='https://diabetes-ml-model-deploy.onrender.com/diabetes_prediction'

#6,148,72,35,0,33.6,0.627,50
input_data_for_model={    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
   }


input_json = json.dumps(input_data_for_model)
print(input_json)
response = requests.post(url, data=input_json)

print(response.text)