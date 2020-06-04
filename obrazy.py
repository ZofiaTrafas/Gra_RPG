from tkinter import *
from tkinter import ttk
import time

class Picture:
    global pole_tekstowe
    global przycisk_1
    global przycisk_2
    global przycisk_3
    def __init__(self, parent):
        self.parent = parent
        obraz1= PhotoImage(file='1.Uniwersytet.png',width=600,height=500)
        self.label = ttk.Label(self.parent)
        self.label['image'] = obraz1
        obraz1.image = obraz1
        self.label.pack()

        self.pole_tekstowe=Label(self.parent, text="Witaj na uniwersytecie! Studia to czas wyborów bla bla bla",background='white')
        self.pole_tekstowe.place(x=280, y=400)

        self.przycisk_1=Button(self.parent, command=self.obraz2, text='Witaj na uniwerku! Studia to czas wyborów', bg='yellow')
        # self.przycisk_1.place(x=0,y=0)
        self.przycisk_1.pack()


    def obraz2(self):
        obraz2=PhotoImage(file='2.Pokój w akademiku.png',width=600,height=500)
        self.label['image']=obraz2
        obraz2.image=obraz2

        self.pole_tekstowe.configure(text="Budzisz się w swoim pokoju w akademiku")
        self.przycisk_1.configure(text="Sprawdź, która godzina",command=self.obraz3)


    def obraz3(self):
        obraz3=PhotoImage(file='3.Zegar.png',width=600,height=500)
        self.label['image']=obraz3
        obraz3.image=obraz3

        self.pole_tekstowe.configure(text="O nie! Za 5 minut zaczynasz zajęcia!\nJak pójdziesz w piżamie to zdążysz.\nJak zdecydujesz się ubrać to się spóźnisz.\nCo robisz?")
        self.przycisk_1.configure(text="Spóźnienie",command=self.obraz4)
        
        self.przycisk_2 = Button(self.parent, text = "   Piżama   ", bg = "yellow", command=self.obraz5)
        # self.przycisk_2.place(x=0,y=0)
        self.przycisk_2.configure(state='disabled')
        self.przycisk_2.pack()

    def obraz4(self):
        obraz4=PhotoImage(file='4.2-Spóźnienie.png',width=600,height=500)
        self.label['image']=obraz4
        obraz4.image=obraz4

        self.pole_tekstowe.configure(text="Spózniasz się! Profesor jest zły. Sprawdź jakie ma dla cb zadanie")
        self.przycisk_1.configure(text="Zadanie",command=self.obraz6)
        self.przycisk_2.configure(text="              ", state='disabled', bg = "grey")

    def obraz5(self):
        obraz5=PhotoImage(file='4.1-Piżama.png')
        self.label['image']=obraz5
        obra5.image=obraz5
        
        self.pole_tekstowe.configure(text="Uadło ci się zdążyć na zajęcia! Profesor coś do ciebie mówi")
        self.przycisk_1.configure(text="Posłuchaj Profesora ", command = self.obraz9)
        self.przycisk_2.configure(text="                                    ", state='disabled', bg = "grey")

    def obraz6(self):
        obraz6=PhotoImage(file="5.Recytacja Słowackiego.png")
        self.label['image']=obraz6
        obraz6.image=obraz6

        self.pole_tekstowe.configure(text="Masz wyrecytować Słowackiego!\nMasz do wyboru 2 dzieła!\nTylko się nie pomyl, bo możesz stać się pośmiewiskiem....")
        self.przycisk_1.configure(text="Oda do młodości",command=self.obraz8)
        self.przycisk_2.configure(text="Oda do wolności",state='normal',bg="yellow",command=self.obraz7)

    def obraz7(self):
        obraz7=PhotoImage(file="6.1.Recytacja-Słowacki.png",width=600,height=500)
        self.label['image']=obraz7
        obraz7.image=obraz7

        self.pole_tekstowe.configure(text="Masz szczęście... Przynajmniej znasz swojego patrona.\nKoniec zajęć - idźcie się zapoznać")
        self.przycisk_1.configure(text="Idź poznać ludzi", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz8(self):
        obraz8=PhotoImage(file="6.2.Recytacja-Mickiewicz.png", width=600,height=500)
        self.label['image']=obraz8
        obraz8.image=obraz8

        self.pole_tekstowe.configure(text="To jakaś kpina! Nawet nie wiesz co napisał nasz patron?!\nKażdy wie, że \"Odę do młodości\" napisał Mieckiwcz...\nPowodzenia przy poznawaniu ludzi niedouczony człowieku")
        self.przycisk_1.configure(text="Idź poznać ludzi", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz9(self):
        obraz9=PhotoImage(file="7.Profesor.png")
        self.label['image']=obraz9
        obraz9.image=obraz9
        
        self.pole_tekstowe.configure(text="Profesorowi nie podoba się, że przyszedłes na zajęcia w piżamie...")
        self.przycisk_1.configure(text="Przeproś", command = self.obraz10)
        self.przycisk_2.configure(text="Odpyskuj", command = self.obraz11, state="normal", bg="yellow")

    def obraz10(self):
        obraz10= PhotoImage(file="8.1.Odpyskowanie.png",width=600,height=500)
        self.label['image']=obraz10
        obraz10.image=obraz10
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Idź poznać ludzi", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz11(self):
        obraz11=PhotoImage(file="8.2.Przeproszenie.png")
        self.label['image']=obraz11
        obraz11.image=obraz11
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Idź poznać ludzi", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz12(self): #PODWÓJNE - DOBRE MIEJSCE NA ZACZĘCIE WYBORU PRZYJACIELA
        obraz12=PhotoImage(file="8.2.Przeproszenie.png")
        self.label['image']=obraz12
        obraz12.image=obraz12
        
        self.pole_tekstowe.configure(text="Wybierz przyjaciela!")
        self.przycisk_1.configure(text="Alternatywka", command = self.obraz13)
        self.przycisk_2.configure(text="Koniara", command = self.obraz14, state="normal",bg="yellow")
        
        self.przycisk_3= Button(self.parent, text = "Dżokej", bg = "yellow")
        # self.przycisk_3.place(x = 600,y =  150)
        self.przycisk_3.pack()

    def obraz13(self):
        obraz13=PhotoImage(file="9.1.Alternatywka.png")
        self.label['image']=obraz13
        obraz13.image=obraz13
        
        self.pole_tekstowe.configure(text="Alternatywka zostaje twoim przyjacielem!")
        self.przycisk_1.configure(text="Co dalej?", command = self.obraz16)
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz14(self):
        obraz14=PhotoImage(file="9.2.Koniara.png")
        self.label['image']=obraz14
        obraz14.image=obraz14
        
        self.pole_tekstowe.configure(text="Koniara zostaje twoim przyjacielem!")
        self.przycisk_1.configure(text="Co dalej?", command = self.obraz16)
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz15(self):
        obraz15=PhotoImage(file="9.3.Dżokej.png")
        self.label['image']=obraz15
        obraz15.image=obraz15
        
        self.pole_tekstowe.configure(text="Dżokej zostaje twoim przyjacielem!")
        self.przycisk_1.configure(text="Co dalej?", command = self.obraz16)
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz16(self):  ## WF - na razie od razu idzie do piwa, jak wstawimy minigrę usuniemy/zmienimy przcisk 3
        obraz16=PhotoImage(file="10W-F.png")
        self.label['image']=obraz16
        obraz16.image=obraz16
        
        self.pole_tekstowe.configure(text="Minigra - wf wprowadzenie")
        self.przycisk_1.configure(text="START")
        self.przycisk_2.configure(text="Naciskaj!", state="normal", bg="green")

        self.przycisk_3 = Button(self.parent, text = "Dalej", bg = "yellow", command=self.obraz20)
        self.przycisk_3.place(x=150,y=400)
        self.przycisk_3.pack()

    def obraz17(self):
        obraz17=PhotoImage(file="11.1.Praca_w_stajni.png")
        self.label['image']=obraz17
        obraz17.image=obraz17
        
        self.pole_tekstowe.configure(text="Praca w stajni\nWybrałeś już wf czas iść na wykład... a może na piwo?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz18(self):
        obraz18=PhotoImage(file="11.2.Joga na koniach.png")
        self.label['image']=obraz18
        obraz18.image=obraz18
        
        self.pole_tekstowe.configure(text="Joga\nWybrałeś już wf czas iść na wykład... a może na piwo?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz19(self):
        obraz19=PhotoImage(file="11.2.Wyścigi konne.png")
        self.label['image']=obraz19
        obraz19.image=obraz19
        
        self.pole_tekstowe.configure(text="Wyścigi konne\nWybrałeś już wf czas iść na wykład... a może na piwo?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz20(self):
        obraz20=PhotoImage(file="12.Piwo.png")
        self.label['image']=obraz20
        obraz20.image=obraz20
        
        self.pole_tekstowe.configure(text="Poszedłeś na piwo! To teraz czas na wykład... a może jedak jeszcze jedno?")
        self.przycisk_1.configure(text="piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", command=self.obraz21)

    def obraz21(self):
        obraz21=PhotoImage(file="12.Wykład.png")
        self.label['image']=obraz21
        obraz21.image=obraz21
        
        self.pole_tekstowe.configure(text="witaj na wykładzie. Zajmij miejsce")
        self.przycisk_1.configure(text="Przód", command=self.obraz22)
        self.przycisk_2.configure(text="Tył", command=self.obraz22)

    def obraz22(self):
        obraz22=PhotoImage(file="13.1.Zepsuty_rzutnik.png")
        self.label['image']=obraz22
        obraz22.image=obraz22
        
        self.pole_tekstowe.configure(text="Profesorowi zepsuł się rzutnik.\nCo zrobić?")
        self.przycisk_1.configure(text="Zignoruj", command=self.obraz23)
        self.przycisk_2.configure(text="Napraw", command=self.obraz24)

    def obraz23(self):
        obraz23=PhotoImage(file="14.1.Naprawiłeś_rzutnik.png")
        self.label['image']=obraz23
        obraz23.image=obraz23
        
        self.pole_tekstowe.configure(text="Super uwu")
        self.przycisk_1.configure(text="koniec wykładu", command=self.obraz25)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz24(self):
        obraz24=PhotoImage(file="14.Nie naprawiłeś rzutnika.png")
        self.label['image']=obraz24
        obraz24.image=obraz24
        
        self.pole_tekstowe.configure(text="Meh")
        self.przycisk_1.configure(text="koniec wykładu", command=self.obraz25)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz25(self):
        obraz25=PhotoImage(file="15.1.Egzamin.png")
        self.label['image']=obraz25
        obraz25.image=obraz25
        
        self.pole_tekstowe.configure(text="Czas na egzamin")
        self.przycisk_1.configure(text="koniec wykładu", command=self.obraz25)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz26(self):
        obraz26=PhotoImage(file="16.1.Przyłapany na ściąganiu.png")
        self.label['image']=obraz26
        obraz26.image=obraz26
        
        self.pole_tekstowe.configure(text="O nie! Zostałeś przyłapany na ściąganiu. Idzie w twoją stronę profesor..")
        self.przycisk_1.configure(text="przyznaj się", command=self.obraz29)
        self.przycisk_2.configure(text="uciekaj", command=self.obraz29)

    def obraz27(self):
        obraz27=PhotoImage(file="17.1.Zdałeś.png")
        self.label['image']=obraz27
        obraz27.image=obraz27
        
        self.pole_tekstowe.configure(text="Zdałeś, wybierz prowadzących na następny semestr")
        self.przycisk_1.configure(text="Francuz", command = self.obraz33)
        self.przycisk_2.configure(text="Dżokej Instruktor", command= slef.obraz34)

    def obraz28(self):
        obraz28=PhotoImage(file="17.2.Oblałeś.png")
        self.label['image']=obraz28
        obraz28.image=obraz28
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Pa Pa",command = self.autorzy)
        self.przycisk_2.configure(text="Zacznij jeszcze raz", command = self.obraz1)

    def obraz29(self):
        obraz29=PhotoImage(file="17.5.Wylatujesz.png")
        self.label['image']=obraz29
        obraz29.image=obraz29
        
        self.pole_tekstowe.configure(text="Zostałeś przyłapany na ściąganiu")
        self.przycisk_1.configure(text="Pa Pa",command = self.autorzy)
        self.przycisk_2.destroy()

    def obraz30(self):
        obraz30=PhotoImage(file="17.6.Wylatujesz.png")
        self.label['image']=obraz30
        obraz30.image=obraz30
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Pa Pa",command = self.autorzy)
        self.przycisk_2.destroy()

    def obraz31(self):
        obraz31=PhotoImage(file="17.7.Wylatujesz.png")
        self.label['image']=obraz31
        obraz31.image=obraz31
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Pa Pa",command = self.autorzy)
        self.przycisk_2.destroy()

    def obraz32(self):
        obraz32=PhotoImage(file="18.Poprawka.png")
        self.label['image']=obraz32
        obraz32.image=obraz32
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="")
        self.przycisk_2.configure(text="")

    def obraz33(self):
        obraz33=PhotoImage(file="20.Francuz.png")
        self.label['image']=obraz33
        obraz33.image=obraz33
        
        self.pole_tekstowe.configure(text="Francuz")
        self.przycisk_1.configure(text="Idę na zajęcia!", command = slef.obrazek38)
        self.przycisk_2.configure(text="                           ", state="disabled",bg="grey")

    def obraz34(self):
        obraz34=PhotoImage(file="21.Dżokej Instruktor.png")
        self.label['image']=obraz34
        obraz34.image=obraz34
        
        elf.pole_tekstowe.configure(text="Dżokej instruktor")
        self.przycisk_1.configure(text="Idę na zajęcia!", command = slef.obrazek38)
        self.przycisk_2.configure(text="                           ", state="disabled",bg="grey")        
        
    def obraz35(self):
        obraz35=PhotoImage(file="22.1.DylematMoralny.png")
        self.label['image']=obraz35
        obraz35.image=obraz35
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="")
        self.przycisk_2.configure(text="", state="normal",bg="yellow")

    def obraz36(self):
        obraz36=PhotoImage(file="22.2.DylematMoralny.png")
        self.label['image']=obraz36
        obraz36.image=obraz36
        
        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="")
        self.przycisk_2.configure(text="", state="normal",bg="yellow")

    def obraz37(self):
        obraz37=PhotoImage(file="22.ProblemWagonika.png")
        self.label['image']=obraz37
        obraz37.image=obraz37
        
        self.pole_tekstowe.configure(text="Problem wagonika")
        self.przycisk_1.configure(text="nic nie rób",command=self.obrazek38)
        self.przycisk_2.configure(text="przesuń dźwignię",command=self.obrazek38, state="normal",bg="yellow")

    def obraz38(self):
        obraz38=PhotoImage(file="23.W twoich rękach.png")
        self.label['image']=obraz38
        obraz38.image=obraz38
        
        self.pole_tekstowe.configure(text="Wszystko w twoich rękach...")
        self.przycisk_1.destroy()
        self.przycisk_2.configure(text="Napisy końcowe", command = self.autorzy)
        
    def autorzy(self):
        self.pole_tekstowe.configure(text="tytuł, autorzy, muzyka etc")
        self.przycisk_1.destroy()
        self.przycisk_2.configure(text="wyjdz", command=okno_gry.quit)

def main():
    okno_gry= Tk()
    okno_gry.geometry('800x600')
    Picture(okno_gry)
    okno_gry.mainloop()

main()
