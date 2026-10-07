import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Análise via Derivadas", layout="centered")

# ==========================================
# CSS: QUADRO, SOMBRA À ESQUERDA E ANTI-SCROLL
# ==========================================
st.markdown("""
<style>
/* Cria o quadro com sombra projetada para a ESQUERDA e para baixo */
[data-testid="stPlotlyChart"] {
    background-color: var(--background-color); /* Fundo sólido adaptável (claro/escuro) */
    border-radius: 8px;
    box-shadow: -12px 12px 20px rgba(128, 128, 128, 0.25); /* Valor negativo no X joga a sombra pra esquerda */
    padding: 10px;
    margin-top: 1rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(128, 128, 128, 0.15); /* Borda sutil para fechar o quadro */
}

/* Trava a largura para não gerar barras de rolagem indesejadas */
[data-testid="stPlotlyChart"] iframe {
    max-width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL CUSTOMIZADA (PERSISTENTE)
# ==========================================
with st.sidebar:
    st.markdown("### Navegação")
    st.page_link("Inicio.py", label="Início")
    
    with st.expander("Módulo: Cálculo I", expanded=True):
        st.page_link("pages/1_Analise_de_graficos_via_derivadas.py", label="Análise de gráficos via derivadas")
        st.page_link("pages/2_Teorema_de_Rolle_e_Valor_Medio.py", label="Teoremas de Rolle e do Valor Médio")
        st.page_link("pages/3_Testes_da_1a_e_2a_Derivada.py", label="Testes da 1ª e 2ª Derivada")

# ==========================================
# CONTEÚDO PRINCIPAL
# ==========================================
st.title("1. Interpretação da derivada a partir do gráfico")

try:
    with open("textos/analise_intro.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except FileNotFoundError:
    st.warning("Crie o arquivo 'textos/analise_intro.md' com o texto base na pasta textos/.")

st.divider()

# ------------------------------------------
# EXEMPLO 1: CIÊNCIAS ECONÔMICAS
# ------------------------------------------
st.subheader("Exemplo Prático: Ciências Econômicas")
st.markdown("""
**Função Custo Total:** $C(q) = q^3 - 6q^2 + 15q$  
*(Representa o custo de produzir $q$ mil unidades)*

Observe que o custo sempre sobe, mas a **velocidade (ritmo)** muda ao longo da produção:
* **Fase inicial:** Cresce acelerado (ineficiência de escala pequena).
* **Fase intermediária:** Desacelera (ganho e economia de escala).
* **Fase final:** Acelera de novo (gargalos operacionais, horas extras).

**Pergunta-chave:** *Em qual quantidade o custo marginal (o custo de produzir a próxima unidade) é mínimo?*
""")

q_ext = np.linspace(-50, 50, 2000)
c_ext = q_ext**3 - 6*q_ext**2 + 15*q_ext

fig_econ = go.Figure()

fig_econ.add_trace(go.Scatter(
    x=q_ext, y=c_ext, 
    mode='lines', 
    name='Custo Total C(q)', 
    line=dict(color='#0072B2', width=4) 
))

inflex_y = 2**3 - 6*2**2 + 15*2
fig_econ.add_trace(go.Scatter(
    x=[2], y=[inflex_y], 
    mode='markers', 
    name='Custo Marginal Mínimo', 
    marker=dict(color='#D55E00', size=12, symbol='diamond')
))

fig_econ.update_layout(
    # Título embutido dentro do quadro do gráfico (Padrão ABNT)
    title=dict(
        text="<b>Gráfico 1</b> – Função Custo Total e Custo Marginal Mínimo",
        font=dict(size=15),
        y=0.95, x=0.02, xanchor='left', yanchor='top'
    ),
    xaxis_title="Quantidade produzida (q) em milhares",
    yaxis_title="Custo Total C(q)",
    hovermode="x unified",
    margin=dict(l=20, r=20, t=60, b=80), # Margem superior (t) ampliada para o título caber
    legend=dict(orientation="h", yanchor="top", y=-0.25, xanchor="right", x=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        range=[0, 6], 
        showgrid=True, gridcolor='rgba(128,128,128,0.5)', # Contraste aumentado
        zeroline=True, zerolinecolor='rgba(128,128,128,0.8)', zerolinewidth=2, # Eixos principais muito mais escuros
        showline=True, linewidth=1, linecolor='rgba(128,128,128,0.8)',
        mirror=True
    ),
    yaxis=dict(
        range=[0, 100],
        showgrid=True, gridcolor='rgba(128,128,128,0.5)', # Contraste aumentado
        zeroline=True, zerolinecolor='rgba(128,128,128,0.8)', zerolinewidth=2,
        showline=True, linewidth=1, linecolor='rgba(128,128,128,0.8)',
        mirror=True
    )
)

st.plotly_chart(fig_econ, use_container_width=True)

st.divider()

# ------------------------------------------
# EXEMPLO 2: CIÊNCIAS AGRONÔMICAS
# ------------------------------------------
st.subheader("Exemplo Prático: Ciências Agronômicas")
st.markdown("""
**Função Produção:** $P(d) = -0.1d^3 + 1.2d^2 + 2d$  
*(Produção em t/ha em função da dose de fertilizante $d$)*

O gráfico revela três fases distintas do impacto do fertilizante:
* **Fase 1 (Rendimentos crescentes):** Até $d = 4$, cada dose extra aumenta a produção de forma acelerada.
* **Fase 2 (Rendimentos decrescentes):** De $d = 4$ até $d = 8.75$, a produção ainda cresce, mas em ritmo cada vez menor.
* **Fase 3 (Rendimentos negativos):** Após $d = 8.75$, o excesso de fertilizante intoxica o solo e a produção cai.

**Pergunta-chave:** *Qual a dose exata que maximiza a produção?*
""")

d_ext = np.linspace(-50, 50, 2000)
p_ext = -0.1*d_ext**3 + 1.2*d_ext**2 + 2*d_ext

fig_agro = go.Figure()

fig_agro.add_trace(go.Scatter(
    x=d_ext, y=p_ext, 
    mode='lines', 
    name='Produção P(d)', 
    line=dict(color='#0072B2', width=4)
))

p_inflex = -0.1*4**3 + 1.2*4**2 + 2*4
p_max = -0.1*8.75**3 + 1.2*8.75**2 + 2*8.75

fig_agro.add_trace(go.Scatter(
    x=[4], y=[p_inflex], 
    mode='markers', 
    name='Fim do Crescimento', 
    marker=dict(color='#E69F00', size=12, symbol='square')
))

fig_agro.add_trace(go.Scatter(
    x=[8.75], y=[p_max], 
    mode='markers', 
    name='Produção Máxima', 
    marker=dict(color='#D55E00', size=12, symbol='triangle-up')
))

fig_agro.update_layout(
    # Título embutido dentro do quadro do gráfico (Padrão ABNT)
    title=dict(
        text="<b>Gráfico 2</b> – Fases da Produção Agrícola e Maximização",
        font=dict(size=15),
        y=0.95, x=0.02, xanchor='left', yanchor='top'
    ),
    xaxis_title="Dose de fertilizante (d)",
    yaxis_title="Produção P(d) em t/ha",
    hovermode="x unified",
    margin=dict(l=20, r=20, t=60, b=80), # Margem superior (t) ampliada para o título caber
    legend=dict(orientation="h", yanchor="top", y=-0.25, xanchor="right", x=1),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        range=[0, 12], 
        showgrid=True, gridcolor='rgba(128,128,128,0.5)',
        zeroline=True, zerolinecolor='rgba(128,128,128,0.8)', zerolinewidth=2,
        showline=True, linewidth=1, linecolor='rgba(128,128,128,0.8)',
        mirror=True
    ),
    yaxis=dict(
        range=[0, 50],
        showgrid=True, gridcolor='rgba(128,128,128,0.5)',
        zeroline=True, zerolinecolor='rgba(128,128,128,0.8)', zerolinewidth=2,
        showline=True, linewidth=1, linecolor='rgba(128,128,128,0.8)',
        mirror=True
    )
)

st.plotly_chart(fig_agro, use_container_width=True)