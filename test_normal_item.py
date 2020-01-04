from normal_item import Normal_item


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
