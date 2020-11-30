def test_romain_to_decimal():
    from calcRomaine.calcRomaine import romain_to_decimal
    #assert romain_to_decimal("V") == 5
    assert romain_to_decimal("VVI") == 11
    assert romain_to_decimal("II") == 2
    assert romain_to_decimal("MMC") == 2100
    assert romain_to_decimal("DCL") == 650
    assert romain_to_decimal("IV") == 4
    assert romain_to_decimal("MCMXLIV") == 1944


