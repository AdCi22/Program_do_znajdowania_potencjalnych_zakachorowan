from klasa_choroba import Choroba


def test_zwrocenie_nazwy_choroby():
    choroba = Choroba('virus', 3, 3)
    assert choroba.nazwa_choroby() == 'virus'


def test_zwrócenie_czasu_zarazliwosci():
    choroba = Choroba('virus', 3, 3)
    assert choroba.czas_zarazliwosci_jako_int() == 3


def test_zwrócenie_stopnia_zarazliwosci():
    choroba = Choroba('virus', 3, 3)
    assert choroba.stopien_zarazliwosci == 3
