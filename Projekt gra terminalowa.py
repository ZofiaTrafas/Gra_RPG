# import random
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw
#
# print("Powitanie! Studia blablabla wybory")
# #WYBOR SPOZNIENIE A PIZAMA
# print("budzisz sie, spozniony na zajecia. Co robisz?\n1 - spozniasz sie na zajecia, 2 - idziesz na zajecia w pizamie")
# wybor_spoznienie_pizama = int(input())
# #WYBOR SPOZNIENIE A PIZAMA - SPOZNIENIE
# if wybor_spoznienie_pizama == 1:
#     #WYBOR MICKIEWICZ A SLOWACKI
#     print("Spozniasz sie na zajecia. Prowadzacy za kare kaze ci wyrecytowac dzielo Slowackiego. Co recytujesz?\n 1 - oda do mlodosci, 2 - oda do wolnosci")
#     wybor_mickiewicz_slowacki = int(input())
#     #WYBOR MICKIEWICZ A SLOWACKI - MICKIEWICZ
#     if wybor_mickiewicz_slowacki == 1:
#         #ludzie nas nie lubia, wiec sympatia 1
#         sympatia_ludzi = 1
#     #WYBOR MICKIEWICZ A SLOWACKI - SLOWACKI
#     elif wybor_mickiewicz_slowacki == 2:
#         #Ludzie nas lubia, wiec sympatia 2
#         sympatia_ludzi = 2
#     else:
#         print("Zostala wprowadzona zla komenda")
# #WYBOR SPOZNIENIE A PIZAMA - PIZAMA
# elif wybor_spoznienie_pizama == 2:
#     #WYBOR ODPYSKUJ A PRZEPROS
#     print("Profesorowi sie nie podoba, ze jestes w pizamie. Co wybierasz?\n1 - odpyskuj, 2 - przepros")
#     wybor_odpyskuj_przepros = int(input())
#     # WYBOR ODPYSKUJ A PRZEPROS - ODPYSKUJ
#     if wybor_odpyskuj_przepros == 1:
#         #ludzie nas nie lubia, wiec sympatia 3
#         sympatia_ludzi = 3
#     #WYBOR ODPYSKUJ A PRZEPROS - PRZEPROS
#     elif wybor_odpyskuj_przepros == 2:
#         #Ludzie nas lubia, wiec sympatia 4
#         sympatia_ludzi = 4
# else:
#     print("Zostala wprowadzona zla komenda")
#
# #Tutaj nasze dwie początkowe ścieżki się spotykają, więc kontynuujmy tutaj.
#
#
#
#
# #ALTERNATYWKA A KONIARA A DZOKEJ
# print("Poznajesz nowe osobki. Masz do wyboru:\n1 - alternatywke, 2 - koniare, 3 - dzokeja")
# wybor_alternatywka_koniara_dzokej = int(input())
# #sympatia ludzi 2 i 4 to wtedy, gdy nas polubili. 3 i 4, gdy nie
#
# #funkcja ktora sluzy do sprawdzenia, dlaczego ktos cie polubil lub nie
# def sprawdzenie_sympatii_ludzi():
#     if sympatia_ludzi == 2:
#         print("Bardzo docenila to, ze znales utwor Slowackiego na zajeciach")
#     elif sympatia_ludzi == 4:
#         print("Spodobalo jej sie, ze pomimo tego, ze przyszedles w pizamie, to potrafiles przeprosic")
#     elif sympatia_ludzi == 1:
#         print("Nie spodobalo sie jej, ze przez ciebie bedzie kartkowka z tworczosci Slowackiego")
#     elif sympatia_ludzi == 3:
#         print("Nie spodobalo sie jej, ze nie dosc, ze przyszedles w pizamie, to jeszcze odpyskowales prowadzacemu")
#
# #jak ludzie cie polubili, to pierwszy wybor zostaje twoim przyjacielem (+ wyjasnienie dlaczego za pomoca funkcji)
# if sympatia_ludzi == 2 or sympatia_ludzi == 4:
#     if wybor_alternatywka_koniara_dzokej == 1:
#         print("Twoim przyjacielem zostaje alternatywka!")
#         wybor_przyjaciela = 1
#         sprawdzenie_sympatii_ludzi()
#     elif wybor_alternatywka_koniara_dzokej == 2:
#         print("Twoim przyjacielem zostaje koniara!")
#         wybor_przyjaciela = 2
#         sprawdzenie_sympatii_ludzi()
#     elif wybor_alternatywka_koniara_dzokej == 3:
#         print("Twoim przyjacielem zostaje dzokej!")
#         wybor_przyjaciela = 3
#         sprawdzenie_sympatii_ludzi()
#     else:
#         print("Zostala wprowadzona zla komenda")
#
# #jak ludzie cie nie polubili, to pierwszy wybor zostaje odrzucony (+ wyjasnienie dlaczego za pomoca funkcji), a pozniej wybor z pozostalych dwoch opcji
# elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
#     if wybor_alternatywka_koniara_dzokej == 1:
#         print("Alternatywka nie chce byc twoim przyjacielem!")
#         sprawdzenie_sympatii_ludzi()
#         print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n2 - koniara, 3 - dzokej")
#         wybor_przyjaciela = int(input())
#         if wybor_przyjaciela == 2:
#             print("Twoim przyjacielem zostaje koniara!")
#         elif wybor_przyjaciela == 3:
#             print("Twoim przyjacielem zostaje dzokej!")
#         else:
#             print("Zostala wprowadzona zla komenda")
#     elif wybor_alternatywka_koniara_dzokej == 2:
#         print("Koniara nie chce byc twoim przyjacielem!")
#         sprawdzenie_sympatii_ludzi()
#         print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n1 - alternatywka, 3 - dzokej")
#         wybor_przyjaciela = int(input())
#         if wybor_przyjaciela == 1:
#             print("Twoim przyjacielem zostaje alternatywka!")
#         elif wybor_przyjaciela == 3:
#             print("Twoim przyjacielem zostaje dzokej!")
#         else:
#             print("Zostala wprowadzona zla komenda")
#     elif wybor_alternatywka_koniara_dzokej == 3:
#         print("Dzokej nie chce byc twoim przyjacielem!")
#         sprawdzenie_sympatii_ludzi()
#         print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n1 - alternatywka, 2 - koniara")
#         wybor_przyjaciela = int(input())
#         if wybor_przyjaciela == 1:
#             print("Twoim przyjacielem zostaje alternatywka!")
#         elif wybor_przyjaciela == 2:
#             print("Twoim przyjacielem zostaje koniara!")
#         else:
#             print("Zostala wprowadzona zla komenda")
#     else:
#         print("Zostala wprowadzona zla komenda")
#
#
# #Znowu sciezki sie spotykaja, wiec kontynuujemy dalej
#
# #WYBOR WF, ale moze zrobimy to za pomoca cookie clickera
# print("Na jaki WF chcialbys uczeszczac?\n1 - praca w stajni, 2 - wyscigi konne, 3 - joga na koniach")
# wybor_wf = int(input())
# if wybor_wf == 1:
#     print("Bedziesz pracowac w stajni")
# elif wybor_wf == 2:
#     print("Bedziesz bral udzial w wyscigach konnych")
# elif wybor_wf == 3:
#     print("Bedziesz bral udzial w jodze na koniach")
#
#
# #WYBOR P I W E R K O  CZY WYKLAD
# print("Chcesz isc na piwo, czy na wyklad?\n1 - piwo, 2 - wyklad")
# wybor_piwo_wyklad = int(input())
# #piwo to licznik ile razy byles na piwie
# piwo = 0
# if wybor_piwo_wyklad == 1:
#     while piwo != 5:
#         piwo += 1
#         print("Poszedles na piwo. Chcesz isc na piwo czy wyklad?\n1 - piwo, 2 - wyklad")
#         wybor_piwo_wyklad_2 = int(input())
#         if wybor_piwo_wyklad_2 == 1:
#             print("Ile mozna?")
#         elif wybor_piwo_wyklad_2:
#             print("Idziesz na wyklad")
#             break
#     if piwo == 5:
#         print("Znajomi zaciagaja cie na wyklad, bo ile mozna pic")
#
# elif wybor_piwo_wyklad == 2:
#     print("Jako grzeczny student idziesz na wyklad")
#
# else:
#     print("Zostala wprowadzona zla komenda")
# print("piwo", piwo)
# #albo po piwie, albo bez piwa, ale docieramy na wyklad
#
# #WYBOR NIE POMOC CZY TAK
# print("Profesor ma problem z projektorem. Pomozesz mu?\n1 - nie, 2 - tak")
# wybor_nie_pomoc = int(input())
# if wybor_nie_pomoc == 1:
#     print("No slabo")
# elif wybor_nie_pomoc == 2:
#     #jak pomozesz to pozniej fajne rzeczy sie dzieja, likwiduje to pierwszy zly wybor!
#     print("Super uwu")
# else:
#     print("Zostala wprowadzona zla komenda")
#
# #EGZAMIN! Jesli piles piwo to jestes nieprzygotowany, jesli  nie piles to ogarniasz
#
#
# #dodaje to jako funkcje, zeby skrocic kod. jest to wybor czy chcesz sciagac czy nie plus czy chcesz miec poprawke czy nie
#
# def poprawka_czy_chcesz():
#     print("Czy chcesz poprawke?\n1 - tak, 2 - nie")
#     poprawka = int(input())
#     if poprawka == 1:
#         #przechodzi do opcji z poprawka
#         print("Bedziesz mial poprawke")
#     elif poprawka == 2:
#         #zakonczenie z makiem
#         print("Praca w maku")
#     else:
#         print("Zostala wprowadzona zla komenda")
#     return poprawka
#
# def sciaganie():
#     print("Co wybierasz?\n1 - sciagasz, 2 - nie sciagasz")
#     wybor_sciagasz_nie = int(input())
#     #WYBOR SCIAGANIE - SCIAGA
#     if wybor_sciagasz_nie == 1:
#         #zostaje przylapany
#         print("Zostalesz przylapany na sciaganiu")
#         return poprawka_czy_chcesz()
#     #WYBOR SCIAGANIE - NIE SCIAGA
#     elif wybor_sciagasz_nie == 2:
#         #szansa na zdanie jest losowa
#         szansa_na_zdanie = random.randint(1,prawdopodobienstwo_zdania)
#         if 1 < szansa_na_zdanie < 5:
#             print("Nie udało ci się zdać")
#             return poprawka_czy_chcesz()
#         else:
#             print("")
#     else:
#         print("Zostala wprowadzona zla komenda")
#     #nie chcesz poprawki, wiec jest ona rowna -1
#     return -1
#
#
#
#
#
# print("Nadeszla sesja. Masz egzamin.")
#
# if piwo == 0:
#     print("Brales udzial w wykladach, byles odpowiedzialny, zdajesz bez problemu")
#     poprawka = -1
# elif 3 >= piwo > 0:
#     #jak jestes srednio nauczony, to masz gorsze szanse zdania
#     print("Jestes srednio nauczony. Mozesz sciagac, narazajac sie na przylapanie, albo sprobowac napisac to samemu (masz male szanse zdanie).")
#     prawdopodobienstwo_zdania = 10
#     poprawka = sciaganie()
#
# elif 5 >= piwo > 3:
#     #jak tylko byles na piwie, to w ogole slabe szanse
#     print("Jestes zle nauczony. Mozesz sciagac, narazajac sie na przylapanie, albo sprobowac napisac to samemu (masz BARDZO male szanse zdanie).")
#     prawdopodobienstwo_zdania = 7
#     poprawka = sciaganie()
#
#
# #dodaje to jako funkcje, zeby skrocic kod. jest to wybor czy chcesz sprobowac ponownie czy nie
# def sprobuj_ponownie():
#     print("Chcesz sprobowac od nowa?\n1 - tak, 2 - nie")
#     wybor_od_nowa = int(input())
#     if wybor_od_nowa == 1:
#         print("witamy ponownie")
#         #start programu od nowa, tylko z nowymi dialogami
#     elif wybor_od_nowa == 2:
#         #zakonczenie z makiem
#         print("Pracujesz w maku")
#     else:
#         print("Zostala wprowadzona zla komenda")
#
# if poprawka == 1:
#     #tutaj sprawdzamy poprzednie wybory. Jesli ktos tylko pil piwo, to zdaje. Jesli ktos oprocz piwa recytowal mickiewicza, albo pyskowal - nie zdaje, chyba ze pozniej pomogl profesorowi z projektorem.
#     if wybor_mickiewicz_slowacki == 1 and wybor_nie_pomoc == 1:
#         print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach recytowales mickiewicza zamiast slowackiego, przez co nie zdajesz przedmiotu z gwiazdka.")
#         sprobuj_ponownie()
#     elif wybor_mickiewicz_slowacki == 1 and wybor_nie_pomoc == 2:
#         print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach recytowales mickiewicza zamiast slowackiego, ale przypomina sobie, ze jego kolega cie chwalil, ze pomogles mu z projektorem, wiec jest pozytywnie do ciebie nastawiony i zdajesz")
#     elif wybor_spoznienie_pizama == 1 and wybor_nie_pomoc == 1:
#         print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach przyszedles w pizamie i odpyskowales, przez co nie zdajesz przedmiotu z gwiazdka.")
#         sprobuj_ponownie()
#     elif wybor_spoznienie_pizama == 1 and wybor_nie_pomoc == 2:
#         print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach przyszedles w pizamie i odpyskowales,ale przypomina sobie, ze jego kolega cie chwalil, ze pomogles mu z projektorem, wiec jest pozytywnie do ciebie nastawiony i zdajesz")
#
# #tutaj leci historia dla tych, ktorzy zdali
#
# print("Gratulacje, zdales!")
# if wybor_przyjaciela == 1:
#     print("Ty i twoja przyjaciolka alternatywka pomyslnie zdajecie pierwszy semestr")
# elif wybor_przyjaciela == 2:
#     print("Ty i twoja przyjaciolka koniara pomyslnie zdajecie pierwszy semestr")
# elif wybor_przyjaciela == 3:
#     print("Ty i twoj przyjaciel dzokej pomyslnie zdajecie pierwszy semestr")
#
# if wybor_wf == 1:
#     print("a ty odnosisz sukcesy pracujac w stajni w ramach WFu")
# elif wybor_wf ==2:
#     print("a ty odnosisz sukcesy w wyscigach konnych w ramach WFu")
# elif wybor_wf == 3:
#     print("a ty jestes zrelaksowany po calym semestrze jogi na koniach")


#D R U G I    S E M E S T R

from tkinter import *
import time
import os
import random
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw

tura = 0        # napisy i odpowiedzi są przy4dzielane przyciskom wg. "tury". Opcja_1 = +1 tura Opcja_2 = +10 tur Opcja_3 = +20 tur
sympatia_ludzi = 0

okno_test = Tk()
okno_test.title("Testuje przyciski")
# okno_test.geometry("600x400")

#
plotno=Canvas(okno_test, width=800,height=400)
plotno.pack()
obraz1=Image.open("1.Uniwersytet.jpg")
obraz1=obraz1.resize((400,400))
obrazTk=ImageTk.PhotoImage(obraz1)
plotno.create_image(400,200,image=obrazTk)

plotno=Canvas(okno_test, width=800,height=400)
plotno.pack()
obraz2=Image.open("2.Pokój w akademiku.jpg")
obraz2=obraz2.resize((400,400))
obrazTk=ImageTk.PhotoImage(obraz2)
plotno.create_image(400,200,image=obrazTk)

plotno=Canvas(okno_test, width=800,height=400)
plotno.pack()
obraz3=Image.open("3.Zegar.jpg")
obraz3=obraz3.resize((400,400))
obrazTk=ImageTk.PhotoImage(obraz3)
plotno.create_image(400,200,image=obrazTk)

def wybor_1():  # wyskakuje po naciśnięciu przycisk_1
    global tura # bez tego nie liczy tur
    global sympatia_ludzi
    tura = tura + 1
    if tura == 1:
        # tekst.configure - zmienia zmienną "tekst", dzięki temu nie otwiera się nowe okno
        # wybór nr 1.1 - spóźnienie, co recytwoać? (0+1tura)
        tekst.configure(text = "(przycisk 1)\nSpozniasz sie na zajecia.\nProwadzacy za kare kaze ci wyrecytowac dzielo Slowackiego. Co recytujesz?")
        przycisk_1.configure(text = " oda do mlodosci ")
        przycisk_2.configure(text = " oda do wolnosci ")
        przycisk_3.configure(text = "                 ")
    elif tura == 2:
        # wybór nr 1.2 - Mickiewicz, wybierz przyjaciela (1+1tura)
        tekst.configure(text = "Poznajesz nowe osobki.\nWybierz przyjaciela")
        reakcje.configure(text = "(przycisk 1+1; tura 2)\nLudzie nas nie lubią [Mickiewicz]")
        przycisk_1.configure(text = " alternatywka ")
        przycisk_2.configure(text = " koniara ")
        przycisk_3.configure(text = "dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 1
    elif tura == 11:
        #wybór 2.1 - przeproszony prof, wybierz przyjaciela (10+1 tura)
        tekst.configure(text = "Poznajesz nowe osobki.\nWybierz przyjaciela")
        reakcje.configure(text = "(przycisk 2+1)\nLudzie nas lubią [przeproszony prof] ")
        przycisk_1.configure(text = " alternatywka ")
        przycisk_2.configure(text = " koniara ")
        przycisk_3.configure(text = "dżokej", bg = "yellow", state = "normal") #"normal" odblokowuje trzeci przycisk
        sympatia_ludzi = sympatia_ludzi + 4
    elif tura > 2 and tura < 36:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje alternatywka!") #[przycisk: 1+2+1 or 2+1+1 ; tury: 12 ]
            wybor_przyjaciela = 1
            sprawdzenie_sympatii_ludzi()
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Alternatywka nie chce byc twoim przyjacielem! Wybierz kogoś innego.") # [przycisk: 1+1+1 or 2+2+1; tury: 3 or 21]
            wybor_przyjaciela = 1
            sprawdzenie_sympatii_ludzi()
            przycisk_1.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1
    else:
        tekst.configure(text = ("KONIEC, poziom sympatii wynosi: ",sympatia_ludzi))
        przycisk_1.configure(state = "disabled", bg = "grey")    # przycisków nie da się dalej naciskać
        przycisk_2.configure(state = "disabled", bg = "grey")
        przycisk_3.configure(state = "disabled", bg = "grey")


def wybor_2():  # wyskakuje po naciśnięciu przycisk_2
    global tura
    global sympatia_ludzi
    tura = tura + 10
    if tura == 10:
        tekst.configure(text = "(przycisk 2)\nProfesorowi sie nie podoba, ze jestes w pizamie. Co wybierasz?")
        przycisk_1.configure(text = " Przeproś ")
        przycisk_2.configure(text = " Odpyskuj ")
        przycisk_3.configure(text = "          ")
    elif tura == 11:
        tekst.configure(text = "Poznajesz nowe osobki.\nWybierz przyjaciela")
        reakcje.configure(text = "(przycisk 1+2)\nLudzie nas lubią [Słowacki]")
        przycisk_1.configure(text = " alternatywka ")
        przycisk_2.configure(text = " koniara ")
        przycisk_3.configure(text = "dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 2
    elif tura == 20:
        tekst.configure(text = "Poznajesz nowe osobki.\nWybierz przyjaciela")
        reakcje.configure(text = "(przycisk 2+2; tura 11)\nLudzie nas nie lubią [odpyskowany prof]")
        przycisk_1.configure(text = " alternatywka ")
        przycisk_2.configure(text = " koniara ")
        przycisk_3.configure(text = "dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 3
    elif tura > 2 and tura < 36:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje koniara!")
            wybor_przyjaciela = 2
            sprawdzenie_sympatii_ludzi()
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Koniara nie chce byc twoim przyjacielem! Wybierz kogoś innego.")
            wybor_przyjaciela = 2
            sprawdzenie_sympatii_ludzi()
            przycisk_2.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1
    else:
        tekst.configure(text = ("KONIEC, poziom sympatii wynosi: ",sympatia_ludzi))
        przycisk_1.configure(state = "disabled", bg = "grey")
        przycisk_2.configure(state = "disabled", bg = "grey")
        przycisk_3.configure(state = "disabled", bg = "grey")


def wybor_3():
    global tura
    global sympatia_ludzi
    tura = tura + 20
    if tura > 2 and tura < 36:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje dżokej!")
            wybor_przyjaciela = 3
            sprawdzenie_sympatii_ludzi()
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Dżokej nie chce byc twoim przyjacielem! Wybierz kogoś innego.")
            wybor_przyjaciela = 3
            sprawdzenie_sympatii_ludzi()
            przycisk_3.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1
    else:
        tekst.configure(text = ("KONIEC, poziom sympatii wynosi: ",sympatia_ludzi))
        przycisk_1.configure(state = "disabled", bg = "grey")
        przycisk_2.configure(state = "disabled", bg = "grey")
        przycisk_3.configure(state = "disabled", bg = "grey")# wyskakuje po naciśnięciu przycisk_3; potrzebny tylko do wyboru przyjaciół, chyba że coś jeszcze w 2sem?


def sprawdzenie_sympatii_ludzi():
    global sympatia_ludzi
    if sympatia_ludzi == 2:
        reakcje.configure(text = "Bardzo docenila to, ze znales utwor Slowackiego na zajeciach")
    elif sympatia_ludzi == 4:
        reakcje.configure(text = "Spodobalo jej sie, ze pomimo tego, ze przyszedles w pizamie, to potrafiles przeprosic")
    elif sympatia_ludzi == 1:
        reakcje.configure(text = "Nie spodobalo sie jej, ze przez ciebie bedzie kartkowka z tworczosci Slowackiego")
    elif sympatia_ludzi == 3:
        reakcje.configure(text = "Nie spodobalo sie jej, ze nie dosc, ze przyszedles w pizamie, to jeszcze odpyskowales prowadzacemu")#uzupełnia "dialogi"(odpowiedzi?) po zaproponowaniu przyjaźni
# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# # MINI GRA
# from tkinter import *
# import time
# # from tkinter.ttk import *
#
# #definicja odpowiada za odliczanie 5 sekund
# def rozpoczęcie_odliczania():
#     time.sleep(1)
#     print("START")
#     time.sleep(5)
#     print("STOP")
#
# #definicja odpowiada za zliczanie ilości kliknięć i w zależności od ilości wybór dyscypliny
# liczba = 0
# def kliknięcia(): # without event because I use `command=` instead of `bind`
#     global liczba
#     liczba = liczba + 1
#     if liczba<=10:
#         dyscyplina="Jesteś powolny i dokładny, Twoja dyscyplina to praca w stajni"
#     elif liczba>=20:
#         dyscyplina="Jesteś bardzo szybki, Twoja dyscyplina to wyścigi konne"
#     else:
#         dyscyplina="Jesteś opanowany i spokojny, Twoja dyscyplina to joga na koniach"
#     label1.configure(text=f'STOP! Liczba kliknięć: {liczba} {dyscyplina}')
#
#
# windows = Tk()
# windows.title("Wybór dyscypliny")
# windows.geometry("600x500")
# label = Label(windows, text="To najwyższy czas na zapisanie się na zajęcia wychowania fizycznego. Do wyboru masz trzy dyscypliny:"
# "\n"
# "\n a) praca w stajni"
# "\n b) wyścigi konne"
# "\n c) joga na koniach"
# "\n"
# "\n Sprawdźmy do czego się nadajesz."
# "\n Kiedy będziesz gotowy naciśnij \"START\""
# "\n A następnie wciskaj klawisz \"Naćiśnij\" tak dużo razy jak potrafisz aż do momentu pojawienia STOP.")
#
# label.grid(column=0, row=0)
# label1 = Label(windows, text = "_____________________________")
# label1.grid(column=0, row=6)
# custom_button = Button(windows, text="Naciśnij", command=kliknięcia)
# custom_button.grid(column=0, row=5)
# przycisk_startu=Button(windows, text="START", command=rozpoczęcie_odliczania)
# przycisk_startu.grid(column=0, row=3)
#
# windows.mainloop()

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# okno_test = Tk()
# okno_test.title("Testuje przyciski")
# okno_test.geometry("800x300")

#WPROWADZENIE - imię i przywitanie - niedziała, nwm czemu, ale jeszcze pobrubuję

# podaj_imie = Entry(okno_test, width = 10)
# podaj_imie.grid(column = 3, row = 3)
# podaj_imie.focus()  # nietrzeba klikać na txtbox żeby zacząć pisać
# imie = podaj_imie.get()
# podaj_imie.grid_remove()
#
# tekst = Label(okno_test, text = ("Cześć", imie, "wprowadzenie"), font = ("Arial Bold", 13))
# tekst.grid(column = 0, row = 0)
# time.sleep(3)
# tekst.configure(text = "Budzisz sie, spozniony na zajecia. Co robisz?")

#START - pierwszy wybór i baza do reszty, jak zadziała to u góry ten będzie zbędny

reakcje = Label(okno_test, text = "")
reakcje.place(x = 250,y = 200)

tekst = Label(okno_test, text = "Budzisz sie, spozniony na zajecia. Co robisz?", font = ("Arial Bold", 13))
tekst.place(x = 200,y = 50)

#RZECZY POTZREBNE I KONIECZNE :P

#Do notatek/ sprawdzenia czy wszystko działa i uzasadnień przyjaciół


#Przycisk_3 jest aktywowany w odpowiednich miejscach w funkcajch wyborów + po wyborze przyjaciół będzie usunięty
przycisk_1 = Button(okno_test, text = " Spozniasz sie na zajecia ", bg = "yellow", command = wybor_1, compound=TOP)
przycisk_1.place(x = 150,y =  150)

przycisk_2 = Button(okno_test, text = " Idziesz na zajecia w pizamie ", bg = "yellow", command = wybor_2,compound=TOP)
przycisk_2.place(x = 350,y =  150)

przycisk_3 = Button(okno_test, text = "                                          ", bg = "yellow", command = wybor_3,compound=TOP)
przycisk_3.place(x = 600,y =  150)
przycisk_3.configure(state = "disabled", bg = "grey")

# def powitanie():
#     messagebox.showinfo("Powitanie","Witaj! Jesteś studentem I roku Koniowistyki na Uniwerystecie Juliusza Słowackiego.")
#     messagebox.showinfo("Rada na początek nauki","Okres studiów to najlepszy czas w Twoim życiu. Pamiętaj, żeby go nie zmarnować...")

# plotno=Canvas(okno_test, width=400, height=400)
# plotno.pack()
# obraz=Image.open("1.Uniwersytet.jpg")
# obraz=obraz.resize((400,400))
# obrazTk=ImageTk.PhotoImage(obraz)
# plotno.create_image(200,200,image=obrazTk)
# przycisk1=Button(okno_test, text="Powitanie",command=powitanie)
# przycisk1.pack()


okno_test.mainloop()
