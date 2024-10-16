
import streamlit as st
import random

st.title("JOGO DO NÚMERO SECRETO")

st.write("Boas-Vindas ! Advinhe o Número")

numsecreto = random.randint(1, 100)

if 'numsecreto' not in st.session_state:
    st.session_state.numsecreto = numsecreto
    st.session_state.tentativas = 0

numero = st.number_input("Digite um número de 1 a 100:", min_value=1, max_value=100)

if st.button("Verificar"):
    st.session_state.tentativas += 1
    
    if numero < st.session_state.numsecreto:
        st.warning("Muito baixo! Tente novamente.")
    elif numero > st.session_state.numsecreto:
        st.warning("Muito alto! Tente novamente.")
    else:
        st.success(f"Parabéns! Você acertou o número {st.session_state.numsecreto} em {st.session_state.tentativas} tentativas!")