def test_romain_to_decimal():
    from calcRomaine.calcRomaine import romain_to_decimal
    assert romain_to_decimal("V") == 5
    assert romain_to_decimal("VVI") == 11
    assert romain_to_decimal("II") == 2
    assert romain_to_decimal("MMC") == 2100
    assert romain_to_decimal("DCL") == 650
    assert romain_to_decimal("IV") == 4
    assert romain_to_decimal("MCMXLIV") == 1944


def test_add():
    from calcRomaine.calcRomaine import add
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
    assert add(0, 3) == 3
    assert add(2, 0) == 2


def test_sous():
    from calcRomaine.calcRomaine import sous
    assert sous(2, 3) == -1
    assert sous(-2, 3) == -5
    assert sous(2, -3) == 5
    assert sous(0, 3) == -3
    assert sous(2, 0) == 2


def test_mul():
    from calcRomaine.calcRomaine import mul
    assert mul(2, 3) == 6
    assert mul(-2, 3) == -6
    assert mul(2, -3) == -6
    assert mul(0, 3) == 0
    assert mul(2, 0) == 0


def test_div():
    from calcRomaine.calcRomaine import div
    assert div(10, 2) == 5
    assert div(2, 0) == -1


def test_caltos_romaine():
    from calcRomaine.calcRomaine import caltos_romaine
    assert caltos_romaine("VVI", "I", '-') == 10
    assert caltos_romaine("MCMXLIV", "III", '+') == 1947
    assert caltos_romaine("VI", "VV", '*') == 60
    assert caltos_romaine("XXIV", "VI", '/') == 4
    assert caltos_romaine("VI","VV",'') == -1

