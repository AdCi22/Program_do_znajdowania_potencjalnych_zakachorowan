from klasa_choroba import Choroba
from json.decoder import JSONDecodeError
import json

"""
Klasa pozwalająca na gromadzenie informacji na temat chorób
Umożliwia:
-dodanie choroby
-znalezienie choroby
-zapisywanie chorób do pliku
-wczytywanie chorób z pliku
"""


class Wszystkie_choroby:
    def __init__(self, lista_chorob=[]):
        self._lista_chorob = lista_chorob

    # Odczyt z pliku wcześniej zarejestrowanych chorób

    def wczytaj_z_json(self, sciezka_odczytu):
        plik = open(sciezka_odczytu)
        try:
            lista_chorob = json.load(plik)
            for choroba_zakazna in lista_chorob:
                nazwa = choroba_zakazna['nazwa']
                czas_zarazliwosci = choroba_zakazna['czas_zarazliwosc']
                zarazliwosc = choroba_zakazna['zarazliwosc']
                wczytana_choroba = Choroba(nazwa, czas_zarazliwosci, zarazliwosc)

                self.dodaj_chorobe(wczytana_choroba)
        except JSONDecodeError:  # Gdy plik z którego czytamy jest pusty omijamy odczyt
            pass


    # Zapis do pliku wszystkich obecnie zarejestrowanych chorób

    def zapisz_do_json(self, sciezka_zapisu):
        lista_chorob = self.obecna_lista_chorob()
        zawartosc_do_zapisania = []
        for choroba in lista_chorob:
            nazwa = choroba.nazwa_choroby()
            czas_zarazliwosci = choroba.czas_zarazliwosci_jako_int()
            zarazliwosc = choroba.stopien_zarazliwosci()
            dane_choroby = {
                'nazwa': nazwa,
                'czas_zarazliwosc': czas_zarazliwosci,
                'zarazliwosc': zarazliwosc
            }
            zawartosc_do_zapisania.append(dane_choroby)
        zawartosc = json.dumps(zawartosc_do_zapisania)
        with open(sciezka_zapisu, "w") as plik:
            plik.write(zawartosc)

    # Zwraca obecną liste chorób

    def obecna_lista_chorob(self):
        return self._lista_chorob

    # Szukanie choroby po nazwie

    def znajdz_chorobe(self, choroba_do_znalezienia):
        for choroba in self.obecna_lista_chorob():
            if choroba_do_znalezienia == str(choroba.nazwa_choroby()):
                return choroba
        return False

    # Dodanie choroby do listy chorób

    def dodaj_chorobe(self, choroba_do_dodania):
        self._lista_chorob.append(choroba_do_dodania)
