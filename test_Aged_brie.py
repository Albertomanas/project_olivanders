from aged_brie import Aged_brie


def test_quality_major_zero():
    pato = Aged_brie("pato", 2, 0)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 1)


def test_sell_in_less_zero_item():
    pato = Aged_brie("pato", 0, 2)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -1, 4)

# Casos test random para testear codigo


def test_normal_case_one():
    pato = Aged_brie("pato", -2, 30)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", -3, 32)


def test_normal_case_two():
    pato = Aged_brie("pato", 2, 40)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 1, 41)


def test_normal_case_three():
    pato = Aged_brie("pato", 3, 26)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 27)

# Fin "random"


def test_quality_not_more_fifty():
    pato = Aged_brie("pato", 3, 56)
    pato.update_item()
    assert pato.get_item_updated() == ("pato", 2, 50)
