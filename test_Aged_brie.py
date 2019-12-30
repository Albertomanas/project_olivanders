from aged_brie import Aged_brie


def test_update_quality_Aged_brie():
    assert 2 == Aged_brie("pato", 1, 1).update_quality
    assert 6 == Aged_brie.("pato", -1, 4).update_quality
