from klasa_spotkanie import Spotkanie
from datetime import date


def test_stworzenie_spotkania():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    assert spotkanie.data_i_osoby() == ([1, 2], poczatek_spotkania, koniec_spotkania)


def test_zwrocenie_listy_osob_na_spotkaniu():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    assert spotkanie.osoby_na_spotkaniu() == [1, 2]


def test_zwrocenie_daty_poczatku_spotkania():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    assert spotkanie.poczatek_spotkania() == poczatek_spotkania


def test_zwrocenie_daty_konca_spotkania():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    assert spotkanie.koniec_spotkania() == koniec_spotkania


def test_sprawdzenie_czy_jest_osoba_na_spotkaniu():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    assert spotkanie.sprawdz_czy_jest_osoba(1) is True
    assert spotkanie.sprawdz_czy_jest_osoba(3) is False


def test_stworzenie_spotkania_z_choroba():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania, 'symboliczna choroba')
    assert spotkanie.choroba_zakazna() == 'symboliczna choroba'

def test_szukanie_spotkania_z_choroba():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania, 'symboliczna choroba')
    assert spotkanie.spotkanie_z_choroba('symboliczna choroba') == spotkanie
