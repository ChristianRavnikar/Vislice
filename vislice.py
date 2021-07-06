import bottle
import model

SKRIVNOST = 'moja skrivnost'

vislice = model.Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

# @bottle.post("/igra/")
# def nova_igra():
#     id_igre = vislice.nova_igra()
#     novi_url = f"/igra/{id_igre}/"
#     bottle.redirect(novi_url)

@bottle.post("/nova-igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', f'idigre{id_igre}', secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')

# @bottle.get("/igra/<id_igre:int>/")
# def pokazi_igro(id_igre):
#     trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
#     return bottle.template("igra.tpl", igra=trenutna_igra, stanje=trenutno_stanje)

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=trenutna_igra, stanje=trenutno_stanje)

# @bottle.post("/igra/<id_igre:int>/")
# def ugibaj_na_igri(id_igre):
#     ugibana = bottle.request.forms["crka"]
#     vislice.ugibaj(id_igre, ugibana)
#     return bottle.redirect(f"/igra/{id_igre}/")

@bottle.post('/igra/')
def ugibaj_na_igri():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    ugibana = bottle.request.forms["crka"]
    vislice.ugibaj(id_igre, ugibana)
    return bottle.redirect('/igra/')


@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path, "img")

#Vse kar pride v /im/ nekiii , to je statična datoteka, ki loh gre tut na drug server iskat al pa nekam drugam

bottle.run(reloader=True, debug=True)