from klasa_wszystkie_spotkania import Wszystkie_spotkania
from klasa_spotkanie import Spotkanie
from datetime import date


def test_stworzenie_listy_spotkan():
    spotkania_w_systemie = Wszystkie_spotkania()
    assert spotkania_w_systemie.wszystkie_spotkania() == []


def test_dodawanie_spotkania():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    spotkania_w_systemie = Wszystkie_spotkania()
    spotkania_w_systemie.dodaj_spotkanie(spotkanie)
    assert spotkania_w_systemie.wszystkie_spotkania() == [spotkanie]


def test_znalezienie_spotkania_osoby():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    spotkania_w_systemie = Wszystkie_spotkania([spotkanie])
    assert spotkania_w_systemie.znajdz_wszystkie_spotkania_osoby(1) == spotkanie


def test_znalezienia_spotkan_w_zakresie_czasu():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    spotkania_w_systemie = Wszystkie_spotkania([spotkanie])
    assert spotkania_w_systemie.spotkanie_w_danym_zakresie(date(1, 1, 1), date(1, 1, 3)) == spotkanie


def test_znalezienia_spotkan_osoby_w_zakresie_czasu():
    id_osob = [1, 2]
    poczatek_spotkania = date(1, 1, 1)
    koniec_spotkania = date(1, 1, 2)
    spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania)
    spotkania_w_systemie = Wszystkie_spotkania([spotkanie])
    assert spotkania_w_systemie.znajdz_spotkania_osoby_w_zakresie(1, date(1, 1, 1), date(1, 1, 3)) == spotkanie
