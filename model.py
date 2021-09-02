import json

class Uporabnik:
    def __init__(self, uporabnisko_ime, geslo, seznam_matrik):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo = geslo
        self.seznam_matrik = seznam_matrik

    def preveri_geslo(self, geslo):
        if self.geslo != geslo:
            raise ValueError('Napačno geslo!')

    @staticmethod
    def preveri_enakost_gesel(geslo1, geslo2):
        if geslo1 != geslo2:
            raise ValueError('Gesli se ne ujemata!')

    def shrani_matriko(self, ime_datoteke):
        slovar_podatkov = {
            'uporabnisko_ime': self.uporabnisko_ime,
            'geslo': self.geslo,
            'seznam_matrik': self.seznam_matrik,
        }
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(slovar_podatkov, datoteka, ensure_ascii=False, indent=4)

    @classmethod  
    def nalozi_matriko(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_podatkov = json.load(datoteka)
        uporabnisko_ime = slovar_podatkov['uporabnisko_ime']
        geslo = slovar_podatkov['geslo']
        seznam_matrik = slovar_podatkov['seznam_matrik']
        return cls(uporabnisko_ime, geslo, seznam_matrik)

class Matrika:
    def __init__(self, matrika):
        self.matrika = matrika
        self.visina = len(self.matrika)
        self.sirina = len(self.matrika[0])

    def __str__(self):
        return "\n".join(
            ", ".join([str(i) for i in line]) 
            for line in self.matrika
        )

    def dodaj_stevilo(self, stevilo, vrstica, stolpec):
        '''Doda število v matriko (ali že obstoječe število spremeni v drugo).'''
        if str(stevilo) not in '123456789' or str(vrstica) not in '123456789' or str(stolpec) not in '123456789':
            raise ValueError('Prosimo, da za vrstice, stolpce in števila izbirate števila od 1 do 9.')
        else: 
            stevilo = int(stevilo)
            vrstica = int(vrstica)
            stolpec = int(stolpec)
        if len(str(stevilo)) != 1:
            raise ValueError(f'{stevilo} ni primeren znak. Prosim izberite število od 1 do 9.')
        elif int(vrstica) > 9 or int(vrstica) < 1:
            raise ValueError('Ta vrstica ne obstaja.')
        elif int(stolpec) > 9 or int(stolpec) < 1:
            raise ValueError('Ta stolpec ne obstaja.')
        else:
            self.matrika[vrstica - 1][stolpec - 1] = stevilo

    def odstrani_stevilo(self, vrstica, stolpec):
        '''Odstrani število v matriki in ga nadomesti z vrednostjo 0.'''
        if str(vrstica) not in '123456789' or str(stolpec) not in '123456789':
            raise ValueError('Prosimo, da za vrstice, stolpce in števila izbirate števila od 1 do 9.')
        else:
            vrstica = int(vrstica)
            stolpec = int(stolpec)
        if self.matrika[vrstica - 1][stolpec - 1] == 0:
            pass
        elif vrstica > 9 or vrstica < 1:
            raise ValueError('Ta vrstica ne obstaja.')
        elif stolpec > 9 or stolpec < 1:
            raise ValueError('Ta stolpec ne obstaja.')
        else:
            self.matrika[vrstica - 1][stolpec - 1] = 0

    def izbrisi_cel_sudoku(self):
        self.matrika = [9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0], 9 * [0]]
        return Matrika(self.matrika)

    def najdi_naslednjo_prazno_celico(self, vrstica, stolpec):
        for i in range(vrstica, 9):
            for j in range(stolpec, 9):
                if self.matrika[i][j] == 0:
                    return i, j
        for i in range(0,9):
            for j in range(0,9):
                if self.matrika[i][j] == 0:
                    return i, j
        return -1, -1

    def preveri_ustreznost(self, vrstica, stolpec, stevilo):
        vrsticaok = all([stevilo != self.matrika[vrstica][j] for j in range(9)])
        if vrsticaok:
            stolpecok = all([stevilo != self.matrika[i][stolpec] for i in range(9)])
            if stolpecok:
                vrst, stol = 3 * ((vrstica) // 3), 3 * ((stolpec) // 3)
                for i in range(vrst, vrst + 3):
                    for j in range(stol, stol + 3):
                        if self.matrika[i][j] == stevilo:
                            return False
                return True
        return False

    def resevanje(self, vrstica=0, stolpec=0):
        vrstica, stolpec = self.najdi_naslednjo_prazno_celico(vrstica, stolpec)
        if vrstica == -1:
            return True
        for stevilo in range(1,10):
            if self.preveri_ustreznost(vrstica, stolpec, stevilo):
                self.matrika[vrstica][stolpec] = stevilo
                if self.resevanje(vrstica, stolpec):
                    return True
                self.matrika[vrstica][stolpec] = 0
        return False

    def resi(self):
        if self.resevanje() == False:
            raise ValueError('Sudokuja ni mogoče rešiti. Preverite ali ste pravilno vnesli vsa števila.')
        else:
            return Matrika(self.matrika)