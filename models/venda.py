import json
from datetime import datetime

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.__id = id
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        self.__id_cliente = id_cliente

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_carrinho(self): return self.__carrinho
    def get_total(self): return self.__total
    def get_id_cliente(self): return self.__id_cliente

    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_carrinho(self, carrinho): self.__carrinho = carrinho
    def set_total(self, total): self.__total = total
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__total:.2f}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.isoformat(),
            "carrinho": self.__carrinho,
            "total": self.__total,
            "id_cliente": self.__id_cliente
        }

class VendaDAO:
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
            with open("vendas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Venda(dic["id"], datetime.fromisoformat(dic["data"]), dic["carrinho"], dic["total"], dic["id_cliente"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Venda.to_json)
