from Backstage_pass import Backstage_pass
from Normal_item import Normal_item


def test_update_quality_normal_item():
    pato = Backstage_pass("pato pass", 15, 20)
    pato.update_item()
    assert pato.get_item_updated() == ("pato pass", 14, 21)