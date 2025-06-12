
# 🛍️ Pesquisador de Produtos – Lojas Mimi

Este aplicativo web foi desenvolvido com [**Streamlit**](https://streamlit.io/) para facilitar o trabalho dos colaboradores das **Lojas Mimi**, permitindo uma pesquisa rápida e eficiente de informações sobre produtos, sem a necessidade de abrir manualmente diversas planilhas ou navegar entre abas.

## 🚀 Objetivo

O sistema visa otimizar o tempo gasto pelos auxiliares de escritório e demais colaboradores, centralizando em um único local a consulta por códigos de barras, códigos internos (VF) e referências de produtos.

## 🔎 Funcionalidades

* **Pesquisa inteligente** por:

  * Código de Barras
  * Código VF (Varejo Fácil)
  * Código do Fornecedor (REF)

* **Visualização completa** da base de produtos em formato de tabela interativa

* **Interface amigável e responsiva**, com navegação por menu lateral

* **Carregamento automático** de dados a partir de um arquivo CSV hospedado no GitHub

## 🧱 Tecnologias Utilizadas

* [Python 3.8+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)

## 🛠️ Como Usar

1. Clone este repositório, baixe o código ou acesse [esse link](https://mimi-pesquisar-itens.streamlit.app/).
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:

   ```bash
   streamlit run fazer_pedidos.py
   ```
4. Acesse no navegador:

   ```
   http://localhost:8501
   ```

> **Observação:** o aplicativo carrega os dados automaticamente de um arquivo CSV hospedado no GitHub:
> [`cad_concatenado.csv`](https://github.com/LojasMimi/pesquisar_prod/blob/main/cad_concatenado.csv)

## 👨‍💻 Autor

Desenvolvido por [**Pablo Dantas**](https://github.com/opablodantas) para uso exclusivo das **Lojas Mimi**.

## 📄 Licença

Este projeto é privado e de uso interno. Todos os direitos reservados.

---
