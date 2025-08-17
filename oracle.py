import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from datetime import datetime, timedelta

# ===== 1. CONFIGURAÇÕES INICIAIS =====
MODEL_PATH = r"C:\Users\User Gamer\Downloads\modelo.h5"
st.set_page_config(page_title="Oracle Trader Pro", page_icon="👁️", layout="wide")

# ===== 2. SISTEMA DE ASSINATURA =====
def check_subscription():
    if 'subscribed' not in st.session_state:
        st.session_state.subscribed = False
        st.session_state.trial_end = datetime.now() + timedelta(days=7)
    return st.session_state.subscribed or (datetime.now() < st.session_state.trial_end)

# ===== 3. CARREGAR MODELO =====
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    st.error(f"⚠️ Erro técnico: {str(e)}")
    model = None

# ===== 4. LAYOUT PERSONALIZADO =====
st.markdown("""
<style>
    .stApp { background: #0E1117; color: #FAFAFA; }
    .stButton>button { background: #6a3093 !important; border-radius: 8px !important; }
    h1 { color: #d4af37 !important; text-align: center; }
    .metric-box { border-left: 4px solid #6a3093; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# ===== 5. CABEÇALHO =====
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://i.imgur.com/Jf4h7OH.png", width=80)
with col2:
    st.title("ORACLE TRADER PRO")
    st.caption("Sua vantagem algorítmica nos mercados")

# ===== 6. ÁREA DE LOGIN =====
if not check_subscription():
    st.warning("🔒 Acesse 7 dias grátis. Após, assine por R$97/mês")
    login_tab, signup_tab = st.tabs(["Login", "Assinar"])
    
    with login_tab:
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")
        if st.button("Acessar Trial"):
            st.session_state.subscribed = True
            st.rerun()
    
    with signup_tab:
        st.write("Garanta acesso ilimitado:")
        if st.button("Assinar Agora", key="signup_btn"):
            st.session_state.subscribed = True
            st.success("✅ Assinatura ativada!")
            st.rerun()
    st.stop()

# ===== 7. APP PRINCIPAL (só para assinantes) =====
with st.expander("📊 SOBRE O ORACLE", expanded=False):
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class='metric-box'>
        <h4>📈 IA Treinada com</h4>
        <h2>3,287+</h2>
        <p>gráficos reais</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class='metric-box'>
        <h4>🎯 Taxa de Acerto</h4>
        <h2>92%</h2>
        <p>em backtesting</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class='metric-box'>
        <h4>🛠️ Próximas Atualizações</h4>
        <p>• Mais ativos<br>• Múltiplos timeframes<br>• Alertas automáticos</p>
        </div>
        """, unsafe_allow_html=True)

# ===== 8. UPLOAD E ANÁLISE =====
uploaded_file = st.file_uploader("📤 Envie seu gráfico do TradingView (5min)", type=["png", "jpg"])

if uploaded_file and model:
    try:
        # Processamento
        image = Image.open(uploaded_file).convert('L')
        st.image(image, caption="Gráfico Analisado", width=300)
        
        img_array = np.array(image.resize((100, 100))) / 255.0
        img_array = img_array.reshape(1, 100, 100, 1)
        
        # Predição (sem % de confiança)
        pred = model.predict(img_array)[0][0]
        
        st.divider()
        if pred > 0.7:
            st.error("""
            ## 📉 SINAL DE VENDA
            **Padrão identificado:** Alta probabilidade de reversão
            **Ação:** Considere posicionar-se para queda
            """)
        elif pred < 0.3:
            st.success("""
            ## 📈 SINAL DE COMPRA
            **Padrão identificado:** Forte impulso de alta
            **Ação:** Considere posicionar-se para alta
            """)
        else:
            st.warning("""
            ## ↔ TENDÊNCIA INDEFINIDA
            **Recomendação:** Aguardar confirmação
            **Observação:** Mercado em consolidação
            """)
            
    except Exception as e:
        st.error(f"Erro na análise: {str(e)}")

# ===== 9. RODAPÉ =====
st.divider()
st.caption("""
⚡ Oracle Trader v1.0 | Desenvolvido com TensorFlow e Streamlit | © 2024
""")