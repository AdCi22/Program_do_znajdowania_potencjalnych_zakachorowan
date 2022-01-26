from klasa_spotkanie import Spotkanie
from klasa_wszystkie_spotkania import Wszystkie_spotkania
from klasa_choroba import Choroba
from klasa_wszystkie_choroby import Wszystkie_choroby
from klasa_populacja import Populacja
from klasa_czlowiek import Czlowiek

from datetime import date

# Funkcja pytająca o kontynuacje
# Używana np. gdy chcemy dodać kilka osób do systemu ale nie mamy określonej ich ilosci


def wybor_o_kontynuacji(zapytanie):
    while True:
        print(zapytanie)
        odpowiedz = input('[T/N] ')
        if odpowiedz == 'T' or odpowiedz == 't':
            return True
        elif odpowiedz == 'N' or odpowiedz == 'n':
            return False
        else:
            print('Wprowadzono nieprawidłową wartość spróbuj jeszcze raz T - Tak, N - Nie')

# Funkcja wprowadzania daty, zwraca zformatowaną date


def wpisz_date(zapytanie):
    rok = input(f'Rok {zapytanie} ')
    miesiac = input(f'Miesiac {zapytanie} ')
    dzien = input(f'Dzien {zapytanie} ')
    wprowadzona_data = date(int(rok), int(miesiac), int(dzien))
    return wprowadzona_data

# Interfejs tekstowy programu


def interfejs():
    print('\nWitaj w programie do znajowania chorych powiązań!')

    # Wczytywanie danych z plików i tworzenie głównych obiektów klas na których działa program

    osoby_w_systemie = Populacja()
    choroby_w_systemie = Wszystkie_choroby()
    lista_wszystkich_spotkan = Wszystkie_spotkania()
    
    sciezka = input("Podaj sciezke do glownego folderu programu: ")# ścieżka do głównego folderu z programem

    lokalizacja_pilku_z_osobami_w_systemie = f'{sciezka}osoby_w_systemie.json'
    osoby_w_systemie.wczytaj_z_json(lokalizacja_pilku_z_osobami_w_systemie)

    lokalizacja_pilku_z_chorobami_w_systemie = f'{sciezka}choroby_w_systemie.json'
    choroby_w_systemie.wczytaj_z_json(lokalizacja_pilku_z_chorobami_w_systemie)

    lokalizacja_pilku_z_wszystkimi_spotkaniami = f'{sciezka}wszystkie_spotkania.json'
    lista_wszystkich_spotkan.wczytaj_z_json(choroby_w_systemie, lokalizacja_pilku_z_wszystkimi_spotkaniami)

    while True:  # Główna pętla funkcji interfejs()
        decyzja = 0

        decyzja = input("""
            Co chcesz zrobić?

            1. Pokaż osoby w systemie
            2. Dodaj osoby do sysytemu
            3. Sprawdz id osoby
            4. Dodaj spotkanie osob
            5. Dodaj zachorowanie osoby
            6. Dodj nowa chorobe zakazna
            7. Pokaz wszystkie choroby
            8. Wskaz wszystkie  osoby zakazone
            9. Wskaz wszystkie osoby podejrzane o zakarzenie
            10. Pokaz wszystkie spotkania
            11. Wyjdz z sysemu

            Wpisz numer podanej decyzji: """)
        decyzja = int(decyzja)
        print('')

        if decyzja == 1:  # Pokaż osoby w systemie
            for osoba in osoby_w_systemie.pokaz_liste_osob():
                print(F'Imie osoby: {osoba.imie_osoby()} ID:{osoba.id_osoby()}')
            print('')

        elif decyzja == 2:  # Dodaj osoby do sysytemu
            while True:
                imie = input("Podaj imie: ")
                osoba = Czlowiek(imie)
                osoby_w_systemie.dodaj_osobe_do_listy(osoba)
                zapytanie = "Czy chesz dodac kolejna osobe?"
                if wybor_o_kontynuacji(zapytanie):
                    continue
                else:
                    break

        elif decyzja == 3:  # Sprawdz id osoby
            osoba_do_sprawdzenia = input('Podaj imie osoby: ')
            znalezione_osoby = osoby_w_systemie.znajdz_osoby_po_imieniu(osoba_do_sprawdzenia)
            print('ID osob o podanym imieniu: ')
            for id_osoby_o_szukanym_imieniu in znalezione_osoby:
                print(id_osoby_o_szukanym_imieniu)
            if znalezione_osoby == []:
                print('Nie ma takiej osoby')

        elif decyzja == 4:  # Dodaj spotkanie osob
            ile_osob = int(input('Ile bylo osob na spotkaniu? (minimum 2) '))
            id_osob_na_spotkaniu = []
            if ile_osob < 2:
                ile_osob = 2
            for kolejna_osoba in range(ile_osob):
                osoba_na_spotkaniu = int(input(f'Podaj ID osoby nr.{kolejna_osoba+1}: '))
                id_osob_na_spotkaniu.append(osoba_na_spotkaniu)
            poczatek_spotkania = wpisz_date('poczatku spotkania')
            print('')
            koniec_spotkania = wpisz_date('konca spotkania')
            if poczatek_spotkania <= koniec_spotkania:
                spotkanie = Spotkanie(id_osob_na_spotkaniu, poczatek_spotkania, koniec_spotkania, 'nie', 'zdrowy')
                lista_wszystkich_spotkan.dodaj_spotkanie(spotkanie)
            else:
                print('Blendna data: data poczatkowa wieksza niż data koncowa')

        elif decyzja == 5:  # Dodaj zachorowanie osoby
            while True:
                id_chora_osoba = input('Poddaj id osoby zakazonej: ')

                if osoby_w_systemie.sprawdz_poprawnosc_id(id_chora_osoba):
                    if wybor_o_kontynuacji('ID po za zakresem czy chcsz wprowadzićdane od nowa? '):
                        continue
                    else:
                        break

                print('Kiedy doszlo do zakazenia?')
                data_zakazenia = wpisz_date('zakazenia:')

                while True:

                    nazwa_choroby = input('Nazwa choroby: ')

                    choroba_zakazna = choroby_w_systemie.znajdz_chorobe(nazwa_choroby)

                    if choroba_zakazna:
                        chora_osoba = osoby_w_systemie.znajdz_osobe_po_id(int(id_chora_osoba))
                        chora_osoba.zarazony_choroba(choroba_zakazna)
                        chora_osoba.zostal_zarazony(data_zakazenia, lista_wszystkich_spotkan, osoby_w_systemie)
                        break
                    else:
                        print('Nie ma takiej choroby w systemie')
                        if wybor_o_kontynuacji('Checzesz sprubowac wpisac chorobe jeszcze raz?'):
                            continue
                        else:
                            break

                zapytanie = "Czy chesz dodac kolejne zachorowanie?"
                if wybor_o_kontynuacji(zapytanie):
                    continue
                else:
                    break

        elif decyzja == 6:  # Dodj nowa chorobe zakazna
            nazwa_nowej_choroby = input("Podaj nazwe nowej choroby: ")
            czas_zarazliwosci_choroby = input('Podaj czas zarazliwosci choroby: ')
            ilosc_zarazen = input('Podaj stopien zarazliwosci choroby: ')
            nowa_choroba = Choroba(nazwa_nowej_choroby, int(czas_zarazliwosci_choroby), int(ilosc_zarazen))
            choroby_w_systemie.dodaj_chorobe(nowa_choroba)
            print('Choroba zostala dodana do systemu \n')

        elif decyzja == 7:  # Pokaz wszystkie choroby
            for choroba in choroby_w_systemie.obecna_lista_chorob():
                nazwa = choroba.nazwa_choroby()
                czas_zarazliwosc = choroba.czas_zarazliwosci_jako_int()
                zarazliwosc = choroba.stopien_zarazliwosci()
                print(f'''Nazwa choroby: {nazwa}
                Czas zarazliwosci choroby w dniach: {czas_zarazliwosc}
                Stopien zarazliwosci: {zarazliwosc}\n''')

        elif decyzja == 8:  # Wskaz wszystkie  osoby zakazone
            choroba = input('Nazwa choroby: ')
            for zakazenie in lista_wszystkich_spotkan.spotkania_z_choroba_i_stanem_zdrowia(choroba, "zarazony"):
                id_osob, poczatek, koniec = zakazenie.data_i_osoby()
                print(f'ID osoby: {id_osob} Czas trwania choroby: {poczatek} {koniec}')
            if lista_wszystkich_spotkan.spotkania_z_choroba_i_stanem_zdrowia(choroba, "zarazony") == []:
                print('Nie ma zarazen ta choraba')

        elif decyzja == 9:  # Wskaz wszystkie osoby podejrzane o zakarzenie
            choroba = input('Nazwa choroby: ')
            for podejrzenie in lista_wszystkich_spotkan.spotkania_z_choroba_i_stanem_zdrowia(choroba, "podejrzany"):
                id_osob, poczatek, koniec = podejrzenie.data_i_osoby()
                print(f'ID osoby: {id_osob} Czas trwania potencjalnej choroby: {poczatek} {koniec}')
            if lista_wszystkich_spotkan.spotkania_z_choroba_i_stanem_zdrowia(choroba, "zarazony") == []:
                print('Nie ma potencjalnych zarazen ta choraba')

        elif decyzja == 10:  # Pokaz wszystkie spotkania
            for spotkanie in lista_wszystkich_spotkan.spotkania_z_choroba_i_stanem_zdrowia('nie', 'zdrowy'):
                id_osob, poczatek, koniec = spotkanie.data_i_osoby()
                print(f'ID osób: {id_osob} Czas trwania spotkania: {poczatek} {koniec}')

        elif decyzja == 11:  # Wyjdz z sysemu
            print('Dziekujemy za uzywanie naszego systemu!')

            # zapisanie wprowadzonych danych
            osoby_w_systemie.zapisz_do_json(lokalizacja_pilku_z_osobami_w_systemie)
            choroby_w_systemie.zapisz_do_json(lokalizacja_pilku_z_chorobami_w_systemie)
            lista_wszystkich_spotkan.zapisz_do_json(lokalizacja_pilku_z_wszystkimi_spotkaniami)

            break
        else:  # Po wprowadzeniu nie prawidłowego numeru decyzji program wraca na początek pętli
            print('Podałeś nieprawiddłowe dane')


if __name__ == '__main__':
    interfejs()
