from klasa_czlowiek import Czlowiek
from json.decoder import JSONDecodeError
import json

"""
Klasa pozwalająca na gromadzenie informacji na temat populacji
Umożliwia:
-automatyczne przyporządkowywanie ID do osoby
-znalezienie osoby po ID
-znalezienie ID osoby po imieniu
-dodanie osoby
-zapisywać osoby i ich ID do pliku
-wczytywać osoby i ich ID z pliku

"""


class Populacja:
    def __init__(self, lista_osob=None):
        self._obecnie_najwyzsze_id = 0
        self._lista_osob = lista_osob if lista_osob else []
        self.dodaj_id_do_osoby(self._lista_osob)

    # Przypisanie nowej wartości najwyższego ID dzięki której ustalane są kolejne ID

    def ustaw_najwyzsze_id(self, najwyzsze_id):
        self._obecnie_najwyzsze_id = najwyzsze_id

    # Odczyt z pliku wcześniej zarejestrowanych osób

    def wczytaj_z_json(self, sciezka_odczytu):
        plik = open(sciezka_odczytu)
        try:
            dane_z_pliku = json.load(plik)
            for osoba in dane_z_pliku:
                imie = osoba['imie']
                id = osoba['id']
                wczytana_osoba = Czlowiek(imie, id)
                self.dodaj_osobe_do_listy(wczytana_osoba)
            self.ustaw_najwyzsze_id(wczytana_osoba.id_osoby())
        except JSONDecodeError:  # Gdy plik z którego czytamy jest pusty omijamy odczyt
            pass

    # Zapisz do pliku wszystkie zarejestrowane osoby

    def zapisz_do_json(self, sciezka_zapisu):
        lista_ludzi = self.pokaz_liste_osob()
        zawartosc_do_zapisania = []
        for osoba in lista_ludzi:
            imie = osoba.imie_osoby()
            id = osoba.id_osoby()
            dane_osoby = {
                'imie': imie,
                'id': id
            }
            zawartosc_do_zapisania.append(dane_osoby)

        zawartosc = json.dumps(zawartosc_do_zapisania)

        with open(sciezka_zapisu, "w") as plik:
            plik.write(zawartosc)

    # Sprawdzenie czy ktoś o podanym ID znajduje sie w systemie

    def sprawdz_poprawnosc_id(self, id_do_sprawdzenia):
        if int(id_do_sprawdzenia) < 0 or int(id_do_sprawdzenia) > self._obecnie_najwyzsze_id:
            return True
        else:
            return False

    # Zwraca obecną liste osób

    def pokaz_liste_osob(self):
        return self._lista_osob

    # Dodaje ID do osoby

    def dodaj_id_do_osoby(self, osoby):
        for osoba in osoby:
            self.dodaj_id(osoba)

    # Przyporzątkowuje odpowiednie ID do osoby

    def dodaj_id(self, osoba):
        if osoba.id_osoby() is None:
            najwyzsze_id = self._obecnie_najwyzsze_id
            osoba.ustaw_id(najwyzsze_id)
            self._obecnie_najwyzsze_id += 1

    # Po przypisaniu ID dodaje osobe do listy ludzi

    def dodaj_osobe_do_listy(self, osoba_do_dodania):
        self.dodaj_id(osoba_do_dodania)
        self.pokaz_liste_osob().append(osoba_do_dodania)

    # Szukanie osoby po podanym ID

    def znajdz_osobe_po_id(self, id):
        for osoba in self.pokaz_liste_osob():
            if osoba.id_osoby() == id:
                return osoba
    # Szukanie osoby po podanym imieniu

    def znajdz_osoby_po_imieniu(self, osoba_szukana):
        lista_id_szukanych_osob = []
        for osoba in self.pokaz_liste_osob():
            if osoba.imie_osoby() == osoba_szukana:
                lista_id_szukanych_osob.append(osoba.id_osoby())
        return lista_id_szukanych_osob
