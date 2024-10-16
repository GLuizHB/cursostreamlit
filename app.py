import streamlit as st

# Definir título e estilo de cabeçalho
st.set_page_config(page_title="Fisio Maia", layout="wide")

# Cabeçalho
st.markdown("""
    <style>
        .main-header {
            font-size: 40px;
            font-weight: bold;
            color: #1E6F86;
            text-align: center;
        }
        .login-box {
            background-color: #E1EAEA;
            padding: 20px;
            border-radius: 10px;
        }
        .input-box {
            margin-bottom: 10px;
        }
        .botao {
            background-color: #1E6F86;
            color: white;
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }
        .social-login {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .social-icon {
            margin: 0 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Layout de colunas
col1, col2 = st.columns([1, 3])

# Coluna do Login
with col1:
    st.image("logo.png", width=150)  # Substitua com o caminho da logo
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.subheader("Acesse sua conta")
    
    usuario = st.text_input("Usuário:", "joao.transeunte@aqui.com", key="user")
    senha = st.text_input("Senha:", type="password", key="password")

    if st.button("Entrar", key="entrar"):
        st.write("Logado com sucesso!")  # Ação do login

    st.markdown("<p>ou entre por:</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='social-login'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Google_2015_logo.svg' alt='Google' class='social-icon' width=30 />
        <img src='https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg' alt='Facebook' class='social-icon' width=30 />
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p>Caso não tenha conta, <a href='#'>Cadastre-se aqui</a></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Coluna do Conteúdo
with col2:
    st.markdown("<h1 class='main-header'>Conheça a FISIO MAIA</h1>", unsafe_allow_html=True)
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """)
    
    st.image("equipe.png", caption="Equipe Fisioterapeutas")  # Substitua com a imagem da equipe

    # Ícones de redes sociais
    st.markdown("""
    <div style='display: flex; justify-content: center;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png' alt='Instagram' width=30 style='margin: 0 10px;'/>
        <img src='https://upload.wikimedia.org/wikipedia/commons/5/53/Twitter_bird_logo_2012.svg' alt='Twitter' width=30 style='margin: 0 10px;'/>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/42/X_logo_2023.svg' alt='X' width=30 style='margin: 0 10px;'/>
    </div>
    """, unsafe_allow_html=True)
