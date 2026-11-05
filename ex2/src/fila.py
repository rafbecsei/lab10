class Fila:
    def __init__(self):
        self.aguardando = 0
        self.numero_normal = 0
        self.numero_prioridade = 0

    def emitir(self, tipo):
        if tipo == "prioridade":
            self.numero_prioridade += 1
            senha = f"P{self.numero_prioridade}"
        else:
            self.numero_normal += 1
            senha = f"N{self.numero_normal}"

        self.aguardando += 1
        return senha