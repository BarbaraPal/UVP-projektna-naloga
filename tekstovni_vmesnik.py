from model import Matrika

IME_DATOTEKE = "stanje.json"
try:
    matrika = Matrika.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    matrika = Matrika([9 * [None], 9 * [None], 9 * [None], 9 * [None], 9 * [None], 9 * [None], 9 * [None], 9 * [None], 9 * [None]])

RESI = 1
NAMIG = 2
DODAJ_STEVILO = 3
ODSTRANI_STEVILO = 4
IZBRISI = 5
IZHOD = 6

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")

def preberi_ukaz(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

def prikazi_pozdravno_sporocilo():
    print('Pozdravljeni')
    print('Za izhod pritisnite Ctrl-C.')

def prikaz_matrike(matrika):
    print(matrika.__str__())
    return matrika.__str__()

def osnovni_zaslon():
    prikaz_matrike(matrika)
    while True:
        ukaz = preberi_ukaz([
            (RESI, 'reši sudoku'),
            (NAMIG, 'namig'),
            (DODAJ_STEVILO, 'dodaj število'),
            (ODSTRANI_STEVILO, 'odstrani število'),
            (IZBRISI, 'izbriši ta sudoku'),
            (IZHOD, 'izhod')
        ])
        if ukaz == RESI:
            resi_sudoku()
        elif ukaz == NAMIG:
            daj_namig()
        elif ukaz == DODAJ_STEVILO:
            dodaj_stevilo()
        elif ukaz == ODSTRANI_STEVILO:
            odstrani_stevilo()
        elif ukaz == IZBRISI:
            izbrisi_cel_sudoku()
        elif ukaz == IZHOD:
            stanje.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break
        else:
            pass

def resi_sudoku():
    matrika.resi()
    print(matrika)

def dodaj_stevilo():
    print('V katero vrstico bi radi vnesli število?')
    vrstica = input("Vrstica> ")
    print('V kateri stolpec bi radi vnesli število?')
    stolpec = input("Stolpec> ")
    print("Prosim vnesite število.")
    stevilo = input("Število> ")
    matrika.dodaj_stevilo(stevilo,vrstica,stolpec)
    print(matrika)

def odstrani_stevilo():
    print("Iz katere vrstice bi radi odstranili število?")    
    vrstica = input("Vrstica> ")
    print('Iz katerega stolpca bi radi odstranili število?')
    stolpec = input("Stolpec> ")
    matrika.odstrani_stevilo(vrstica, stolpec)
    print(matrika)

def izbrisi_cel_sudoku():
    matrika.izbrisi_cel_sudoku()
    print(matrika)

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()
        
tekstovni_vmesnik()