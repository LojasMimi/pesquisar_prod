import streamlit as st
import pandas as pd

# CSV remoto hospedado no GitHub (ajustado com sua URL)
CSV_URL = "https://raw.githubusercontent.com/LojasMimi/pesquisar_prod/refs/heads/main/cad_concatenado.csv"

# Função para carregar dados com cache
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

# Configuração da página
st.set_page_config(
    page_title="PESQUISADOR DE PRODUTOS - LOJAS MIMI",
    page_icon="🛍️",
    initial_sidebar_state="expanded"
)

# Menu lateral de navegação
pagina = st.sidebar.radio("Navegar", ["Pesquisar", "Dados dos produtos", "Sobre"], index=0)

# Título principal
st.title("PESQUISADOR DE PRODUTOS - LOJAS MIMI")

# Carregar dados uma única vez
df = carregar_dados()

# Página de pesquisa
if pagina == "Pesquisar":
    st.subheader("🔍 Pesquisar produto")

    tipo_busca = st.selectbox("Selecione o tipo de código:", ["Código de Barras", "Código VF", "REF"])
    entrada = st.text_input(f"Digite o {tipo_busca.lower()}")

    # Mapeamento atualizado para nomes das colunas reais
    colunas_mapeadas = {
        "Código de Barras": "CODIGO BARRA",
        "Código VF": "VAREJO FACIL",
        "REF": "CODIGO"
    }

    coluna = colunas_mapeadas[tipo_busca]

    if st.button("PESQUISAR"):
        if coluna not in df.columns:
            st.warning(f"A coluna '{coluna}' não foi encontrada no CSV.")
        elif entrada.strip() == "":
            st.warning("Digite um valor para pesquisar.")
        else:
            resultados = df[df[coluna].astype(str).str.contains(entrada, case=False, na=False)]

            if not resultados.empty:
                st.success(f"{len(resultados)} resultado(s) encontrado(s):")
                st.dataframe(resultados)
            else:
                st.warning("Nenhum resultado encontrado.")

# Página de exibição dos dados
elif pagina == "Dados dos produtos":
    st.subheader("📦 Todos os produtos")
    if df.empty:
        st.warning("Nenhum dado carregado.")
    else:
        st.dataframe(df)

# Página de informações
elif pagina == "Sobre":
    st.subheader("ℹ️ Sobre")
    st.markdown("""
    Este aplicativo foi desenvolvido para auxiliar na pesquisa de produtos das **Lojas Mimi**.

    **Funcionalidades:**
    - Pesquisa por Código de Barras, Código VF ou REF
    - Visualização completa da base de produtos
    - Navegação simples e eficiente

    Desenvolvido com ❤️ pela equipe de dados.
    """)
