from fila import Fila


def test_fila_inicia_vazia():
    fila = Fila()
    assert fila.aguardando == 0