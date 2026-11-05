from fila import Fila


def test_fila_inicia_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_primeira_senha_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.aguardando == 1

def test_duas_senhas_normais():
    fila = Fila()

    assert fila.emitir("normal") == "N1"
    assert fila.emitir("normal") == "N2"
    assert fila.aguardando == 2