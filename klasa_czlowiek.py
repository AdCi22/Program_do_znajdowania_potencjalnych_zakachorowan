from klasa_spotkanie import Spotkanie

"""
Klasa określająca podstawowe parametry człowieka czyli:
-Imie
-ID

Określa też parametry ważne dla funkcjonowania programu czyli:
- stan zdrowia (zarażony, podejrzany, zdrowy)
- choroba którą ktoś się zaraził
- obecny stopień zaraźliwośc choroby

Najważniejsze metody:
-stwierdzenie zakażenia
-stwierdzenie prawdopodobieństwa choroby
"""


class Czlowiek:
    def __init__(self, imie, id=None, zarazony=None, podejrzany=None, choroba=None, stopien_zarazliwosci=None):
        self._zarazony = zarazony if zarazony else False
        self._podejrzany = podejrzany if podejrzany else False
        self._choroba = choroba if choroba else None
        self._id = id if id else None
        self._imie = imie
        self._stopien_zarazliwosci = stopien_zarazliwosci

    # Zwraca informacje czy człowiek jest zarażony

    def zarazenie(self):
        return self._zarazony

    # Zwraca informacje czy człowiek jesz podejrzanym zarażonym

    def czy_podejrzany(self):
        return self._podejrzany()

    # Zwraca informacje o chorobie człowieka

    def obecna_choroba(self):
        return self._choroba

    # Zwraca ID człowieka

    def id_osoby(self):
        return self._id

    # Zwraca imie człowieka

    def imie_osoby(self):
        return self._imie

    # Zwraca obecny stopień zaraźliwości choroby króra ma dany człowiek

    def obecna_zarazliowsc(self, stopien_zakazania):
        self._stopien_zarazliwosci = stopien_zakazania

    def stan_zdrowia(self):
        if self.zarazenie():
            return "zarazony"
        elif self.czy_podejrzany():
            return "podejrzany"
        else:
            return "zdrowy"

    # Przeprowadzenie prodecury zarażenia, wytypowanie potencjalnych zakażonych

    def zostal_zarazony(self, data_zakazenia, wszystkie_spotkania, populacja):
        self._zarazony = True
        choroba = self.obecna_choroba()
        koniec_czasu_zarazliwosci = choroba.czas_zarazliwosci() + data_zakazenia

        zbior_podejrzanych_chorych = set()  # zbiór osob po id
        lista_podejrzanych_z_datami = []
        id = self.id_osoby()
        lista_spotkan_osoby = wszystkie_spotkania.znajdz_spotkania_osoby_w_zakresie(id, data_zakazenia, koniec_czasu_zarazliwosci)

        zakazenie = Spotkanie(self.imie_osoby(), data_zakazenia, koniec_czasu_zarazliwosci, choroba.nazwa_choroby(), "zarazony")

        wszystkie_spotkania.dodaj_spotkanie(zakazenie)
        
        for spotkanie in lista_spotkan_osoby:
            poczatek_spotkania = spotkanie.poczatek_spotkania()

            for osoba_id in spotkanie.osoby_na_spotkaniu():

                if osoba_id not in zbior_podejrzanych_chorych:
                    zbior_podejrzanych_chorych.add(osoba_id)
                    poczatek_podejrzewania = [poczatek_spotkania, osoba_id]
                    lista_podejrzanych_z_datami.append(poczatek_podejrzewania)

        zarazliwosc = int(choroba.stopien_zarazliwosci())
        self.obecna_zarazliowsc(zarazliwosc)
        if zarazliwosc > 0:
            for potencjalny_poczatek_zachorowania in lista_podejrzanych_z_datami:
                osoba = populacja.znajdz_osobe_po_id(int(potencjalny_poczatek_zachorowania[1]))
                osoba.zostal_podejrzany(zarazliwosc-1, potencjalny_poczatek_zachorowania[0], koniec_czasu_zarazliwosci, wszystkie_spotkania, choroba, populacja)

    # Wytypowanie potencjalnych zakażonych

    def zostal_podejrzany(self, obecna_zarazliwosc, poczatek_zachorowania, koniec_zachorowania, wszystkie_spotkania, choroba, populacja):
        self._podejrzany = True
        self.zarazony_choroba(choroba)

        zbior_podejrzanych_chorych = set()  # zbiór osob po id
        lista_podejrzanych_z_datami = []

        koniec_czasu_zarazliwosci = choroba.czas_zarazliwosci() + poczatek_zachorowania
        podejrzenie = Spotkanie(self.imie_osoby(), poczatek_zachorowania, koniec_czasu_zarazliwosci, choroba.nazwa_choroby(), 'podejrzany')
       
        wszystkie_spotkania.dodaj_spotkanie(podejrzenie)
        lista_spotkan_osoby = wszystkie_spotkania.znajdz_spotkania_osoby_w_zakresie(self.id_osoby(), poczatek_zachorowania, koniec_zachorowania)

        for spotkanie in lista_spotkan_osoby:
            poczatek_spotkania = spotkanie.poczatek_spotkania()

            for osoba_id in spotkanie.osoby_na_spotkaniu():

                if osoba_id not in zbior_podejrzanych_chorych:
                    zbior_podejrzanych_chorych.add(osoba_id)
                    poczatek_podejrzewania = [poczatek_spotkania, osoba_id]
                    lista_podejrzanych_z_datami.append(poczatek_podejrzewania)

        zarazliwosc = obecna_zarazliwosc

        self.obecna_zarazliowsc(zarazliwosc)
        if zarazliwosc > 0:
            for potencjalny_poczatek_zachorowania in lista_podejrzanych_z_datami:
                osoba = populacja.znajdz_osobe_po_id(potencjalny_poczatek_zachorowania[1])
                osoba.zostal_podejrzany(zarazliwosc-1, potencjalny_poczatek_zachorowania[0], koniec_zachorowania, wszystkie_spotkania, choroba, populacja)

    # Ustawienie obecnej choroby człowieka

    def zarazony_choroba(self, nowa_choroba):
        self._choroba = nowa_choroba

    # Ustawienie ID osoby

    def ustaw_id(self, nowe_id):
        self._id = nowe_id
