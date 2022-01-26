import datetime

"""
Klasa określająca podstawowe parametry choroby czyli:
-nazwe choroby
-czas zaraźliwości
-zaraźliwość
"""

class Choroba:
    def __init__(self, nazwa, czas_zarazliwosci, zarazliwosc):
        self._nazwa_choroby = nazwa
        self._czas_zarazliwosci = czas_zarazliwosci  # w dniach
        self._zarazliwosc = zarazliwosc

    # Zwraca nazwe choroby

    def nazwa_choroby(self):
        return self._nazwa_choroby

    # Zwraca sformatowany czas zakazania

    def czas_zarazliwosci(self):
        return datetime.timedelta(self._czas_zarazliwosci)

    # Zwraca czas zarazliwosci w dniach jako liczba

    def czas_zarazliwosci_jako_int(self):
        return self._czas_zarazliwosci

    # Zwraca stopień zaraźliwości

    def stopien_zarazliwosci(self):
        return self._zarazliwosc
