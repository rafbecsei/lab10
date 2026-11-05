class Fila:
    def __init__(self):
        self.aguardando = 0
        self.numero_normal = 0

    def emitir(self, tipo):
        self.numero_normal += 1
        self.aguardando += 1
        return f"N{self.numero_normal}"