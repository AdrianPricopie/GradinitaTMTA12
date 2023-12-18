# GRADINITA
"""Abstractizare
Creati o clasa abstracta numita Gradinita care sa mosteneasca clasa ABC
(abstract base class) care sa aiba urmatoarele metode:

activitate_practica()
ora_de_somn()

Corpul primei metode va fi “pass” iar corpul celei de-a doua metode va contine
un raise NotImplementedException (estimeaza cineva ce inseamna acest raise NotImplementedException?).
Fiecare din cele doua metode vor avea decoratorul @abstractbaseclass (ce este un decorator?)
Implementati doua clase: GradinitaPublica si GradinitaPrivata care sa implementeze (mosteneasca) clasa abstracta Gradinita.
Prima clasa, GradinitaPublica va rescrie ambele metode in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa deseneze”
ora_de_somn() va printa pe ecran: “copiii trebuie sa doarma la ora cinci”
A doua clasa, GradinitaPrivata va rescrie o singura metoda in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa modeleze cu plastilina”

Rulati codul. Se intampla ceva?
Instantiati un obiect din clasa GradinitaPublica si rulati codul. Se printeaza ceva pe ecran? De ce?
Apelati metoda activitate_practica() si rulati codul. Ce observati?
Instantiati un obiect din clasa GradinitaPrivata si rulati codul. De ce va da eroare?
Cum putem sa rezolvam eroarea?
"""
from abc import ABC, abstractmethod

class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Metoda trebuie implementata in clasele derivate")
class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print("Copiii invata sa deseneze")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora cinci")

class GradinitaPrivata(Gradinita):
    def activitate_practica(self):
        print("Copiii invata sa modeleze cu plastilina")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora cinci")

# Instantierea obiectului din clasa GradinitaPublica
gradinita_publica = GradinitaPublica()

# Apelarea metodelor
gradinita_publica.activitate_practica()
gradinita_publica.ora_de_somn()

# Instantierea obiectului din clasa GradinitaPrivata
gradinita_privata = GradinitaPrivata()

# Apelarea metodelor
gradinita_privata.activitate_practica()
gradinita_privata.ora_de_somn()
"""
Explicatii : NotImplementedError este ridicată în corpul metodei ora_de_somn() 
pentru a indica că această metodă trebuie implementată în clasele derivate.
GradinitaPublica implementează ambele metode definite în clasa de bază Gradinita.
GradinitaPrivata implementează doar o singură metodă, ceea ce duce la o eroare în 
timpul instanțierii, deoarece nu îndeplinește toate metodele abstracte definite în 
clasa de bază. Pentru a rezolva eroarea, trebuie să implementăm și metoda ora_de_somn() 
în clasa GradinitaPrivata
"""


"""
Mostenire
Creati o noua clasa: GradinitaPublica25 care sa mosteneasca clasa GradinitaPublica. 
Implementati doar una din metode in felul urmator:
activitate_practica() va printa pe ecran: “Copiii se joaca in curte pe balansoar”

Instantiati un obiect din clasa GradinitaPublica25.
Prin intermediul obiectului instantiat apelati metodele activitate_practica() 
si ora_de_somn(). Ce se printeaza pe ecran? De ce putem sa apelam si metoda somn?
"""
class GradinitaPublica25(GradinitaPublica):
    def activitate_practica(self):
        print("Copiii se joaca in curte pe balansoar")

    # def calculeaza_media_buline_rosii(self):
    #     numar_elevi = int(input("Introduceți numărul de elevi: "))
    #     buline_rosii = []
    #
    #     for i in range(numar_elevi):
    #         buline = int(input(f"Introduceți numărul de buline roșii pentru elevul {i + 1}: "))
    #         buline_rosii.append(buline)
    #
    #     media = sum(buline_rosii) / numar_elevi
    #
    #     if media > 5:
    #         print("Elevii acestei grădinițe sunt foarte neastâmpărați.")
    #     else:
    #         print("Elevii gradinitei sunt foarte cuminti.")


    def __init__(self):
            self.public = "Atribut public"
            self.__private = "Atribut privat"
            self._protected = "Atribut protejat"

        # alte metode din clasa

    def get_private(self):
            return self.__private

    def set_private(self, valoare):
            self.__private = valoare

    def del_private(self):
            del self.__private

gradinita_publica_25 = GradinitaPublica25()

# Accesarea atributului public
print(gradinita_publica_25.public)  # Nu va returna eroare, se poate accesa direct

# Accesarea atributului privat
# print(gradinita_publica_25.__private)  # Acesta va returna eroare pentru că încercăm să accesăm un atribut privat direct

# Accesarea atributului protejat
# print(gradinita_publica_25._protected)  # Nu va returna eroare, dar este considerat "protejat" și nu ar trebui să fie accesat direct

# Utilizarea getter-ului pentru atributul privat
print(gradinita_publica_25.get_private())  # Va returna valoarea atributului privat

# Utilizarea setter-ului pentru atributul privat
gradinita_publica_25.set_private("Noua valoare")  # Setăm o nouă valoare pentru atributul privat

# Utilizarea deleter-ului pentru atributul privat
gradinita_publica_25.del_private()  # Ștergem atributul privat
# print(gradinita_publica_25.get_private())  # Va returna eroare pentru că atributul privat a fost șters



# Instantierea obiectului din clasa GradinitaPublica25
gradinita_25 = GradinitaPublica25()

# Apelarea metodelor
gradinita_25.activitate_practica()
gradinita_25.ora_de_somn()

# Apelarea metodei adăugate în clasa GradinitaPublica25
# gradinita_25.calculeaza_media_buline_rosii()

"""
Explicatii:Clasa GradinitaPublica25 mosteneste clasa GradinitaPublica, 
astfel încât mostenirea metodei ora_de_somn() vine de la clasa de bază.
Apelând metodele prin intermediul obiectului gradinita_25, se observă că 
metoda activitate_practica() a fost suprascrisă în clasa GradinitaPublica25, 
iar metoda ora_de_somn() este moștenită de la clasa de bază GradinitaPublica.
"""

"""
Polimorfism
In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de 
la tastatura numarul de buline rosii pe care le-a primit fiecare elev in parte,
 procesati-le si calculati media aritmetica a numarului de buline rosii. 
 Daca aceasta este mai mare decat cinci, printati pe ecran: “Elevii acestei gradinite 
 sunt foarte neastamparati”.
"""

"""
Bonus:
In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de 
la tastatura un dictionar care sa contina o serie de perechi cheie:valoare si dictionare
 imbricate (embedded, nested) care sa contina urmatoarele informatii: numele elevului, 
 numele parintilor, varsta elevului, activitatea preferata. Printati pentru 
 fiecare elev toate informatiile de mai sus.
"""




"""

Encapsulare
In interiorul clasei GradinitaPublica25 creati trei atribute: unul public, 
unul private si unul protected.

Prin intermediul obiectului instantiat din clasa apelati pe rand: 
atributul public, atributul private si respectiv pe cel protected. Care din cele trei sunt sugerate atunci cand scriem numele obiectului instantiat urmat de caracterul “.”?

Rulati codul. Accesarea caruia dintre atribute returneaza eroare?

Implementati in interiorul clasei GradinitaPublica25 un getter, un setter 
si un deleter pentru atributul private. Cum ne putem folosi de acestia pentru 
accesarea acestui atribut in afara clasei?
"""
