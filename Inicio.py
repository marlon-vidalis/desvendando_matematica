import streamlit as st

# Configuração básica da página
st.set_page_config(
    page_title="Desvendando Matemática",
    page_icon="📐",
    layout="centered" # 'centered' deixa o texto mais confortável para leitura que o 'wide'
)

# Título baseado no README
st.title("📐 Desvendando Matemática")

# Introdução baseada no README
st.markdown("""
Material didático interativo para explorar conceitos matemáticos por meio de explicações, gráficos e experimentação.

A proposta é aproximar a explicação teórica da exploração visual dos conceitos. As funções e seus gráficos não aparecem apenas como ilustrações: você pode interagir com as representações gráficas e observar como diferentes funções se comportam.
""")

st.divider()

# Módulo de Cálculo
st.header("📚 Módulo: Cálculo I")
st.markdown("Selecione um dos conteúdos abaixo para iniciar:")

# Botões clicáveis (alto contraste e fáceis de identificar)
if st.button("1️⃣ Análise de gráficos via derivadas", use_container_width=True):
    st.switch_page("pages/1_Analise_de_graficos_via_derivadas.py")

if st.button("2️⃣ Teorema de Rolle e do Valor Médio", use_container_width=True):
    st.switch_page("pages/2_Teorema_de_Rolle_e_Valor_Medio.py")

if st.button("3️⃣ Testes da 1ª e 2ª Derivada", use_container_width=True):
    st.switch_page("pages/3_Testes_da_1a_e_2a_Derivada.py")