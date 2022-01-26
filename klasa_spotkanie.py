"""
Klasa określająca podstawowe parametry spotkania czyli:
-ID osób biorących udział na spotkaniu
-data początku spotkania
-data końca spotkania
-choroba(domyślnie brak)

Dodatkową funkcjonalnością jest sprawdzanie
czy osoba o danym ID jest na spotkaniu
"""


class Spotkanie:
    def __init__(self, id_osob, poczatek_spotkania, koniec_spotkania, choroba='nie', stan_zdrowia="zdrowy"):
        self._id_osob = id_osob  # lista
        self._poczatek_spotkania = poczatek_spotkania
        self._koniec_spotkania = koniec_spotkania
        self._choroba = choroba
        self._stan_zdrowia = stan_zdrowia

    # Zwrócenie wszystkich informacji na temat spotkania czyli:
    # Id osób na spotkaniu, daty początku spotkania i jego końca

    def data_i_osoby(self):
        return self._id_osob, self._poczatek_spotkania, self._koniec_spotkania

    # Zwraca ID osób na spotkaniu

    def osoby_na_spotkaniu(self):
        return self._id_osob

    # Zwraca date początku spotkania

    def poczatek_spotkania(self):
        return self._poczatek_spotkania

    # Zwraca date konca spotkania

    def koniec_spotkania(self):
        return self._koniec_spotkania

    # Sprawdzenie czy osoba o podanym ID jest na spotkaniu

    def sprawdz_czy_jest_osoba(self, id_osoby_do_znalezienia):
        for id_osoby in self._id_osob:
            if id_osoby == id_osoby_do_znalezienia:
                return True

    # Sprawdzenie choroby zakaznej spotkania

    def choroba_zakazna(self):
        return self._choroba

    # Sprawdzenie stanu zdrowia na spotkaniu

    def zdrowie(self):
        return self._stan_zdrowia
