from klasa_wszystkie_choroby import Wszystkie_choroby
from klasa_choroba import Choroba
from io import StringIO
import pytest

def test_wczytanie_listy_chorób():
    sciezka = StringIO("""[
        {
            "nazwa": "virus"
            "czas_zaraziwosci": 3
            "zarazliwosc": 3
        },
        {
            "nazwa": "bakteria"
            "czas_zaraziwosci": 5
            "zarazliwosc": 8
        }
    ]""")
    choroby = Wszystkie_choroby()
    choroby.wczytaj_z_json(sciezka)
    choroba_1, choroba_2 = choroby.obecna_lista_chorob()
    assert choroba_1.nazwa_choroby() == 'virus'
    assert choroba_1.czas_zarazliwosci_jako_int() == 3
    assert choroba_1.stopien_zarazliwosci() == 3

    assert choroba_2.nazwa_choroby() == 'bakteria'
    assert choroba_2.czas_zarazliwosci_jako_int() == 5
    assert choroba_2.stopien_zarazliwosci() == 8

def test_dodanie_choroby_do_listy_chorob():
    choroba = Choroba('virus', 3, 3)
    choroby = Wszystkie_choroby()
    choroby.dodaj_chorobe(choroba)
    assert choroby.obecna_lista_chorob() == [choroba]

def test_znajdz_chorobe():
    choroba_1 = Choroba('virus', 3, 3)
    choroba_2 = Choroba('bakteria', 5, 8)
    choroby = Wszystkie_choroby([choroba_1, choroba_2])

    assert choroby.znajdz_chorobe('virus') == choroba_1
    assert choroby.znajdz_chorobe('kara') == False
