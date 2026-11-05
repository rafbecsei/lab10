def contar_palavras(texto):
    if not texto:
        return {}

    palavras = texto.split()
    resultado = {}

    for palavra in palavras:
        palavra = palavra.lower()
        resultado[palavra] = resultado.get(palavra, 0) + 1

    return resultado