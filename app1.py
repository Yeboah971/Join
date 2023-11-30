# -*- coding: utf-8 -*-
"""

@author: Shalom Adjei-Yebaoh
"""

# -*- coding: utf-8 -*-
"""
Created on  Dec. 12:50:04 2023

@author: Shalom Adjei-Yebaoh
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import tensorflow as tf


from PIL import Image

model =tf.keras.models.load_model("model.h5")
#pickle_in = open("model.pkl","rb")
#model=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(LL,PI,DPI,CF):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    prediction=model.predict([[LL,PI,DPI,CF]])
    print(prediction)
    return prediction



def main():
    st.title("Residual Shear Stenght of Clay")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Geotech  ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    LL = st.text_input("LL","Input Liquid Limit")
    PI = st.text_input("PI","Input Plasticity Index")
    DPI = st.text_input("DPI","Input Change in PI")
    CF= st.text_input("CF","Input Clay Fraction")
    try:
     LL = float(LL)
     PI = float(PI)
     DPI = float(DPI)
     CF = float(CF)
    except ValueError:
     st.error("Please enter SCALED numeric values for LL, PI, DPI, and CF.")
     st.stop()
    result=""
    
    if st.button("Predict"):
        result=predict_note_authentication(LL,PI,DPI,CF)
    st.success('The frictional angle is  {}'.format(result))
    if st.button("About"):
        st.text("This app is used for predicting the residual shear strenth of clay")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    