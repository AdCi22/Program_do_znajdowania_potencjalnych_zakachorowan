from klasa_populacja import Populacja
from klasa_czlowiek import Czlowiek
from io import StringIO

def test_ustawienie_id():
    czlowiek = Czlowiek('Joachim')
    populacja = Populacja([czlowiek])
    assert czlowiek.id_osoby() == 0

def test_ustawienie_id_kilku_id():
    czlowiek = Czlowiek('Joachim')
    czlowiek_1 = Czlowiek('Gombrowicz')
    czlowiek_2 = Czlowiek('Adam')
    populacja = Populacja([czlowiek, czlowiek_1, czlowiek_2])
    assert czlowiek.id_osoby() == 0  
    assert czlowiek_1.id_osoby() == 1      
    assert czlowiek_2.id_osoby() == 2 
    
def test_ustawienie_najwyzszego_id():
    populacja = Populacja()
    populacja._ustaw_najwyzsze_id(2)
    assert populacja._obecnie_najwyzsze_id == 2

def test_poprawnosc_id():
    populacja = Populacja()
    populacja._ustaw_najwyzsze_id(2)
    assert populacja.sprawdz_poprawnosc_id(2) 
    assert populacja.sprawdz_poprawnosc_id(3) == False 

def test_zwracanie_listy_osob():
    czlowiek = Czlowiek('Joachim')
    czlowiek_1 = Czlowiek('Gombrowicz')
    czlowiek_2 = Czlowiek('Adam')
    populacja = Populacja([czlowiek, czlowiek_1, czlowiek_2])
    assert populacja.pokaz_liste_osob() == [czlowiek, czlowiek_1, czlowiek_2]

def test_znajowanie_osoby_po_id():
    czlowiek = Czlowiek('Joachim')
    czlowiek_1 = Czlowiek('Gombrowicz')
    czlowiek_2 = Czlowiek('Adam')
    populacja = Populacja([czlowiek, czlowiek_1, czlowiek_2])
    assert populacja.znajdz_osobe_po_id(1) == czlowiek_1

def test_znajowanie_osob_po_imieniu():
    czlowiek = Czlowiek('Joachim')
    czlowiek_1 = Czlowiek('Gombrowicz')
    czlowiek_2 = Czlowiek('Adam')
    czlowiek_3 = Czlowiek('Adam')   
    populacja = Populacja([czlowiek, czlowiek_1, czlowiek_2, czlowiek_3])
    assert populacja.znajdz_osoby_po_imieniu("Gombrowicz") == [1]
    assert populacja.znajdz_osoby_po_imieniu("Adam") == [2, 3]

def test_wczytywanie_z_pliku():
    sciezka = StringIO("""[
        {
            "imie": "Kszysztof"
            "id": 0
        },
        {
            "imie": "Piotr"
            "id": 1
        }
    ]""")
    populacja = Populacja()
    populacja.wczytaj_z_json(sciezka)
    czlowiek_1, czlowiek_2 = populacja.pokaz_liste_osob()
    assert czlowiek_1.imie_osoby() == 'Kszysztof'
    assert czlowiek_1.id_osoby() == 0
    assert czlowiek_1.imie_osoby() == 'Piotr'
    assert czlowiek_1.id_osoby() == 1
