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

@bottle.post("/resen_sudoku/")
def resevanje_sudokuja():
    matrika = [
        [bottle.request.query.enaena, bottle.BaseRequest.query('12'), bottle.BaseRequest.query('13'), bottle.BaseRequest.query('14'), bottle.BaseRequest.query('15'), bottle.BaseRequest.query('16'), bottle.BaseRequest.query('17'), bottle.BaseRequest.query('18'), bottle.BaseRequest.query('19')],
        [bottle.BaseRequest.query('21'), bottle.BaseRequest.query('22'), bottle.BaseRequest.query('23'), bottle.BaseRequest.query('24'), bottle.BaseRequest.query('25'), bottle.BaseRequest.query('26'), bottle.BaseRequest.query('27'), bottle.BaseRequest.query('28'), bottle.BaseRequest.query('29')],
        [bottle.BaseRequest.query('31'), bottle.BaseRequest.query('32'), bottle.BaseRequest.query('33'), bottle.BaseRequest.query('34'), bottle.BaseRequest.query('35'), bottle.BaseRequest.query('36'), bottle.BaseRequest.query('37'), bottle.BaseRequest.query('38'), bottle.BaseRequest.query('39')],
        [bottle.BaseRequest.query('41'), bottle.BaseRequest.query('42'), bottle.BaseRequest.query('43'), bottle.BaseRequest.query('44'), bottle.BaseRequest.query('45'), bottle.BaseRequest.query('46'), bottle.BaseRequest.query('47'), bottle.BaseRequest.query('48'), bottle.BaseRequest.query('49')],
        [bottle.BaseRequest.query('51'), bottle.BaseRequest.query('52'), bottle.BaseRequest.query('53'), bottle.BaseRequest.query('54'), bottle.BaseRequest.query('55'), bottle.BaseRequest.query('56'), bottle.BaseRequest.query('57'), bottle.BaseRequest.query('58'), bottle.BaseRequest.query('59')],
        [bottle.BaseRequest.query('61'), bottle.BaseRequest.query('62'), bottle.BaseRequest.query('63'), bottle.BaseRequest.query('64'), bottle.BaseRequest.query('65'), bottle.BaseRequest.query('66'), bottle.BaseRequest.query('67'), bottle.BaseRequest.query('68'), bottle.BaseRequest.query('69')],
        [bottle.BaseRequest.query('71'), bottle.BaseRequest.query('72'), bottle.BaseRequest.query('73'), bottle.BaseRequest.query('74'), bottle.BaseRequest.query('75'), bottle.BaseRequest.query('76'), bottle.BaseRequest.query('77'), bottle.BaseRequest.query('78'), bottle.BaseRequest.query('79')],
        [bottle.BaseRequest.query('81'), bottle.BaseRequest.query('82'), bottle.BaseRequest.query('83'), bottle.BaseRequest.query('84'), bottle.BaseRequest.query('85'), bottle.BaseRequest.query('86'), bottle.BaseRequest.query('87'), bottle.BaseRequest.query('88'), bottle.BaseRequest.query('89')],
        [bottle.BaseRequest.query('91'), bottle.BaseRequest.query('92'), bottle.BaseRequest.query('93'), bottle.BaseRequest.query('94'), bottle.BaseRequest.query('95'), bottle.BaseRequest.query('96'), bottle.BaseRequest.query('97'), bottle.BaseRequest.query('98'), bottle.BaseRequest.query('99')]]
    #self.matrika = matrika
    #resen_sudoku = resi()
    return bottle.template('resen_sudoku.html', celamatrika=matrika)

@bottle.post("/matrika/")
def brisanje_sudokuja():
    trenutni_uporabnik().matrika = izbrisi_cel_sudoku()
    bottle.redirect("/matrika/")

from bottle import error
@error(404)
def error404(error):
    return 'Ta stran ne obstaja!'
bottle.run(debug=True, reloader=True)