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

def test_primeira_senha_prioritaria():
    fila = Fila()

    assert fila.emitir("prioridade") == "P1"
    assert fila.aguardando == 1

def test_numeracao_independente():
    fila = Fila()

    assert fila.emitir("normal") == "N1"
    assert fila.emitir("prioridade") == "P1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("prioridade") == "P2"
    assert fila.aguardando == 4

def test_chamar_senha_normal():
    fila = Fila()

    fila.emitir("normal")

    assert fila.chamar() == "N1"
    assert fila.aguardando == 0

def test_prioridade_antes_da_normal():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioridade")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
    assert fila.aguardando == 0

def test_normal_apos_duas_prioridades():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioridade")
    fila.emitir("prioridade")
    fila.emitir("prioridade")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "P3"
    assert fila.aguardando == 0

import pytest


def test_chamar_fila_vazia():
    fila = Fila()

    with pytest.raises(IndexError):
        fila.chamar()

def test_tipo_invalido():
    fila = Fila()

    with pytest.raises(ValueError):
        fila.emitir("vip")