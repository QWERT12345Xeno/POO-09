from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO

class Service:
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c)

    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)

    def categoria_listar():
        return CategoriaDAO.listar()

    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)

    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)

    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO.excluir(c)

    def produto_inserir(descricao, preco, estoque, id_categoria):
        p = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(p)

    def produto_listar():
        return ProdutoDAO.listar()

    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)

    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        p = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO.atualizar(p)

    def produto_excluir(id):
        p = Produto(id, "", 0, 0, 0)
        ProdutoDAO.excluir(p)

    def produto_reajustar(percentual):
        for obj in ProdutoDAO.listar():
            novo_preco = obj.get_preco() * (1 + percentual / 100)
            obj.set_preco(novo_preco)
            ProdutoDAO.atualizar(obj)
