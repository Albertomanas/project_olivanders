from Normal_item import Normal_item


def test_update_quality_normal_item():
    pato = Normal_item("pato", 2, 2)
    pato.update_quality()
    assert pato.get_quality() == 1


def test_update_sell_in_normal_item():
    pato = Normal_item("pato", 2, 2)
    pato.update_sell_in()
    assert pato.get_sell_in() == 1


def test_quality_not_negative_normal_item():
    pato = Normal_item("pato", 2, 0)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 0)


def test_sell_in_less_zero_item():
    pato = Normal_item("pato", 0, 2)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -1, 0)

# Casos test random para testear codigo


def test_random_uno():
    pato = Normal_item("pato", -2, 30)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -3, 28)


def test_random_dos():
    pato = Normal_item("pato", 2, 40)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 39)


def test_random_tres():
    pato = Normal_item("pato", 3, 26)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 25)

# Fin "random"


def test_quality_not_more_fifty():
    pato = Normal_item("pato", 3, 56)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 50)
