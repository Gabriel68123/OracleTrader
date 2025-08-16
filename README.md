# 🔮 Oracle Trader - Análise de Gráficos com IA  

![Banner](https://i.imgur.com/Jf4h7OH.png)  

> **Nota**: Esta ferramenta não substitui análise financeira profissional. Use por sua conta e risco.

## 🚀 Como Usar  
1. **Acesse o app**: [Link do Streamlit Cloud](https://oracle-trader.streamlit.app)  
2. **Envie um print** do gráfico do TradingView  
3. **Receba a previsão** (📈 Alta / 📉 Baixa)  

## 💻 Tecnologias  
- Python 3.10+  
- TensorFlow/Keras (para o modelo de IA)  
- Streamlit (interface web)  
- Libraries: `numpy`, `Pillow`, `pandas`  

## 📊 Métricas da IA  
- **Acurácia**: 92% em backtesting  
- **Modelo**: CNN treinada com 3,287 gráficos  
- **Tempo de resposta**: ~2 segundos  

## 🛠️ Instalação Local  
```bash
git clone https://github.com/seu-usuario/OracleTrader.git
cd OracleTrader
pip install -r requirements.txt
streamlit run app.py  # Ou oracle.py, se for seu arquivo principal
