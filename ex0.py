# importe o streamlit

import streamlit as st

# Interface gráfica com o usuário

st.sidebar.title("Ex0")

num = st.sidebar.number_input("Digite um número:", step=1)

# Algoritmopara positivo negativo e nulo

if num > 0:
    st.write("É um número positivo!")
elif num < 0:
    st.write("É um número negativo!")
elif num == 0:
    st.write("É um número neutro!")
