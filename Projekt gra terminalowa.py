import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw


from tkinter import *
import time
import os

tura = 0        # napisy i odpowiedzi są przydzielane przyciskom wg. "tury". Opcja_1 = +1 tura Opcja_2 = +10 tur Opcja_3 = +20 tur
sympatia_ludzi = 0
piwo = 0
sesja = 0

def wybor_1():  # wyskakuje po naciśnięciu przycisk_1
    global tura # bez tego nie liczy tur
    global sympatia_ludzi
    global piwo
    tura = tura + 1
    if tura == 1:
        # tekst.configure - zmienia zmienną "tekst", dzięki temu nie otwiera się nowe okno
        # wybór nr 1.1 - spóźnienie, co recytwoać? (0+1tura)
        tekst.configure(text ="(przycisk 1)\n Wchodząc do sali zatrzymuje Cię oburzony wykładowca.\n \"Na moje zajęcia nikt się nie spóźnia!\" - mówi - \"Czy Ty wiesz na jakim Uniwersytecie studiujesz? \n Na Uniwersytecie Juliusza Słowackiego! Proszę mi w takim razie wyrecytować jego utwór.\" \n ""Co wybierasz?")
        przycisk_1.configure(text = " Oda do wolności ")
        przycisk_2.configure(text = " Oda do młodości ")
        przycisk_3.configure(text = "                 ")
    elif tura == 2 and sympatia_ludzi == 0:
        tekst.configure(text = "Następnego dnia przychodzisz na uczelnie trochę za wcześnie, \n ale to dobry moment, by poznać nowych przyjaciół.\nWybierz z kim chcesz nawiązać kontakt")
        reakcje.configure(text = "(przycisk 1+2)\nLudzie nas lubią [Słowacki]")
        przycisk_1.configure(text = " Alternatywka ")
        przycisk_2.configure(text = " Koniara ")
        przycisk_3.configure(text = "Dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 2
    elif tura == 3 and sympatia_ludzi == 0:
        tekst.configure(text = "Następnego dnia przychodzisz na uczelnie trochę za wcześnie, \n ale to dobry moment, by poznać nowych przyjaciół.\nWybierz z kim chcesz nawiązać kontakt")
        reakcje.configure(text = "(przycisk 2+2; tura 11)\nLudzie nas nie lubią [odpyskowany prof]")
        przycisk_1.configure(text = " Alternatywka ")
        przycisk_2.configure(text = " Koniara ")
        przycisk_3.configure(text = "Dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 3
    elif tura > 2 and tura < 6:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje alternatywka!")
            wybor_przyjaciela = 1
            sprawdzenie_sympatii_ludzi()
            if tura == 3:
                tura = tura + 3
            elif tura == 4:
                tura = tura + 2
            elif tura == 5:
                tura = tura + 1
            przycisk_1.configure(state = "disabled", bg = "grey", text = "         ")
            przycisk_2.configure(text = "NEXT STEP", bg = "yellow")
            przycisk_3.configure(state = "disabled", bg = "grey", text = "         ")
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Alternatywka nie chce byc twoim przyjacielem! Wybierz kogoś innego.")
            wybor_przyjaciela = 1
            sprawdzenie_sympatii_ludzi()
            przycisk_1.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1
    elif tura == 6:
        tekst.configure(text = "Twoim przyjacielem zostaje alternatywka!")
        wybor_przyjaciela = 1
        sprawdzenie_sympatii_ludzi()
        przycisk_1.configure(state = "disabled", bg = "grey", text = "         ")
        przycisk_2.configure(text = "NEXT STEP", bg = "yellow")
        przycisk_3.configure(state = "disabled", bg = "grey", text = "         ")
    elif tura >= 12 and tura <= 16:  #piwo
        przycisk_start.configure(state = "disabled", bg = "grey")
        if piwo != 5:
            piwo += 1
            tekst.configure(text = "Poszedles na piwo. Chcesz isc na piwo czy wyklad?")
            przycisk_1.configure(text = " piwo ")
            przycisk_2.configure(text = "wykład")
            if tura == 13:
                reakcje.configure(text = "Ile mozna?")
            tura = tura + 1
        elif piwo == 5:
            if tura == 12:
                tura = tura + 4
            elif tura == 13:
                tura = tura + 3
            elif tura == 14:
                tura = tura + 2
            elif tura == 15:
                tura = tura + 1
            tekst.configure(text = "Znajomi zaciagaja cie na wyklad, bo ile mozna pic\n Profesor ma problem z projektorem. Pomozesz mu?")
            reakcje.configure(text = " ")
            przycisk_1.configure(text = "tak")
            przycisk_2.configure(text = "nie")
    elif tura = 17:
        test.configure(text = " Super uwu ")
        przycisk_1.configure(state = "disabled", text = "      ", bg = "grey", command = egzamin_1)
        przycisk_2.configure(text = "Nadeszla sesja. Masz egzamin", bg = "green", command = egzamin_2)

        

def wybor_2():  # wyskakuje po naciśnięciu przycisk_2
    global tura
    global sympatia_ludzi
    tura = tura + 2
    if tura == 2:
        tekst.configure(text ="(przycisk 2)\n Wchodząc do sali zatrzymuje Cię oburzony wykładowca. \n  \"Czy Ty sobie kpisz z moich zajęć?\" -mówi - \"Jak bezczelnym trzeba być, żeby przyjść tak ubranym?\" \n Co odpowiadasz?")
        przycisk_1.configure(text = "Będę się ubierać jak chcę. ")
        przycisk_2.configure(text = " Przepraszam Profesorze ")
        przycisk_3.configure(text = "          ")
    elif tura == 3 and sympatia_ludzi == 0:
        tekst.configure(text ="Następnego dnia przychodzisz na uczelnie trochę za wcześnie, \n ale to dobry moment, by poznać nowych przyjaciół.\nWybierz z kim chcesz nawiązać kontakt")
        reakcje.configure(text = "(przycisk 1+1; tura 2)\nLudzie nas nie lubią [Mickiewicz]")
        przycisk_1.configure(text = " Alternatywka ")
        przycisk_2.configure(text = " Koniara ")
        przycisk_3.configure(text = "Dżokej", bg = "yellow", state = "normal")
        sympatia_ludzi = sympatia_ludzi + 1
    elif tura == 4 and sympatia_ludzi == 0:
        tekst.configure(text ="Następnego dnia przychodzisz na uczelnie trochę za wcześnie, \n ale to dobry moment, by poznać nowych przyjaciół.\nWybierz z kim chcesz nawiązać kontakt")
        reakcje.configure(text = "(przycisk 2+1)\nLudzie nas lubią [przeproszony prof] ")
        przycisk_1.configure(text = " Alternatywka ")
        przycisk_2.configure(text = " Koniara ")
        przycisk_3.configure(text = "Dżokej", bg = "yellow", state = "normal") #"normal" odblokowuje trzeci przycisk
        sympatia_ludzi = sympatia_ludzi + 4

    elif tura > 1 and tura <= 6:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje koniara!")
            wybor_przyjaciela = 2
            sprawdzenie_sympatii_ludzi()
            if tura == 3:
                tura = tura + 3
            elif tura == 4:
                tura = tura + 2
            elif tura == 5:
                tura = tura + 1
            przycisk_1.configure(state = "disabled", bg = "grey", text = "         ")
            przycisk_2.configure(state = "normal", text = "NEXT STEP", bg = "yellow")
            przycisk_3.configure(state = "disabled", bg = "grey", text = "         ")
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Koniara nie chce byc twoim przyjacielem! Wybierz kogoś innego.")
            wybor_przyjaciela = 2
            sprawdzenie_sympatii_ludzi()
            przycisk_2.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1

    elif tura == 8: ## MIEJSCE GRY - NIEGOTOWE
        tekst.configure(text = "To najwyższy czas na zapisanie się na zajęcia wychowania fizycznego. \n Do wyboru masz trzy dyscypliny:"
        "\n a) praca w stajni"
        "\n b) wyścigi konne"
        "\n c) joga na koniach"
        "\n Sprawdźmy do czego się nadajesz."
        "\n Kiedy będziesz gotowy naciśnij \"START\""
        "\n A następnie wciskaj klawisz \"Naćiśnij\" tak dużo razy jak potrafisz aż do momentu pojawienia STOP.")
        przycisk_1.configure(state = "disabled",text = "             " ,bg = "grey")
        przycisk_2.configure(state = "normal", text = "START", bg = "yellow")
        przycisk_3.configure(state = "normal", text = "Przejdź dalej" ,bg = "grey")
        dodaje_przycisk()
        
    elif tura >= 13 and tura <= 16:
        if tura == 12:
            tura = tura + 4
        elif tura == 13:
            tura = tura + 3
        elif tura == 14:
            tura = tura + 2
        elif tura == 15:
            tura = tura + 1
        tekst.configure(text = "Idziesz na wyklad\n Profesor ma problem z projektorem. Pomozesz mu?")
        przycisk_1.configure(text = "tak")
        przycisk_2.configure(text = "nie")
        przycisk_start.configure(state = "disabled", bg = "grey")
    elif tura = 17:
        test.configure(text = "słabo")
        przycisk_1.configure(state = "disabled", text = "      ", bg = "grey")
        przycisk_2.configure(text = "czas na egazamin", bg = "green", command = egzamin_2)


def wybor_3():
    global tura
    global sympatia_ludzi
    tura = tura + 1
    if tura > 1 and tura <= 6:
        if sympatia_ludzi == 2 or sympatia_ludzi == 4:
            tekst.configure(text = "Twoim przyjacielem zostaje dżokej!")
            wybor_przyjaciela = 3
            sprawdzenie_sympatii_ludzi()
            if tura == 3:
                tura = tura + 3
            elif tura == 4:
                tura = tura + 2
            elif tura == 5:
                tura = tura + 1
            przycisk_1.configure(state = "disabled", text = "         ",bg = "grey")
            przycisk_2.configure(text = "NEXT STEP", bg = "yellow")
            przycisk_3.configure(state = "disabled", text = "         ",bg = "grey")
            dodaje_przycisk()
        elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
            tekst.configure(text = "Dżokej nie chce byc twoim przyjacielem! Wybierz kogoś innego.")
            wybor_przyjaciela = 3
            sprawdzenie_sympatii_ludzi()
            przycisk_3.configure(state = "disabled")
            sympatia_ludzi = sympatia_ludzi + 1
            tura = tura + 1
    elif tura == 11:
        tekst.configure(text = "Chcesz isc na piwo, czy na wyklad?")
        reakcje.configure(text = " ")
        przycisk_1.configure(state = "normal", text = " piwo ", bg = "yellow")
        przycisk_2.configure(text = "wykład")
        przycisk_3.configure(text = "      ", state = "disabled", bg = "grey")            
        

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

def dodaje_przycisk():
    przycisk_start = Button(okno_test, text = "Naciśnij", bg = "green")
    przycisk_start.place(x = 350,y = 170)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# MINI GRA
from tkinter import *
import time
# from tkinter.ttk import *

#definicja odpowiada za odliczanie 5 sekund
def rozpoczęcie_odliczania():
    time.sleep(1)
    print("START")
    time.sleep(5)
    print("STOP")

#definicja odpowiada za zliczanie ilości kliknięć i w zależności od ilości wybór dyscypliny
liczba = 0
def kliknięcia(): # without event because I use `command=` instead of `bind`
    global liczba
    liczba = liczba + 1
    if liczba<=10:
        dyscyplina="Jesteś powolny i dokładny, Twoja dyscyplina to praca w stajni"
    elif liczba>=20:
        dyscyplina="Jesteś bardzo szybki, Twoja dyscyplina to wyścigi konne"
    else:
        dyscyplina="Jesteś opanowany i spokojny, Twoja dyscyplina to joga na koniach"
    label1.configure(text=f'STOP! Liczba kliknięć: {liczba} {dyscyplina}')


windows = Tk()
windows.title("Wybór dyscypliny")
windows.geometry("600x500")
label = Label(windows, text="To najwyższy czas na zapisanie się na zajęcia wychowania fizycznego. Do wyboru masz trzy dyscypliny:"
"\n"
"\n a) praca w stajni"
"\n b) wyścigi konne"
"\n c) joga na koniach"
"\n"
"\n Sprawdźmy do czego się nadajesz."
"\n Kiedy będziesz gotowy naciśnij \"START\""
"\n A następnie wciskaj klawisz \"Naćiśnij\" tak dużo razy jak potrafisz aż do momentu pojawienia STOP.")

label.grid(column=0, row=0)
label1 = Label(windows, text = "_____________________________")
label1.grid(column=0, row=6)
custom_button = Button(windows, text="Naciśnij", command=kliknięcia)
custom_button.grid(column=0, row=5)
przycisk_startu=Button(windows, text="START", command=rozpoczęcie_odliczania)
przycisk_startu.grid(column=0, row=3)

windows.mainloop()

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
okno_test = Tk()
okno_test.title("Testuje przyciski")
okno_test.geometry("800x300")

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

tekst = Label(okno_test, text = "Jest ranek, budzisz się 10 min przed zajęciami."
"\n Możesz iść na uczelnie w piżamie (w ten sposób się nie spóźnisz),"
"\n albo ubrać się i spóźnić 5 min."
"Co wybierasz?", font = ("Arial Bold", 13))
tekst.place(x = 200,y = 50)

#RZECZY POTZREBNE I KONIECZNE :P

#Do notatek/ sprawdzenia czy wszystko działa i uzasadnień przyjaciół
reakcje = Label(okno_test, text = "")
reakcje.place(x = 250,y = 200)

#Przycisk_3 jest aktywowany w odpowiednich miejscach w funkcajch wyborów + po wyborze przyjaciół będzie usunięty
przycisk_1 = Button(okno_test, text = "Wolę się ubrać!", bg = "yellow", command = wybor_1)
przycisk_1.place(x = 150,y =  150)

przycisk_2 = Button(okno_test, text = "Pójdę w piżamie.", bg = "yellow", command = wybor_2)
przycisk_2.place(x = 350,y =  150)

przycisk_3 = Button(okno_test, text = "                                          ", bg = "yellow", command = wybor_3)
przycisk_3.place(x = 600,y =  150)
przycisk_3.configure(state = "disabled", bg = "grey")

# def powitanie():
#     messagebox.showinfo("Powitanie","Witaj! Jesteś studentem I roku Koniowistyki na Uniwerystecie Juliusza Słowackiego.")
#     messagebox.showinfo("Rada na początek nauki","Okres studiów to najlepszy czas w Twoim życiu. Pamiętaj, żeby go nie zmarnować...")

plotno=Canvas(okno_test, width=400, height=400)
plotno.pack()
obraz=Image.open("1.Uniwersytet.jpg")
obraz=obraz.resize((400,400))
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200,image=obrazTk)
przycisk1=Button(okno_test, text="Powitanie",command=powitanie)
przycisk1.pack()



okno_test.mainloop()
