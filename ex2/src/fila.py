class Fila:
    def __init__(self):
        self.aguardando = 0
        self.numero_normal = 0
        self.numero_prioridade = 0
        self.fila_normal = []
        self.fila_prioridade = []

    def emitir(self, tipo):
        if tipo == "prioridade":
            self.numero_prioridade += 1
            senha = f"P{self.numero_prioridade}"
            self.fila_prioridade.append(senha)
        else:
            self.numero_normal += 1
            senha = f"N{self.numero_normal}"
            self.fila_normal.append(senha)

        self.aguardando += 1
        return senha

    def chamar(self):
        if self.fila_prioridade:
            senha = self.fila_prioridade.pop(0)
        else:
            senha = self.fila_normal.pop(0)

        self.aguardando -= 1
        return senha