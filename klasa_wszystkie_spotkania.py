from ast import Str
from klasa_spotkanie import Spotkanie
from json.decoder import JSONDecodeError
from datetime import date
import json

"""
Klasa pozwalająca na gromadzenie informacji na temat spotkań
Umożliwia:
-wyszukiwanie spotkania ze względu na:
    a)czas spotkania
    b)uczestników
    c)chorobe
-dodawać nowe spotkania
-zapisywać spotkania do pliku
-wczytywać spotkania z pliku
"""

class Wszystkie_spotkania:
    def __init__(self, lista_wszystkich_spotkan=[]):
        self._lista_wszystkich_spotkan = lista_wszystkich_spotkan

    # Zwrócenie listy ze wszystkimi odnotowanymi spotkaniami

    def wszystkie_spotkania(self):
        return self._lista_wszystkich_spotkan

    # Dodanie spotkania do listy wszystkich spotkań

    def dodaj_spotkanie(self, spotkanie_do_dodania):
        for spotkanie in self.wszystkie_spotkania():
            if spotkanie.data_i_osoby() == spotkanie_do_dodania.data_i_osoby():
                return None
        self.wszystkie_spotkania().append(spotkanie_do_dodania)

    # Szukanie spotkania ze względu na szukaną osobe

    def znajdz_wszystkie_spotkania_osoby(self, id_osoba):
        lista_spotkan = []
        for spotkanie in self._lista_wszystkich_spotkan:
            if spotkanie.sprawdz_czy_jest_osoba(id_osoba):
                lista_spotkan.append(spotkanie)
        return lista_spotkan

    # Szukanie spotkania ze względu na czas spotkania

    def spotkania_w_danym_zakresie(self, lista_spotkan, data_poczatkowa, data_koncowa):
        lista_spotkan_w_danym_okresie = []

        for spotkanie in lista_spotkan:
            if spotkanie.koniec_spotkania() <= data_koncowa and spotkanie.poczatek_spotkania() >= data_poczatkowa:
                    lista_spotkan_w_danym_okresie.append(spotkanie)
        return lista_spotkan_w_danym_okresie

    # Szukanie spotkania ze względu na czas spotkania i osobe

    def znajdz_spotkania_osoby_w_zakresie(self, id_osoby, data_poczatkowa, data_koncowa):
        lista_spotkan = self.znajdz_wszystkie_spotkania_osoby(id_osoby)
        spotkania = self.spotkania_w_danym_zakresie(lista_spotkan, data_poczatkowa, data_koncowa)
        return spotkania

    # Szukanie spotkan po chorobie

    def _spotkania_z_choroba(self, szukana_choroba):
        lista_spotkan_z_choroba = []
        for spotkanie in self.wszystkie_spotkania():
            if (spotkanie.choroba_zakazna()) == str(szukana_choroba):
                lista_spotkan_z_choroba.append(spotkanie)
        return lista_spotkan_z_choroba 

    # Szukanie spotkan po chorobie i podejrzeniu/zakazeniu

    def spotkania_z_choroba_i_stanem_zdrowia(self, szukana_choroba='nie', stan_zdrowia='zdrowy'):
        lista_spotkan_z_choroba = self._spotkania_z_choroba(str(szukana_choroba))
        szukane_spotkania = []
        for spotkanie in lista_spotkan_z_choroba:
            if spotkanie.zdrowie() == stan_zdrowia:
                szukane_spotkania.append(spotkanie)
        return szukane_spotkania

    # Formatuj reprezentacje daty typu date na liste wartości int

    def _konwertowanie_daty_na_int(self, data_do_zmiany):
        rok = int('{:%Y}'.format(data_do_zmiany))
        miesiac = int('{:%m}'.format(data_do_zmiany))
        dzien = int('{:%d}'.format(data_do_zmiany))
        data_po_konwertowaniu = [rok, miesiac, dzien]
        return data_po_konwertowaniu

    # Formatuj reprezentacje daty z listy wartości int na date

    def _konwertowanie_daty_na_date(self, data_do_zmiany):
        rok = int(data_do_zmiany[0])
        miesiac = int(data_do_zmiany[1])
        dzien = int(data_do_zmiany[2])
        data_po_konwertowaniu = date(rok, miesiac, dzien)
        return data_po_konwertowaniu

    # Odczyt z pliku wcześniejszych spotkań

    def wczytaj_z_json(self, wszystkie_choroby, sciezka_odczytu):
        with open(sciezka_odczytu, 'r') as plik:
            try:
                dane_z_pliku = json.load(plik)
                for spotkanie in dane_z_pliku:
                    id_osob = spotkanie['id_osob']
                    poczatek_spotkania = self._konwertowanie_daty_na_date(spotkanie['poczatek_spotkania'])
                    koniec_spotkania = self._konwertowanie_daty_na_date(spotkanie['koniec_spotkania'])
                    nazwa_choroby = spotkanie['nazwa_choroby']   
                    stan_zdrowia = spotkanie['stan_zdrowia']
                    wczytane_spotkanie = Spotkanie(id_osob, poczatek_spotkania, koniec_spotkania, nazwa_choroby, stan_zdrowia)
                    self.dodaj_spotkanie(wczytane_spotkanie)
            except JSONDecodeError:  # Gdy plik z którego czytamy jest pusty omijamy odczyt
                pass

    # Zapis do pliku wszystkich spotkań

    def zapisz_do_json(self, sciezka_zapisu):

        lista_spotkan = self.wszystkie_spotkania()
        zawartosc_do_zapisania = []
        for spotkanie in lista_spotkan:
            id_osob, poczatek_spotkania, koniec_spotkania = spotkanie.data_i_osoby()

            nazwa_choroby = spotkanie.choroba_zakazna()

            stan_zdrowia = spotkanie.zdrowie()
            dane_spotkania = {
                'id_osob': id_osob,
                'poczatek_spotkania': self._konwertowanie_daty_na_int(poczatek_spotkania),
                'koniec_spotkania': self._konwertowanie_daty_na_int(koniec_spotkania),
                'nazwa_choroby': nazwa_choroby,
                'stan_zdrowia': stan_zdrowia
            }
            zawartosc_do_zapisania.append(dane_spotkania)
        zawartosc = json.dumps(zawartosc_do_zapisania)

        with open(sciezka_zapisu, "w") as plik:
            plik.write(zawartosc)
