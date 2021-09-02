import bottle
import hashlib
import os
from model import Uporabnik, Matrika

SKRIVNOST_ZA_PISKOTKE = 'STROGO ZAUPNA SKRIVNOST'
uporabniki ={}

for ime_datoteke in os.listdir('uporabniki'):
    uporabnik = Uporabnik.nalozi_matriko(os.path.join('uporabniki', ime_datoteke))
    uporabniki[uporabnik.uporabnisko_ime] = uporabnik
    
def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=SKRIVNOST_ZA_PISKOTKE)
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    return uporabniki[uporabnisko_ime]

def shrani_trenutnega_uporabnika():
    uporabnik = trenutni_uporabnik()
    uporabnik.shrani_matriko(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))

def zasifriraj_geslo(geslo):
    h = hashlib.blake2b()
    h.update(geslo.encode(encoding='utf-8'))
    zasifrirano_geslo = h.hexdigest()
    return zasifrirano_geslo

def odpri_stran(stran):
    ime = trenutni_uporabnik().uporabnisko_ime
    seznam_matrik = trenutni_uporabnik().seznam_matrik
    return bottle.template(
        stran,
        seznam_matrik = seznam_matrik, 
        ime = ime)

@bottle.get("/")
def zacetna_stran():
    bottle.redirect("/matrika/")

@bottle.get('/prijava/')
def prijava_get():
    return bottle.template('prijava.html')

@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    zasifrirano_geslo = zasifriraj_geslo(geslo)
    if uporabnisko_ime not in uporabniki:
        raise ValueError('''Uporabniško ime ne obstaja! 
    Vpišite veljavno uporabniško ime ali se registrirajte.''')
    else:
        uporabnik = uporabniki[uporabnisko_ime] 
        uporabnik.preveri_geslo(zasifrirano_geslo)
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=SKRIVNOST_ZA_PISKOTKE)
    bottle.redirect('/')

@bottle.post('/registracija/')
def registracija():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    potrditev = bottle.request.forms.getunicode('potrdi')
    Uporabnik.preveri_enakost_gesel(geslo, potrditev)
    zasifrirano_geslo = zasifriraj_geslo(geslo)
    if uporabnisko_ime in uporabniki:
        raise ValueError('Uporabniško ime je že zasedeno!')
    else:
        uporabnik = Uporabnik(
            uporabnisko_ime,
            zasifrirano_geslo,
            []
        )
        uporabniki[uporabnisko_ime] = uporabnik
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=SKRIVNOST_ZA_PISKOTKE)
    uporabnik.shrani_matriko(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))
    bottle.redirect('/')

@bottle.post('/odjava/')
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime', path='/')
    bottle.redirect('/')

@bottle.get("/navodila/")
def prikaz_navodil():
    return odpri_stran("navodila.html")
    
@bottle.get("/matrika/")
def prikaz_matrike():
    return odpri_stran('matrika.html')

@bottle.post("/resen_sudoku/")
def resevanje_sudokuja():
    ime = trenutni_uporabnik().uporabnisko_ime
    seznam_matrik = trenutni_uporabnik().seznam_matrik
    matrika = [
        [int(bottle.request.forms['m11']), int(bottle.request.forms['m12']), int(bottle.request.forms['m13']), int(bottle.request.forms['m14']), int(bottle.request.forms['m15']), int(bottle.request.forms['m16']), int(bottle.request.forms['m17']), int(bottle.request.forms['m18']), int(bottle.request.forms['m19'])],
        [int(bottle.request.forms['m21']), int(bottle.request.forms['m22']), int(bottle.request.forms['m23']), int(bottle.request.forms['m24']), int(bottle.request.forms['m25']), int(bottle.request.forms['m26']), int(bottle.request.forms['m27']), int(bottle.request.forms['m28']), int(bottle.request.forms['m29'])],
        [int(bottle.request.forms['m31']), int(bottle.request.forms['m32']), int(bottle.request.forms['m33']), int(bottle.request.forms['m34']), int(bottle.request.forms['m35']), int(bottle.request.forms['m36']), int(bottle.request.forms['m37']), int(bottle.request.forms['m38']), int(bottle.request.forms['m39'])],
        [int(bottle.request.forms['m41']), int(bottle.request.forms['m42']), int(bottle.request.forms['m43']), int(bottle.request.forms['m44']), int(bottle.request.forms['m45']), int(bottle.request.forms['m46']), int(bottle.request.forms['m47']), int(bottle.request.forms['m48']), int(bottle.request.forms['m49'])],
        [int(bottle.request.forms['m51']), int(bottle.request.forms['m52']), int(bottle.request.forms['m53']), int(bottle.request.forms['m54']), int(bottle.request.forms['m55']), int(bottle.request.forms['m56']), int(bottle.request.forms['m57']), int(bottle.request.forms['m58']), int(bottle.request.forms['m59'])],
        [int(bottle.request.forms['m61']), int(bottle.request.forms['m62']), int(bottle.request.forms['m63']), int(bottle.request.forms['m64']), int(bottle.request.forms['m65']), int(bottle.request.forms['m66']), int(bottle.request.forms['m67']), int(bottle.request.forms['m68']), int(bottle.request.forms['m69'])],
        [int(bottle.request.forms['m71']), int(bottle.request.forms['m72']), int(bottle.request.forms['m73']), int(bottle.request.forms['m74']), int(bottle.request.forms['m75']), int(bottle.request.forms['m76']), int(bottle.request.forms['m77']), int(bottle.request.forms['m78']), int(bottle.request.forms['m79'])],
        [int(bottle.request.forms['m81']), int(bottle.request.forms['m82']), int(bottle.request.forms['m83']), int(bottle.request.forms['m84']), int(bottle.request.forms['m85']), int(bottle.request.forms['m86']), int(bottle.request.forms['m87']), int(bottle.request.forms['m88']), int(bottle.request.forms['m89'])],
        [int(bottle.request.forms['m91']), int(bottle.request.forms['m92']), int(bottle.request.forms['m93']), int(bottle.request.forms['m94']), int(bottle.request.forms['m95']), int(bottle.request.forms['m96']), int(bottle.request.forms['m97']), int(bottle.request.forms['m98']), int(bottle.request.forms['m99'])]]
    matrika = Matrika(matrika)
    resen_sudoku = matrika.resi()
    resen_sudoku_po_vrsticah = str(resen_sudoku).split('\n')
    mat = []
    for j in range(9):
        for i in range(9):
            mat += resen_sudoku_po_vrsticah[j][3 * i]
    seznam_matrik.append(mat)
    shrani_trenutnega_uporabnika()
    return bottle.template('resen_sudoku.html', celamatrika = mat, ime = ime, seznam_matrik = seznam_matrik)

@bottle.post("/matrika/")
def brisanje_sudokuja():
    trenutni_uporabnik().matrika = izbrisi_cel_sudoku()
    bottle.redirect("/matrika/")

@bottle.get("/moji_sudokuji/")
def moji_sudokuji():
    return odpri_stran('moji_sudokuji.html')

from bottle import error
@error(404)
def error404(error):
    return 'Ta stran ne obstaja'
    
bottle.run(debug=True, reloader=True)