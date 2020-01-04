from normal_item import Normal_item


def test_update_quality_normal_item():
    pato = Normal_item("pato", 2, 2)
    pato.update_quality()
    assert pato.get_quality() == 1


def test_update_sell_in_normal_item():
    pato = Normal_item("pato", 2, 2)
    pato.update_sell_in()
    assert pato.get_sell_in() == 1