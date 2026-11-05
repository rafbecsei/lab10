from contador import contar_palavras


def test_texto_vazio():
    assert contar_palavras("") == {}


def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}

def test_duas_palavras():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}

def test_palavras_repetidas():
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}

def test_maiusculas_minusculas():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}

def test_pontuacao_final():
    assert contar_palavras("fim. Fim!") == {"fim": 2}