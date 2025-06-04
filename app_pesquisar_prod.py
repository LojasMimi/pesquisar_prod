import streamlit as st
import pandas as pd

# CSV remoto (exemplo de URL pública do GitHub, substitua pelo seu link real)
CSV_URL = "https://raw.githubusercontent.com/LojasMimi/pesquisar_prod/refs/heads/main/cad_concatenado.csv"

@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

# Página principal
st.set_page_config(page_title="PESQUISADOR DE PRODUTOS - LOJAS MIMI", page_icon="🛍️", initial_sidebar_state="expanded")

# Navegação
pagina = st.sidebar.radio("Navegar", ["Pesquisar", "Dados dos produtos", "Sobre"], index=0)

# Título fixo em todas as páginas
st.title("PESQUISADOR DE PRODUTOS - LOJAS MIMI")

# Carregamento do dataset
df = carregar_dados()

if pagina == "Pesquisar":
    st.subheader("🔍 Pesquisar produto")

    tipo_busca = st.selectbox("Selecione o tipo de código:", ["Código de Barras", "Código VF", "REF"])
    entrada = st.text_input(f"Digite o {tipo_busca.lower()}")

    if entrada:
        colunas_mapeadas = {
            "Código de Barras": "codigo_barras",
            "Código VF": "codigo_vf",
            "REF": "ref"
        }

        coluna = colunas_mapeadas[tipo_busca]

        if coluna not in df.columns:
            st.warning(f"A coluna '{coluna}' não existe no CSV.")
        else:
            resultados = df[df[coluna].astype(str).str.contains(entrada, case=False, na=False)]

            if not resultados.empty:
                st.success(f"{len(resultados)} resultado(s) encontrado(s):")
                st.dataframe(resultados)
            else:
                st.warning("Nenhum resultado encontrado.")

elif pagina == "Dados dos produtos":
    st.subheader("📦 Todos os produtos")
    if df.empty:
        st.warning("Nenhum dado carregado.")
    else:
        st.dataframe(df)

elif pagina == "Sobre":
    st.subheader("ℹ️ Sobre")
    st.markdown("""
    Este aplicativo foi desenvolvido para auxiliar na pesquisa de produtos das **Lojas Mimi**.
    
    **Funcionalidades:**
    - Pesquisa por Código de Barras, Código VF ou REF
    - Visualização dos dados completos
    - Projeto simples usando Python + Streamlit
    
    Desenvolvido com ❤️ por sua equipe de dados.
    """)
