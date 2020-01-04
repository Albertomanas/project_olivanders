from Backstage_pass import Backstage_pass


def test_update_item():
    pato = Backstage_pass("pato pass", 15, 20)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", 14, 21)


def test_update_item_max_quality():
    pato = Backstage_pass("pato pass", 5, 50)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", 4, 50)


def test_update_item_ten():
    pato = Backstage_pass("pato pass", 10, 20)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", 9, 22)


def test_update_item_sell_in_one():
    pato = Backstage_pass("pato pass", 1, 20)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", 0, 25)


def test_update_item_passed_concert():
    pato = Backstage_pass("pato pass", 0, 50)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", -1, 0)
