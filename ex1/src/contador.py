def contar_palavras(texto):
    if not texto:
        return {}

    palavras = texto.split()
    resultado = {}

    for palavra in palavras:
        resultado[palavra] = 1

    return resultado