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
        obraz= PhotoImage(file='1.Uniwersytet.png',width=600,height=500)
        self.label = ttk.Label(self.parent)
        self.label['image'] = obraz
        obraz.image = obraz
        self.label.pack()

        self.pole_tekstowe=Label(self.parent, text="Witaj! Jesteś studentem I roku Koniowistyki na Uniwersytecie Juliusza Słowackiego.",background='white')
        self.pole_tekstowe.place(x=180, y=400)

        self.przycisk_1=Button(self.parent, command=self.obraz2, text='Okres studiów to najlepszy czas w Twoim życiu. Pamiętaj, żeby go nie zmarnować...', bg='yellow')
        # self.przycisk_1.place(x=0,y=0)
        self.przycisk_1.pack()

    def obraz1(self):
        obraz1=PhotoImage(file='1.Uniwersytet.png',width=600,height=500)
        self.label['image']=obraz1
        obraz1.image=obraz1

        self.pole_tekstowe.configure(text="To znowu Ty... A więc po raz kolejny witamy..") #tutaj będą wracać jeśli będą chcieli zacząć
        self.przycisk_1.configure(text="Masz kolejną szansę. Tym razem postaraj się trochę bardziej.\n Powodzenia",command=self.obraz2)  # jeszcze raz jakby co Asia, więc mozesz im tu jakąś gadkę strzelić
        self.przycisk_2.destroy()

    def obraz2(self):
        obraz2=PhotoImage(file='2.Pokój w akademiku.png',width=600,height=500)
        self.label['image']=obraz2
        obraz2.image=obraz2

        self.pole_tekstowe.configure(text="Jest ranek. Budzisz się w swoim pokoju w akademiku")
        self.przycisk_1.configure(text="Sprawdź, która godzina",command=self.obraz3)


    def obraz3(self):
        obraz3=PhotoImage(file='3.Zegar.png',width=600,height=500)
        self.label['image']=obraz3
        obraz3.image=obraz3

        self.pole_tekstowe.configure(text="Masz 10 min do zajęć. \n Możesz iść na uczelnie w piżamie (w ten sposób się nie spóźnisz), \n albo ubrać się i spóźnić 5 min. Co wybierasz?")
        self.przycisk_1.configure(text="Wolę się ubrać! \n 5 min spóźnienia chyba mi nie zaszkodzi",command=self.obraz4)

        self.przycisk_2 = Button(self.parent, text = "Nie chcę się spóźnić pierwszego dnia, \n więc pójdę w piżamie ", bg = "yellow", command=self.obraz5)
        # self.przycisk_2.place(x=0,y=0)
        self.przycisk_2.configure(state='normal')
        self.przycisk_2.pack()

    def obraz4(self):
        obraz4=PhotoImage(file='4.2-Spóźnienie.png',width=600,height=500)
        self.label['image']=obraz4
        obraz4.image=obraz4

        self.pole_tekstowe.configure(text="Wchodząc do sali zatrzymuje Cię oburzony wykładowca.\n \"Na moje zajęcia nikt się nie spóźnia!\" - mówi -\n \"Czy Ty wiesz na jakim Uniwersytecie studiujesz?\n Na Uniwersytecie Juliusza Słowackiego! \nProszę mi w takim razie wyrecytować jego utwór.\"")
        self.przycisk_1.configure(text="Wybierz utwór do recytacji",command=self.obraz6)
        self.przycisk_2.configure(text="              ", state='disabled', bg = "grey")

    def obraz5(self):
        obraz5=PhotoImage(file='4.1-Piżama.png')
        self.label['image']=obraz5
        obraz5.image=obraz5

        self.pole_tekstowe.configure(text="Wchodząc do sali zatrzymuje Cię oburzony wykładowca.\n \"Czy Ty sobie kpisz z moich zajęć?\" -mówi -\n \"Jak bezczelnym trzeba być, żeby przyjść tak ubranym?\"")
        self.przycisk_1.configure(text="Odpowiedz", command = self.obraz9)
        self.przycisk_2.configure(text="                                    ", state='disabled', bg = "grey")

    def obraz6(self):
        obraz6=PhotoImage(file="5.Recytacja Słowackiego.png")
        self.label['image']=obraz6
        obraz6.image=obraz6

        self.pole_tekstowe.configure(text="Wybierz utwór Słowackiego. \nTylko się nie pomyl, bo możesz stać się pośmiewiskiem....")
        self.przycisk_1.configure(text="Oda do młodości",command=self.obraz8)
        self.przycisk_2.configure(text="Oda do wolności",state='normal',bg="yellow",command=self.obraz7)

    def obraz7(self):
        obraz7=PhotoImage(file="6.1.Recytacja-Słowacki.png",width=600,height=500)
        self.label['image']=obraz7
        obraz7.image=obraz7

        self.pole_tekstowe.configure(text="\"No przynajmniej masz jakąś wiedzę. Siadaj\" - wzdycha wykładowca")
        self.przycisk_1.configure(text="Następny krok", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz8(self):
        obraz8=PhotoImage(file="6.2.Recytacja-Mickiewicz.png", width=600,height=500)
        self.label['image']=obraz8
        obraz8.image=obraz8

        self.pole_tekstowe.configure(text="To jakaś kpina! Nawet nie wiesz co napisał nasz patron?!\nKażdy wie, że \"Odę do młodości\" napisał Mieckiwcz...\n Mam nadzieję, że to ostatni raz! Powodzenia przy poznawaniu ludzi niedouczony człowieku")
        self.przycisk_1.configure(text="Następny krok", command = self.obraz40)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz9(self):
        obraz9=PhotoImage(file="7.Profesor.png",width=600,height=500)
        self.label['image']=obraz9
        obraz9.image=obraz9

        self.pole_tekstowe.configure(text="Wchodząc do sali zatrzymuje Cię oburzony wykładowca.\n \"Czy Ty sobie kpisz z moich zajęć?\" -mówi -\n \"Jak bezczelnym trzeba być, żeby przyjść tak ubranym?\"")
        self.przycisk_1.configure(text="Przepraszam Profesorze", command = self.obraz11)
        self.przycisk_2.configure(text="Będę się ubierać jak chce \n i nic nikomu do tego!", command = self.obraz10, state="normal", bg="yellow")

    def obraz10(self):
        obraz10= PhotoImage(file="8.1.Odpyskowanie.png",width=600,height=500)
        self.label['image']=obraz10
        obraz10.image=obraz10

        self.pole_tekstowe.configure(text="Oj... Chyba wkurzyłeś profesora...\n Powodzenia przy znajdowaniu przyjaciół..")
        self.przycisk_1.configure(text="Następny krok", command = self.obraz41)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz11(self):
        obraz11=PhotoImage(file="8.2.Przeproszenie.png",width=600,height=500)
        self.label['image']=obraz11
        obraz11.image=obraz11

        self.pole_tekstowe.configure(text="Masz szczęście...\n Może znajdziesz jakiegoś przyjaciela...")
        self.przycisk_1.configure(text="Następny krok", command = self.obraz12)
        self.przycisk_2.configure(text="                              ", state="disabled",bg="grey")

    def obraz12(self): #PODWÓJNE - DOBRE MIEJSCE NA ZACZĘCIE WYBORU PRZYJACIELA
        obraz12=PhotoImage(file="8.Przyjaciele_wybor.png",width=600,height=500)
        self.label['image']=obraz12
        obraz12.image=obraz12

        self.pole_tekstowe.configure(text="Do następnego wykładu zostało kilka minut. \n To dobry czas, aby poznać kogoś nowego. \n Wybierz z kim chcesz nawiązać kontakt!")
        self.przycisk_1.configure(text="Alternatywka", command = self.obraz13)
        self.przycisk_2.configure(text="Koniara", command = self.obraz14, state="normal",bg="yellow")

        self.przycisk_3= Button(self.parent, text = "Dżokej", bg = "yellow",command=self.obraz15)
        # self.przycisk_3.place(x = 600,y =  150)
        self.przycisk_3.pack()

    def obraz40(self):
        obraz40=PhotoImage(file="8.Przyjaciele_wybor.png",width=600,height=500)
        self.label['image']=obraz40
        obraz40.image=obraz40

        self.pole_tekstowe.configure(text="Do następnego wykładu zosrało kilka minut.\n To dobry czas, aby poznać kogoś nowego! \nNo chyba, że wyrecytowałeś Mickiewicza...to cud jeśli kogokolwiek znajdziesz..\nZdaje się, że tylko dżokej był wyrozumiały")
        self.przycisk_1.configure(text="Alternatywka", state="disabled")
        self.przycisk_2.configure(text="Koniara", state="disabled",bg="yellow")

        self.przycisk_3= Button(self.parent, text = "Dżokej", bg = "yellow",command=self.obraz15)
        # self.przycisk_3.place(x = 600,y =  150)
        self.przycisk_3.pack()

    def obraz41(self):
        obraz41=PhotoImage(file="8.Przyjaciele_wybor.png",width=600,height=500)
        self.label['image']=obraz41
        obraz41.image=obraz41

        self.pole_tekstowe.configure(text="Do następnego wykładu zostało kilka minut. \n To dobry czas, aby poznać kogoś nowego. \n Jednak alternatywce nie spodobało się jak odpyskowałeś profesorowi..\nZ jej strony nie licz na przyjaźń")
        self.przycisk_1.configure(text="Alternatywka", state='disabled')
        self.przycisk_2.configure(text="Koniara", command = self.obraz14, state="normal",bg="yellow")

        self.przycisk_3= Button(self.parent, text = "Dżokej", bg = "yellow",command=self.obraz15)
        self.przycisk_3.pack()


    def obraz13(self):
        obraz13=PhotoImage(file="9.1.Alternatywka.png",width=600,height=500)
        self.label['image']=obraz13
        obraz13.image=obraz13

        self.pole_tekstowe.configure(text="Alternatywka zostaje Twoim przyjacielem!")
        self.przycisk_1.configure(text="To najwyższy czas, żeby zapisać się na wf :)", command = self.obraz16)
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz14(self):
        obraz14=PhotoImage(file="9.2.Koniara.png",width=600,height=500)
        self.label['image']=obraz14
        obraz14.image=obraz14

        self.pole_tekstowe.configure(text="Koniara zostaje Twoim przyjacielem!")
        self.przycisk_1.configure(text="To najwyższy czas, żeby zapisać się na wf :)", command = self.obraz16,state='normal')
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz15(self):
        obraz15=PhotoImage(file="9.3.Dżokej.png",width=600,height=500)
        self.label['image']=obraz15
        obraz15.image=obraz15

        self.pole_tekstowe.configure(text="Dżokej zostaje Twoim przyjacielem!")
        self.przycisk_1.configure(text="To najwyższy czas, żeby zapisać się na wf :)", command = self.obraz16,state='normal')
        self.przycisk_2.configure(text="                 ", state="disabled", bg="grey")
        self.przycisk_3.destroy()

    def obraz16(self):  ## WF - na razie od razu idzie do piwa, jak wstawimy minigrę usuniemy/zmienimy przcisk 3
        obraz16=PhotoImage(file="10W-F.png",width=600,height=500)
        self.label['image']=obraz16
        obraz16.image=obraz16

        self.pole_tekstowe.configure(text="Zapisz się na w-f")
        self.przycisk_1.configure(text="Joga na koniach",command=self.obraz18)
        self.przycisk_2.configure(text="Wyścigi konne", state="normal", bg="yellow",command=self.obraz19)

        self.przycisk_3 = Button(self.parent, text = "Praca w stajni", bg = "yellow",state='normal',command=self.obraz17)
        self.przycisk_3.place(x=150,y=400)
        self.przycisk_3.pack()

    def obraz17(self):
        obraz17=PhotoImage(file="11.1.Praca_w_stajni.png",width=600,height=500)
        self.label['image']=obraz17
        obraz17.image=obraz17

        self.pole_tekstowe.configure(text="Gratulacje! Udało Ci się zapisać na pracę w stajni.\n Za chwilę masz wykład z profesorem Czereśniowskim, \n ale przyjaciel zaprasza Cię na piwo. Co wybierasz?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz18(self):
        obraz18=PhotoImage(file="11.3.Joga na koniach.png",width=600,height=500)
        self.label['image']=obraz18
        obraz18.image=obraz18

        self.pole_tekstowe.configure(text="Gratulacje! Udało Ci się zapisać na jogę na koniach.\n  Za chwilę masz wykład z profesorem Czereśniowskim,\n ale przyjaciel zaprasza Cię na piwo. Co wybierasz?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz19(self):
        obraz19=PhotoImage(file="11.2.Wyścigi konne.png",width=600,height=500)
        self.label['image']=obraz19
        obraz19.image=obraz19

        self.pole_tekstowe.configure(text="Gratulacje! Udało Ci się zapisać na wyścigi konne.\n Za chwilę masz wykład z profesorem Czereśniowskim,\n ale przyjaciel zaprasza Cię na piwo. Co wybierasz?")
        self.przycisk_1.configure(text="Piwo", command=self.obraz20)
        self.przycisk_2.configure(text="wykład", bg="yellow", command=self.obraz21)
        self.przycisk_3.destroy()

    def obraz20(self):
        obraz20=PhotoImage(file="12.Piwo.png",width=600,height=500)
        self.label['image']=obraz20
        obraz20.image=obraz20

        self.pole_tekstowe.configure(text="Po wypiciu piwa Twój przyjaciel proponuje kolejne.\n Wypijesz je czy wrócisz na wykład?")
        self.przycisk_1.configure(text="piwo", command=self.obraz42)
        self.przycisk_2.configure(text="wykład", command=self.obraz21)

    def obraz42(self):
        obraz42=PhotoImage(file="12.Piwo.png",width=600,height=500)
        self.label['image']=obraz42
        obraz42.image=obraz42

        self.pole_tekstowe.configure(text="Serio? Znowu...\nTo teraz już chyba czas na wykład... a może jedak jeszcze jedno?")
        self.przycisk_1.configure(text="piwo", command=self.obraz43)
        self.przycisk_2.configure(text="wykład", command=self.obraz21)

    def obraz43(self):
        obraz43=PhotoImage(file="12.Piwo.png",width=600,height=500)
        self.label['image']=obraz43
        obraz43.image=obraz43

        self.pole_tekstowe.configure(text=" Nie masz już dosyć?!\nTo teraz czas na wykład... no chyba, że masz mocną głowę..?")
        self.przycisk_1.configure(text="piwo", command=self.obraz44)
        self.przycisk_2.configure(text="wykład", command=self.obraz21)

    def obraz44(self):
        obraz44=PhotoImage(file="12.Piwo.png",width=600,height=500)
        self.label['image']=obraz44
        obraz44.image=obraz44

        self.pole_tekstowe.configure(text="4 piwa! Dobry jesteś\n To teraz już chyba wrócisz na wykłąd?\n A może jedak jeszcze jedno piwo?")
        self.przycisk_1.configure(text="piwo", command=self.obraz45)
        self.przycisk_2.configure(text="wykład", command=self.obraz21)

    def obraz45(self):
        obraz45=PhotoImage(file="12.Piwo.png",width=600,height=500)
        self.label['image']=obraz45
        obraz45.image=obraz45

        self.pole_tekstowe.configure(text="Chyba już Ci wystarczy. Wracasz na wykład")
        self.przycisk_1.configure(text="wykład", command=self.obraz21)
        self.przycisk_2.configure(text="",state="disabled",bg='grey')

    def obraz21(self):
        obraz21=PhotoImage(file="12.Wykład.png",width=600,height=500)
        self.label['image']=obraz21
        obraz21.image=obraz21

        self.pole_tekstowe.configure(text="Jesteś na wykładzie. Zajmij miejsce")
        self.przycisk_1.configure(text="Przód", command=self.obraz22)
        self.przycisk_2.configure(text="Tył", command=self.obraz22,state='normal',bg='yellow')

    def obraz22(self):
        obraz22=PhotoImage(file="13.1.Zepsuty_rzutnik.png",width=600,height=500)
        self.label['image']=obraz22
        obraz22.image=obraz22

        self.pole_tekstowe.configure(text="Podczas wykładu Profesor myśli, \n że projektor się zepsuł ale Ty wiesz co zrobić, by zaczął działać.\n Pomożesz mu?")
        self.przycisk_1.configure(text="Nie pomoe", command=self.obraz24)
        self.przycisk_2.configure(text="Pomogę", command=self.obraz23)

    def obraz23(self):
        obraz23=PhotoImage(file="14.1.Naprawiłeś_rzutnik.png",width=600,height=500)
        self.label['image']=obraz23
        obraz23.image=obraz23

        self.pole_tekstowe.configure(text="Super! <3")
        self.przycisk_1.configure(text="Koniec wykładu", command=self.obraz25)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz24(self):
        obraz24=PhotoImage(file="14.Nie naprawiłeś rzutnika.png",width=600,height=500)
        self.label['image']=obraz24
        obraz24.image=obraz24

        self.pole_tekstowe.configure(text="Meh :c")
        self.przycisk_1.configure(text="Koniec wykładu", command=self.obraz25)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz25(self):
        obraz25=PhotoImage(file="15.1.Egzamin.png",width=600,height=500)
        self.label['image']=obraz25
        obraz25.image=obraz25

        self.pole_tekstowe.configure(text="Podejmowane przez Ciebie decyzje podczas semestru nie były łatwe, \n ale w końcu nadszedł czas egzaminów.")
        self.przycisk_1.configure(text="Zacznij pisać ", command=self.obraz46)
        self.przycisk_2.configure(text="                           ", state="disabled", bg="grey")

    def obraz46(self):
        obraz46=PhotoImage(file="15.1.Egzamin.png",width=600,height=500)
        self.label['image']=obraz46
        obraz46.image=obraz46

        self.pole_tekstowe.configure(text="Podejmowane przez Ciebie wybory sprawiły, \n że dziś nie jesteś dobrze przygotowany na egzamin \n i jeśli nie dopisze Ci szczęście to prawdopodobnie go oblejesz,\n jednak masz szansę ściągnąć. Co wybierzesz?")
        self.przycisk_1.configure(text="Ściągam!",bg='yellow',command=self.obraz26)
        self.przycisk_2.configure(text="Nie ściągam! Jakoś dam radę...",bg="yellow",command=self.obraz27,state='normal')

    def obraz26(self):
        obraz26=PhotoImage(file="16.1.Przyłapany na ściąganiu.png",width=600,height=500)
        self.label['image']=obraz26
        obraz26.image=obraz26

        self.pole_tekstowe.configure(text="Niestety szczęście Ci nie dopisało i wykładowca zauważył, \n że siągasz. Idzie w twoją stronę profesor...")
        self.przycisk_1.configure(text="Przyznam się!", command=self.obraz31)
        self.przycisk_2.configure(text="Ucieknę... może zapomni", command=self.obraz31)
        self.przycisk_3.destroy()

    def obraz27(self):
        obraz27=PhotoImage(file="17.1.Zdałeś.png",width=600,height=500)
        self.label['image']=obraz27
        obraz27.image=obraz27

        self.pole_tekstowe.configure(text="Udaje Ci się zdać!\n Wybierz swojego nowego prowadzącego od programowania.")
        self.przycisk_1.configure(text="Francuz!", command = self.obraz33)
        self.przycisk_2.configure(text="Dżokej Instruktor!", command= self.obraz34)
        self.przycisk_3.destroy()

    def obraz28(self):
        obraz28=PhotoImage(file="17.2.Oblałeś.png",width=600,height=500)
        self.label['image']=obraz28
        obraz28.image=obraz28

        self.pole_tekstowe.configure(text="")
        self.przycisk_1.configure(text="Niestety nie zdajesz. Musisz zacząć studia od nowa :c",command = self.obraz29)
        self.przycisk_2.configure(text="Zacznę jeszcze raz", command = self.obraz1)
        self.przycisk_3.destroy()

    def obraz31(self):
        obraz31=PhotoImage(file="17.7.Wylatujesz.png",width=600,height=500)
        self.label['image']=obraz31
        obraz31.image=obraz31

        self.pole_tekstowe.configure(text="Zostałeś przyłapany na śiąganiu! Profesor wyprasza Cię z sali")
        self.przycisk_1.configure(text="Żegnaj przyjacielu :c",command = self.autorzy)
        self.przycisk_2.destroy()

    # def obraz32(self):
    #     obraz32=PhotoImage(file="18.Poprawka.png",width=600,height=500)
    #     self.label['image']=obraz32
    #     obraz32.image=obraz32
    #
    #     self.pole_tekstowe.configure(text="")
    #     self.przycisk_1.configure(text="")
    #     self.przycisk_2.configure(text="")

    def obraz33(self):
        obraz33=PhotoImage(file="21.1.Francuz.png",width=600,height=500)
        self.label['image']=obraz33
        obraz33.image=obraz33

        self.pole_tekstowe.configure(text="Oto twój wybór! Francuz :) ")
        self.przycisk_1.configure(text="Idę na zajęcia! ", command = self.obraz35)
        self.przycisk_2.configure(text="                           ", state="disabled",bg="grey")

    def obraz34(self):
        obraz34=PhotoImage(file="21.Dżokej Instruktor.png",width=600,height=500)
        self.label['image']=obraz34
        obraz34.image=obraz34

        self.pole_tekstowe.configure(text="Oto twój wybór! Dżokej instruktor!")
        self.przycisk_1.configure(text="Idę na zajęcia! ", command = self.obraz35)
        self.przycisk_2.configure(text="                           ", state="disabled",bg="grey")

    def obraz35(self):
        obraz35=PhotoImage(file="22.1.DylematMoralny.png",width=600,height=500)
        self.label['image']=obraz35
        obraz35.image=obraz35

        self.pole_tekstowe.configure(text="Od dzisiaj już nic nie będzie takie samo... \n (UWAGA: Twrócy gry nie biorą na siebie odpowiedzialności \n za ewentualne szkody psychiczne.)")
        self.przycisk_1.configure(text="Jestem gotowy!",command=self.obraz36)
        self.przycisk_2.configure(text="Nie jestem gotowy...", state="normal",bg="yellow",command=self.obraz36)

    def obraz36(self):
        obraz36=PhotoImage(file="22.2.DylematMoralny.png",width=600,height=500)
        self.label['image']=obraz36
        obraz36.image=obraz36

        self.pole_tekstowe.configure(text="Na pewno?")
        self.przycisk_1.configure(text="Tak! Jestem gotowy!",command=self.obraz37)
        self.przycisk_2.configure(text="Zabierzcie mnie stąd... :(", state="normal",bg="yellow",command=self.obraz37)

    def obraz37(self):
        obraz37=PhotoImage(file="22.ProblemWagonika.png",width=600,height=500)
        self.label['image']=obraz37
        obraz37.image=obraz37

        self.pole_tekstowe.configure(text="Pociąg jedzie z pełną prędkością.\n  Na jego trasie do torów przywiązanych jest 5 osób.\n  Możesz zmienić trasę pociągu, jednak wtedy rozbije się on o skałę,\n a w raz z nim jedyna osoba będąca w środku - Twój przyjaciel.\n Co wybierasz?") #tutaj Asia proszę wstaw na opis na czym to polega :)
        self.przycisk_1.configure(text="Nie zmieniam trasy. \n Pociąg zabija 5 osób, ale mój przyjaciel przeżyje.",command=self.obraz38)
        self.przycisk_2.configure(text="Zmieniam trasę i uśmiercam przyjaciela, \n lecz ratuję 5 obcych osób.",command=self.obraz38, state="normal",bg="yellow")

    def obraz38(self):
        obraz38=PhotoImage(file="23.W twoich rękach.png",width=600,height=500)
        self.label['image']=obraz38
        obraz38.image=obraz38

        self.pole_tekstowe.configure(text="Teraz wszystko jest w Twoich rękach...\n “Nie ma odwagi bez dylematu lub charakteru,\n który nie jest ukształtowany przez wybory bardziej niż przez zwycięstwa”.\n -Muriel Barbery")
        self.przycisk_1.configure(text="Napisy końcowe", command = self.autorzy)
        self.przycisk_2.destroy()

    def autorzy(self):
        self.pole_tekstowe.configure(text="KONIOWISTYKA \n \n Joanna Depta \n Alicja Raczunas\n Zosia Trafas \n Weronika Wojtas ") #tu wszystkie dane wiadomo
        self.przycisk_1.configure(text="Wyjdź z gry",command=self.wyjscie)
        self.przycisk_2.destroy()

    def wyjscie(self):
        self.parent.quit()

def main():
    okno_gry= Tk()
    okno_gry.geometry('800x600')
    Picture(okno_gry)
    okno_gry.mainloop()

main()

#####################################################
