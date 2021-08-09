class Matrika:
    def __init__(self, matrika):
        self.matrika = [line[:] for line in matrika] 
        self.visina = len(self.matrika)
        self.sirina = len(self.matrika[0])

    def __eq__(self, other):
        '''Preveri ali sta matriki enaki.'''
        return isinstance(other, Matrika) and self.matrika == other.matrika

    def __str__(self):
        return "\n".join(
            ", ".join([str(i) for i in line]) 
            for line in self.matrika
        )
   
    def dodaj_stevilo(self, stevilo, vrstica, stolpec):
        '''Doda število v matriko (ali že obstoječe število spremeni v drugo).'''
        if str(stevilo) not in '123456789' or len(str(stevilo)) != 0:
            raise ValueError(f'{stevilo} ni primeren znak. Prosim izberite število od 1 do 9.')
        elif vrstica > 8 or vrstica < 0:
            raise ValueError('Ta vrstica ne obstaja.')
        elif stolpec > 8 or stolpec < 0:
            raise ValueError('Ta stolpec ne obstaja.')
        else:
            self.matrika[vrstica][stolpec] = int(stevilo)

    def odstrani_stevilo(self, vrstica, stolpec):
        '''Odstrani število v matriki in ga nadomesti z vrednostjo None.'''
        if self.matrika[vrstica][stolpec] == None:
            pass
        elif vrstica > 8 or vrstica < 0:
            raise ValueError('Ta vrstica ne obstaja.')
        elif stolpec > 8 or stolpec < 0:
            raise ValueError('Ta stolpec ne obstaja.')
        else:
            self.matrika[vrstica][stolpec] = None
    
    def preveri_ustreznost_vrstic(self):
        '''Preveri če v nobeni vrstici katero od števil ni zapisano več kot enkrat.'''
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if self.matrika[i][j] == self.matrika[i][k]:
                        return 'Prosim, da ustrezno vnesete števila. V isti vrstici ne sme biti večkrat napisano enako število.'
        return True

    def preveri_ustreznost_stolpcev(self):
        '''Preveri če v nobenem stolpcu katero od števil ni zapisano več kot enkrat.'''
        for j in range(9):
            for i in range(9):
                for k in range(9):
                    if self.matrika[i][j] == self.matrika[k][j]:
                        return 'Prosim, da ustrezno vnesete števila. V istem stolpcu ne sme biti večkrat napisano enako število.'
        return True

    def preveri_ustreznost_kvadratov(self):
        '''Preveri če v nobenem kvadratu 3x3 katero od števil ni zapisano več kot enkrat.'''
        for i in range(3):
            for k in range(3):
                for j in range(3):
                    for l in range(3):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'    
                for j in range(3,6):
                    for l in range(3,6):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
                for j in range(6,9):
                    for l in range(6,9):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
        for i in range(3,6):
            for k in range(3,6):
                for j in range(3):
                    for l in range(3):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'    
                for j in range(3,6):
                    for l in range(3,6):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
                for j in range(6,9):
                    for l in range(6,9):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
        for i in range(6,9):
            for k in range(6,9):
                for j in range(3):
                    for l in range(3):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'    
                for j in range(3,6):
                    for l in range(3,6):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
                for j in range(6,9):
                    for l in range(6,9):
                        if self.matrika[i][j] == self.matrika[k][l]:
                            return 'Prosim, da ustrezno vnesete števila.'
        return True

    def preveri_ustreznost(self):
        '''Preveri ustreznost kvadratov, vrstic in stolpcev naenkrat.'''
        return preveri_ustreznost_kvadratov(self) == True and preveri_ustreznost_stolpcev(self) == True and preveri_ustreznost_vrstic(self) == True 

    def preveri_ali_je_dovolj_stevil(self):
        '''Preveri ali je v začetku vnesenih dovolj števil.'''
        vsota = 0
        for i in self.matrika:
            for j in i:
                if i != None:
                    vsota += 1
        if vsota > 16:
            return True

    def preveri_ali_je_dovolj_razlicnih_stevil(self):
        '''Preveri ali je v začetku vnesenih dovolj različnih števil.'''
        seznam = []
        for i in self.matrika:
            if i != None and i not in seznam:
                seznam += [i]
        if len(seznam) >= 8:
            return True

    def iskanje_matrike_vseh_moznosti(self):
        '''Za vsako prazno polje v sudokuju najde vse možne rešitve.'''
        matrika_vseh_moznosti = self.matrika
        for i in range(9):
            for j in range(9):
                if self.matrika[i][j] == None:
                    for k in range(1,10):
                        self.matrika[i][j] = k
                        if preveri_ustreznost(self):
                            matrika_vseh_moznosti[i][j] += [k]
        return matrika_vseh_moznosti


    def resevanje(self):
        pass

    def resi(self):
        if preveri_ali_je_dovolj_stevil(self) != True:
            raise ValueError('Prosim vnesite vsaj 16 števil.')
        elif preveri_ali_je_dovolj_razlicnih_stevil(self) != True:
            raise ValueError('Prosim vnesite dovolj različnih števil od 1 do 9.')
        elif preveri_ustreznost(self) != True:
            pass
        else:
            resevanje(self)
    
