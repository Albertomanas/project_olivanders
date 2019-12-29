from aged_brie import Aged_brie


def update_quality_Aged_brie():
    assert ("pato", 2, 0) == Aged_brie.update_quality("pato", 1, 1)
    assert ("pato", 0, 2) == Aged_brie.update_quality("pato", -1, 4)
