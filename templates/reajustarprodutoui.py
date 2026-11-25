import streamlit as st
import time
from service import Service

class ReajustarProdutoUI:
    def main():
        st.header("Reajustar Preço de Produtos")
        ReajustarProdutoUI.reajustar()

    def reajustar():
        percentual = st.number_input("Informe o percentual de reajuste (%)", format="%.2f")
        if st.button("Reajustar"):
            Service.produto_reajustar(percentual)
            st.success("Preços reajustados com sucesso")
            time.sleep(2)
            st.rerun()
