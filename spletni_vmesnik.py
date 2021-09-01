import bottle
import hashlib
import os
from model import Uporabnik, Matrika


@bottle.get("/")
def zacetna_stran():
    bottle.redirect("/matrika/")
    
@bottle.get("/matrika/")
def prikaz_matrike():
    return bottle.template('matrika.html')
    
@bottle.get("/resen_sudoku/")
def prikaz_resenega():
    return bottle.template('resen_sudoku.html')

@bottle.post("/resen_sudoku/")
def resevanje_sudokuja():
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
    #self.matrika = matrika
    #resen_sudoku = matrika.resi()
    return bottle.template('resen_sudoku.html', celamatrika=matrika)


@bottle.post("/matrika/")
def brisanje_sudokuja():
    trenutni_uporabnik().matrika = izbrisi_cel_sudoku()
    bottle.redirect("/matrika/")

from bottle import error
@error(404)
def error404(error):
    return 'Ta stran ne obstaja'
    
bottle.run(debug=True, reloader=True)