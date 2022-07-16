import streamlit as st
import pandas as pd
import numpy as np


st.title("Car Price Prediction")

df = pd.read_csv("final_scout_not_dummy.csv", nrows=(100)) 


import pickle
file = open('final_auto_scout', 'rb')
model = pickle.load(file, encoding='utf-8')


Horsepower = st.sidebar.number_input('Horsepower:', min_value = 49 , max_value = 250, value=50, step=10)


Make_model =st.sidebar.selectbox("Please select model", ["Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"])



Age = st.sidebar.selectbox("Please select age",[0.0, 1.0, 2.0, 3.0])

Gearing_Type = st.sidebar.selectbox('Please select gearing type', ['Automatic', 'Manual', 'Semi-automatic'])


Km = st.sidebar.slider('What is the km:' ,min_value = 1000 ,max_value = 55000, step = 500)



my_dict= { 'hp_kW'        : Horsepower   ,
           'age'          : Age  ,
           'make_model'   : Make_model  ,
           'Gearing_Type' : Gearing_Type ,
           'Km'           :Km   }


new_df = pd.DataFrame.from_dict([my_dict])
st.table(new_df)

columns = ['hp_kW',
 'km',
 'age',
 'make_model_Audi A1',
 'make_model_Audi A3',
 'make_model_Opel Astra',
 'make_model_Opel Corsa',
 'make_model_Opel Insignia',
 'make_model_Renault Clio',
 'make_model_Renault Duster',
 'make_model_Renault Espace',
 'Gearing_Type_Automatic',
 'Gearing_Type_Manual',
 'Gearing_Type_Semi-automatic']


new_df = pd.get_dummies(new_df).reindex(columns=columns, fill_value=0)
new_df.head()




if st.button('price'):
    pred = model.predict(new_df)
    st.success("Predict price of your car is €{}. ".format(int(pred[0])))