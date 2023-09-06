# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 12:48:34 2023

@author: dell1
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('Model/trained_model.sav','rb'))
loaded_model_scaled = pickle.load(open('Model/trained_model_scaled.sav','rb'))

def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

def mpg_predict(input_data):
    input_data_flat = flat(input_data)
    input_data_array = np.array([input_data_flat])
    input_data_scaled = loaded_model_scaled.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
    return 'MPG of the car is:', round(prediction[0],2)


def main():
    
    st.title('MPG Prediction of Cars')
    st.header('Enter the value of following parameter')
    
    cyl = st.number_input('Enter the number of cyl')
    disp = st.number_input('Enter the value of displacement')
    hp = st.number_input('Enter the value of horsepower')
    wt = st.number_input('Enter the weight of the car')
    acc = st.number_input("Enter the acceleration of the car")
    yr = st.number_input('model year')
    origin = st.selectbox('Orgin of the car', (1,2,3))
    if origin == 1:
        origin = [1,0,0]
    elif origin == 2:
        origin = [0,1,0]
    else:
        origin = [0,0,1]
        
    pred = ' '
    
    if st.button('Predict'):
        pred = mpg_predict([cyl,disp,hp,wt,acc,yr,origin])
    st.success(pred)
    
if __name__ == '__main__':
    main()