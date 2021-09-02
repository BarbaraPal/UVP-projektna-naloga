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
    
    def kvadratek_ok(self):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
                for k in range(3, 6):
                    for l in range(3,6):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
                for k in range(6, 9):
                    for l in range(6, 9):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
        for i in range(3, 6):
            for j in range(3, 6):
                for k in range(3):
                    for l in range(3):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
                for k in range(3, 6):
                    for l in range(3, 6):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
                for k in range(6, 9):
                    for l in range(6, 9):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
        for i in range(6, 9):
            for j in range(6, 9):
                for k in range(3):
                    for l in range(3):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False 
                for k in range(3, 6):
                    for l in range(3, 6):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False 
                for k in range(6, 9):
                    for l in range(6, 9):
                        if self.matrika[i][k] == self.matrika[j][l] and self.matrika[j][l] != 0 and i != j and k != l:
                            return False
        return True 

    def vrstica_in_stolpec_ok(self):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    for l in range(9):
                        if self.matrika[i][k] == self.matrika[i][l] and self.matrika[i][l] != 0 and k != l:
                            return False
                        elif self.matrika[i][k] == self.matrika[j][k] and self.matrika[j][k] != 0 and i != j:
                            return False
        return True

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
        if self.kvadratek_ok() == False or self.vrstica_in_stolpec_ok() == False:
            raise ValueError('Sudokuja ni mogoče rešiti. Preverite ali ste pravilno vnesli vsa števila.')
        if self.resevanje() == False:
            raise ValueError('Sudokuja ni mogoče rešiti. Preverite ali ste pravilno vnesli vsa števila.')
        else:
            return Matrika(self.matrika)