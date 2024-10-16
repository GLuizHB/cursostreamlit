import streamlit as st 
import pandas as pd 

st.sidebar.title("Carregue o seu DataSet")

upload = st.sidebar.file_uploader("escolha o arquivo", type="csv")
if upload is not None:
    df = pd.read_csv(upload)
    st.dataframe(df)