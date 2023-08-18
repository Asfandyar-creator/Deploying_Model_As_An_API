from fastapi import FastAPI
from pydantic import BaseModel
import json
import pickle


app = FastAPI()
class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int



# Loading model file
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))


@app.post('/diabetes_prediction')
def diabetes_prediction(input_paramenters : model_input):
    input_data = input_paramenters.mode_dum_json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    Bp =  input_dictionary['BloodPressure']
    sktn = input_dictionary['SkinThickness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    diaped = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, Bp, sktn, ins, bmi, diaped, age]
    prediction = diabetes_model.predict([[input_list]])

    if prediction[0] == 0:
        return "This Person is not Diabetic"
    else:
        return "The Person is Diabetic"
