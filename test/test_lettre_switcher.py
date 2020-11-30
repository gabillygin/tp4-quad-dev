def test_val_lettre():
    from calcRomaine.lettre_switcher import  val_lettre
    assert val_lettre('I') == 1
    assert val_lettre('V') == 5
    assert val_lettre('X') == 10
    assert val_lettre('L') == 50
    assert val_lettre('C') == 100
    assert val_lettre('D') == 500
    assert val_lettre('M') == 1000
