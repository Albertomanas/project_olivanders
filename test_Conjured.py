from conjured import Conjured


def test_quality_not_negative_Conjured():
    pato = Conjured("pato", 2, 0)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 0)


def test_sell_in_less_zero_item():
    pato = Conjured("pato", 0, 2)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -1, 0)

# Casos test random para testear codigo


def test_random_uno():
    pato = Conjured("pato", -2, 30)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -3, 26)


def test_random_dos():
    pato = Conjured("pato", 2, 40)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 38)


def test_random_tres():
    pato = Conjured("pato", 3, 26)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 24)

# Fin "random"


def test_quality_not_more_fifty():
    pato = Conjured("pato", 3, 56)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 50)
