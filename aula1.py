import streamlit as st 
import requests 
import pandas as pd
import plotly.express as px 

st.title("DASHBOARD DE VENDAS:shopping_trolley:")


#Estamos iniciando o streamlit
#Ele nos ajudara no peojeto final
# Em sua instalação vem incluido o pandas e outras libs


nome=st.sidebar.text_area("Seu nome:")
st.sidebar.button(label="clique")

st.write(f"Olá {nome}!")

idade = st.sidebar.number_input("Digite sua idade:", min_value=14, max_value=120)
if idade >= 18:
    st.write(f"{nome} - você é maior de idade: {idade}")
else:
    st.write(f"{nome} - você é menor de idade: {idade}")

st.sidebar.radio("Escolha uma opção:")