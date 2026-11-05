def contar_palavras(texto):
    if not texto:
        return {}

    palavras = texto.split()
    resultado = {}

    for palavra in palavras:
        resultado[palavra] = resultado.get(palavra, 0) + 1

    return resultado