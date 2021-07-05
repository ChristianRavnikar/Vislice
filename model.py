import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra(bazen_besed)
        self.igre[nov_id] = (sveza_igra, ZACETEK)
        return nov_id

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)

""" Druga možnost:
    def prost_id_igre(self):
        if not self.igre: return 0
        m = max(self.igre.keys())
        return m + 1
"""


class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
# ne smemo dati privzete vrednosti crke =[], ker potem
# ce naredimo dve igri bo ko spremenimo seznam od ene se spremenil tudi od druge
# tipicna resitev je crke=None, potem pa locimo; če crke is none, damo crke na [], sicer pa pustimo

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
        # izpeljani seznam

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(crka in self.crke for crka in self.geslo)
        #spet izpeljani seznami
        # crka in self.crke vrne logično vrednost, true če je crka res v self.crke in false ce ni
        # preverimo ali so vse črke iz gesla v našem seznamu ugibanih črk

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
        #če presežemo število dovoljenih napak izgubimo

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            if crka in self.crke:
                s += crka + ' '
            else:
                s += '_ '
        return s
    # pogledamo ali je črka iz gesla v našem izboru črk,
    # če je te črke izpišemo, če ni pa zapišemo _ na še neugotovljene črke

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
    # pred join zapišemo niz ki ga uporabi kot presledek,
    # za parameter pa mu damo seznam nizov, ki jih je treba staknit

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

# z metodo .strip bomo porezali znake za skok v novo vrstico
with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]


def nova_igra():
    return Igra(random.choice(bazen_besed))
