import streamlit as st

# Configuração básica da página, sem ícones
st.set_page_config(
    page_title="Desvendando Matemática",
    layout="centered"
)

# ==========================================
# BARRA LATERAL CUSTOMIZADA (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("### Navegação")
    st.page_link("Inicio.py", label="Início")
    
    with st.expander("Módulo: Cálculo I"):
        st.page_link("pages/1_Analise_de_graficos_via_derivadas.py", label="Análise de gráficos via derivadas")
        st.page_link("pages/2_Teorema_de_Rolle_e_Valor_Medio.py", label="Teorema de Rolle e do Valor Médio")
        st.page_link("pages/3_Testes_da_1a_e_2a_Derivada.py", label="Testes da 1ª e 2ª Derivada")

# ==========================================
# CORPO DA PÁGINA PRINCIPAL
# ==========================================
st.title("Desvendando Matemática")

st.markdown("""
Material didático interativo para explorar conceitos matemáticos por meio de explicações, gráficos e experimentação.

A proposta é aproximar a explicação teórica da exploração visual dos conceitos. As funções e seus gráficos não aparecem apenas como ilustrações: você pode interagir com as representações gráficas e observar como diferentes funções se comportam.
""")

st.divider()

st.subheader("Conteúdo")

# Expansor no corpo da página
with st.expander("Módulo: Cálculo I"):
    st.page_link("pages/1_Analise_de_graficos_via_derivadas.py", label="Análise de gráficos via derivadas")
    st.page_link("pages/2_Teorema_de_Rolle_e_Valor_Medio.py", label="Teorema de Rolle e do Valor Médio")
    st.page_link("pages/3_Testes_da_1a_e_2a_Derivada.py", label="Testes da 1ª e 2ª Derivada")