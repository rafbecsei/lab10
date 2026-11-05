class Fila:
    def __init__(self):
        self.aguardando = 0
        self.numero_normal = 0
        self.numero_prioridade = 0
        self.fila_normal = []

    def emitir(self, tipo):
        if tipo == "prioridade":
            self.numero_prioridade += 1
            senha = f"P{self.numero_prioridade}"
        else:
            self.numero_normal += 1
            senha = f"N{self.numero_normal}"
            self.fila_normal.append(senha)

        self.aguardando += 1
        return senha

    def chamar(self):
        senha = self.fila_normal.pop(0)
        self.aguardando -= 1
        return senha