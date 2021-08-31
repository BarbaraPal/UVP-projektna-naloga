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
        [bottle.request.forms['m11'], bottle.request.forms['m12'], bottle.request.forms['m13'], bottle.request.forms['m14'], bottle.request.forms['m15'], bottle.request.forms['m16'], bottle.request.forms['m17'], bottle.request.forms['m18'], bottle.request.forms['m19']],
        [bottle.request.forms['m21'], bottle.request.forms['m22'], bottle.request.forms['m23'], bottle.request.forms['m24'], bottle.request.forms['m25'], bottle.request.forms['m26'], bottle.request.forms['m27'], bottle.request.forms['m28'], bottle.request.forms['m29']],
        [bottle.request.forms['m31'], bottle.request.forms['m32'], bottle.request.forms['m33'], bottle.request.forms['m34'], bottle.request.forms['m35'], bottle.request.forms['m36'], bottle.request.forms['m37'], bottle.request.forms['m38'], bottle.request.forms['m39']],
        [bottle.request.forms['m41'], bottle.request.forms['m42'], bottle.request.forms['m43'], bottle.request.forms['m44'], bottle.request.forms['m45'], bottle.request.forms['m46'], bottle.request.forms['m47'], bottle.request.forms['m48'], bottle.request.forms['m49']],
        [bottle.request.forms['m51'], bottle.request.forms['m52'], bottle.request.forms['m53'], bottle.request.forms['m54'], bottle.request.forms['m55'], bottle.request.forms['m56'], bottle.request.forms['m57'], bottle.request.forms['m58'], bottle.request.forms['m59']],
        [bottle.request.forms['m61'], bottle.request.forms['m62'], bottle.request.forms['m63'], bottle.request.forms['m64'], bottle.request.forms['m65'], bottle.request.forms['m66'], bottle.request.forms['m67'], bottle.request.forms['m68'], bottle.request.forms['m69']],
        [bottle.request.forms['m71'], bottle.request.forms['m72'], bottle.request.forms['m73'], bottle.request.forms['m74'], bottle.request.forms['m75'], bottle.request.forms['m76'], bottle.request.forms['m77'], bottle.request.forms['m78'], bottle.request.forms['m79']],
        [bottle.request.forms['m81'], bottle.request.forms['m82'], bottle.request.forms['m83'], bottle.request.forms['m84'], bottle.request.forms['m85'], bottle.request.forms['m86'], bottle.request.forms['m87'], bottle.request.forms['m88'], bottle.request.forms['m89']],
        [bottle.request.forms['m91'], bottle.request.forms['m92'], bottle.request.forms['m93'], bottle.request.forms['m94'], bottle.request.forms['m95'], bottle.request.forms['m96'], bottle.request.forms['m97'], bottle.request.forms['m98'], bottle.request.forms['m99']]]
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