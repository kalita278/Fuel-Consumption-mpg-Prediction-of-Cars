# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:07:59 2023

@author: dell1
"""

import numpy as np
import pickle
import streamlit as st
from flask import Flask, request, jsonify

loaded_model = pickle.load(open('C:/Users/dell1/MPG(miles per gallon) prediction of cars/trained_model.sav','rb'))
loaded_model_scaled = pickle.load(open('C:/Users/dell1/MPG(miles per gallon) prediction of cars/trained_model_scaled.sav','rb'))

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

app = Flask(__name__)
@app.route('/api',methods=["POST"])
def predict():
    data = request.get_json(force=True)
    predict_req = [[data['cyl'],data['disp'],data['hp'],data['wt'],data['acc'],data['yr'],data['origin_1'],data['origin_2'],data['origin_3']]]
    predict_req = np.array(predict_req)
    predict_req = loaded_model_scaled.transform(predict_req)
    predict_req = predict_req.reshape(1,-1)
    prediction = loaded_model.predict(predict_req)
    op=prediction[0]
    return jsonify(int(op))

if __name__ == '__main__' :
    app.run(port=8080, debug =True)
    
    