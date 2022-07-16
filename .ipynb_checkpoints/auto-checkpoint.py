import streamlit as st
import pandas as pd
import numpy as np


st.title("Price Prediction")

df = pd.read_csv("final_scout_not_dummy.csv", nrows=(100)) 
st.write(df.head())

import pickle
file = open('final_auto_scout', 'rb')
model = pickle.load(file, encoding='utf-8')
st.table(df.head())



Horsepower = st.sidebar.number_input('Horsepower:', min_value = 49 , max_value = 250, value=50, step=10)
st.write('Horsepower:', Horsepower)

Make_model =st.sidebar.selectbox("Please select model", ["Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"])
st.write("You selected this model:", Make_model)


Age = st.sidebar.selectbox("Please select age",[0.0, 1.0, 2.0, 3.0])
st.write("Please select age: ", Age)

Gearing_Type = st.sidebar.selectbox('Please select gearing type', ['Automatic', 'Manual'])
st.write('Please select gearing type :', Gearing_Type)



my_dict= { 'hp_kW'        : Horsepower   ,
           'age'          : Age  ,
           'make_model'   : Make_model  ,
           'Gearing_Type' : Gearing_Type    }


new_df = pd.DataFrame.from_dict([my_dict])
st.table(new_df)

new_df = pd.get_dummies(new_df)




if st.button('price'):
    pred = model.predict(new_df)
    st.write(pred[0])