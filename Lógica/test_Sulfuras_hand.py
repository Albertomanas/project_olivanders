from Sulfuras_hand import Sulfuras_hand


def test_update_item_sulfuras():
    pato = Sulfuras_hand("pato hand", 0, 80)
    pato.update_item()
    assert pato.get_item_updated() == ("pato hand", 0, 80)


def test_update_item_sulfuras_negative_sell_in():
    pato = Sulfuras_hand("pato hand", -1, 80)
    pato.update_item()
    assert pato.get_item_updated() == ("pato hand", -1, 80)
