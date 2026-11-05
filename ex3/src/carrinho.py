CUPONS = {
    "DEZ": {"desconto": 10, "minimo": 10000},
    "VINTE": {"desconto": 20, "minimo": 30000},
}


class Carrinho:
    def __init__(self):
        self._subtotal = 0
        self._cupom = None

    def adicionar(self, preco, quantidade=1):
        if preco <= 0:
            raise ValueError("preco deve ser positivo")

        if type(quantidade) is not int or quantidade < 1:
            raise ValueError("quantidade deve ser inteira e maior ou igual a 1")

        self._subtotal += preco * quantidade

    def aplicar_cupom(self, codigo):
        if codigo not in CUPONS:
            raise ValueError("cupom desconhecido")

        self._cupom = codigo

    @property
    def total(self):
        if self._cupom is None:
            return self._subtotal

        cupom = CUPONS[self._cupom]

        if self._subtotal < cupom["minimo"]:
            return self._subtotal

        return self._subtotal * (100 - cupom["desconto"]) // 100