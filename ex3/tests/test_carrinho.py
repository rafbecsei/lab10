import pytest
from carrinho import Carrinho


def test_carrinho_vazio():
    assert Carrinho().total == 0

def test_um_item():
    c = Carrinho()
    c.adicionar(2500)
    assert c.total == 2500

def test_item_com_quantidade():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000

def test_preco_zero_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)

def test_cupom_dez():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")
    assert c.total == 5000

def test_cupom_desconhecido():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")

def test_item_depois_do_cupom():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)
    assert c.total == 1000

def test_cupom_dez_no_valor_minimo():
    c = Carrinho()
    c.adicionar(10000)
    c.aplicar_cupom("DEZ")
    assert c.total == 9000

def test_cupom_vinte_no_valor_minimo():
    c = Carrinho()
    c.adicionar(30000)
    c.aplicar_cupom("VINTE")
    assert c.total == 24000

def test_cupom_vinte_abaixo_do_minimo():
    c = Carrinho()
    c.adicionar(29999)
    c.aplicar_cupom("VINTE")
    assert c.total == 29999

def test_desconto_ao_atingir_minimo():
    c = Carrinho()
    c.adicionar(5000)
    c.aplicar_cupom("DEZ")

    assert c.total == 5000

    c.adicionar(5000)
    assert c.total == 9000

def test_segundo_cupom_substitui_primeiro():
    c = Carrinho()
    c.adicionar(30000)

    c.aplicar_cupom("DEZ")
    assert c.total == 27000

    c.aplicar_cupom("VINTE")
    assert c.total == 24000

def test_quantidade_zero_rejeitada():
    c = Carrinho()

    with pytest.raises(ValueError):
        c.adicionar(2500, quantidade=0)