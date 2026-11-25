import json

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__id_categoria = id_categoria

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_estoque(self): return self.__estoque
    def get_id_categoria(self): return self.__id_categoria

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_preco(self, preco): self.__preco = preco
    def set_estoque(self, estoque): self.__estoque = estoque
    def set_id_categoria(self, id_categoria): self.__id_categoria = id_categoria

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco:.2f} - {self.__estoque}"

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "id_categoria": self.__id_categoria
        }

class ProdutoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_categoria"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Produto.to_json)
