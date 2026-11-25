import streamlit as st
import time
from service import Service

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produtos: list_dic.append(obj.to_json())
            st.dataframe(list_dic)

    def inserir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            descricao = st.text_input("Informe a descrição")
            preco = st.number_input("Informe o preço", min_value=0.0, format="%.2f")
            estoque = st.number_input("Informe o estoque", min_value=0, step=1)
            cat = st.selectbox("Informe a categoria", categorias)
            if st.button("Inserir"):
                Service.produto_inserir(descricao, preco, int(estoque), cat.get_id())
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            preco = st.number_input("Novo preço", value=float(op.get_preco()), min_value=0.0, format="%.2f")
            estoque = st.number_input("Novo estoque", value=int(op.get_estoque()), min_value=0, step=1)
            cat_atual = Service.categoria_listar_id(op.get_id_categoria())
            idx = 0
            for i in range(len(categorias)):
                if cat_atual != None and categorias[i].get_id() == cat_atual.get_id():
                    idx = i
            cat = st.selectbox("Nova categoria", categorias, index=idx)
            if st.button("Atualizar"):
                id = op.get_id()
                Service.produto_atualizar(id, descricao, preco, int(estoque), cat.get_id())
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = Service.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.produto_excluir(id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()
