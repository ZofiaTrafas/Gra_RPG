import random


print("Powitanie! Studia blablabla wybory")
#WYBOR SPOZNIENIE A PIZAMA
print("budzisz sie, spozniony na zajecia. Co robisz?\n1 - spozniasz sie na zajecia, 2 - idziesz na zajecia w pizamie")
wybor_spoznienie_pizama = int(input())
#WYBOR SPOZNIENIE A PIZAMA - SPOZNIENIE
if wybor_spoznienie_pizama == 1:
    #WYBOR MICKIEWICZ A SLOWACKI
    print("Spozniasz sie na zajecia. Prowadzacy za kare kaze ci wyrecytowac dzielo Slowackiego. Co recytujesz?\n 1 - oda do mlodosci, 2 - oda do wolnosci")
    wybor_mickiewicz_slowacki = int(input())
    #WYBOR MICKIEWICZ A SLOWACKI - MICKIEWICZ
    if wybor_mickiewicz_slowacki == 1:
        #ludzie nas nie lubia, wiec sympatia 1
        sympatia_ludzi = 1
    #WYBOR MICKIEWICZ A SLOWACKI - SLOWACKI
    elif wybor_mickiewicz_slowacki == 2:
        #Ludzie nas lubia, wiec sympatia 2
        sympatia_ludzi = 2
    else:
        print("Zostala wprowadzona zla komenda")
#WYBOR SPOZNIENIE A PIZAMA - PIZAMA
elif wybor_spoznienie_pizama == 2:
    #WYBOR ODPYSKUJ A PRZEPROS
    print("Profesorowi sie nie podoba, ze jestes w pizamie. Co wybierasz?\n1 - odpyskuj, 2 - przepros")
    wybor_odpyskuj_przepros = int(input())
    # WYBOR ODPYSKUJ A PRZEPROS - ODPYSKUJ
    if wybor_odpyskuj_przepros == 1:
        #ludzie nas nie lubia, wiec sympatia 3
        sympatia_ludzi = 3
    #WYBOR ODPYSKUJ A PRZEPROS - PRZEPROS
    elif wybor_odpyskuj_przepros == 2:
        #Ludzie nas lubia, wiec sympatia 4
        sympatia_ludzi = 4
else:
    print("Zostala wprowadzona zla komenda")

#Tutaj nasze dwie początkowe ścieżki się spotykają, więc kontynuujmy tutaj.




#ALTERNATYWKA A KONIARA A DZOKEJ
print("Poznajesz nowe osobki. Masz do wyboru:\n1 - alternatywke, 2 - koniare, 3 - dzokeja")
wybor_alternatywka_koniara_dzokej = int(input())
#sympatia ludzi 2 i 4 to wtedy, gdy nas polubili. 3 i 4, gdy nie

#funkcja ktora sluzy do sprawdzenia, dlaczego ktos cie polubil lub nie
def sprawdzenie_sympatii_ludzi():
    if sympatia_ludzi == 2:
        print("Bardzo docenila to, ze znales utwor Slowackiego na zajeciach")
    elif sympatia_ludzi == 4:
        print("Spodobalo jej sie, ze pomimo tego, ze przyszedles w pizamie, to potrafiles przeprosic")
    elif sympatia_ludzi == 1:
        print("Nie spodobalo sie jej, ze przez ciebie bedzie kartkowka z tworczosci Slowackiego")
    elif sympatia_ludzi == 3:
        print("Nie spodobalo sie jej, ze nie dosc, ze przyszedles w pizamie, to jeszcze odpyskowales prowadzacemu")

#jak ludzie cie polubili, to pierwszy wybor zostaje twoim przyjacielem (+ wyjasnienie dlaczego za pomoca funkcji)
if sympatia_ludzi == 2 or sympatia_ludzi == 4:
    if wybor_alternatywka_koniara_dzokej == 1:
        print("Twoim przyjacielem zostaje alternatywka!")
        wybor_przyjaciela = 1
        sprawdzenie_sympatii_ludzi()
    elif wybor_alternatywka_koniara_dzokej == 2:
        print("Twoim przyjacielem zostaje koniara!")
        wybor_przyjaciela = 2
        sprawdzenie_sympatii_ludzi()
    elif wybor_alternatywka_koniara_dzokej == 3:
        print("Twoim przyjacielem zostaje dzokej!")
        wybor_przyjaciela = 3
        sprawdzenie_sympatii_ludzi()
    else:
        print("Zostala wprowadzona zla komenda")

#jak ludzie cie nie polubili, to pierwszy wybor zostaje odrzucony (+ wyjasnienie dlaczego za pomoca funkcji), a pozniej wybor z pozostalych dwoch opcji
elif sympatia_ludzi == 1 or sympatia_ludzi == 3:
    if wybor_alternatywka_koniara_dzokej == 1:
        print("Alternatywka nie chce byc twoim przyjacielem!")
        sprawdzenie_sympatii_ludzi()
        print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n2 - koniara, 3 - dzokej")
        wybor_przyjaciela = int(input())
        if wybor_przyjaciela == 2:
            print("Twoim przyjacielem zostaje koniara!")
        elif wybor_przyjaciela == 3:
            print("Twoim przyjacielem zostaje dzokej!")
        else:
            print("Zostala wprowadzona zla komenda")
    elif wybor_alternatywka_koniara_dzokej == 2:
        print("Koniara nie chce byc twoim przyjacielem!")
        sprawdzenie_sympatii_ludzi()
        print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n1 - alternatywka, 3 - dzokej")
        wybor_przyjaciela = int(input())
        if wybor_przyjaciela == 1:
            print("Twoim przyjacielem zostaje alternatywka!")
        elif wybor_przyjaciela == 3:
            print("Twoim przyjacielem zostaje dzokej!")
        else:
            print("Zostala wprowadzona zla komenda")
    elif wybor_alternatywka_koniara_dzokej == 3:
        print("Dzokej nie chce byc twoim przyjacielem!")
        sprawdzenie_sympatii_ludzi()
        print("Musisz sprobowac zaprzyjaznic sie z inna osoba.\n1 - alternatywka, 2 - koniara")
        wybor_przyjaciela = int(input())
        if wybor_przyjaciela == 1:
            print("Twoim przyjacielem zostaje alternatywka!")
        elif wybor_przyjaciela == 2:
            print("Twoim przyjacielem zostaje koniara!")
        else:
            print("Zostala wprowadzona zla komenda")
    else:
        print("Zostala wprowadzona zla komenda")


#Znowu sciezki sie spotykaja, wiec kontynuujemy dalej

#WYBOR WF, ale moze zrobimy to za pomoca cookie clickera
print("Na jaki WF chcialbys uczeszczac?\n1 - praca w stajni, 2 - wyscigi konne, 3 - joga na koniach")
wybor_wf = int(input())
if wybor_wf == 1:
    print("Bedziesz pracowac w stajni")
elif wybor_wf == 2:
    print("Bedziesz bral udzial w wyscigach konnych")
elif wybor_wf == 3:
    print("Bedziesz bral udzial w jodze na koniach")


#WYBOR P I W E R K O  CZY WYKLAD
print("Chcesz isc na piwo, czy na wyklad?\n1 - piwo, 2 - wyklad")
wybor_piwo_wyklad = int(input())
#piwo to licznik ile razy byles na piwie
piwo = 0
if wybor_piwo_wyklad == 1:
    while piwo != 5:
        piwo += 1
        print("Poszedles na piwo. Chcesz isc na piwo czy wyklad?\n1 - piwo, 2 - wyklad")
        wybor_piwo_wyklad_2 = int(input())
        if wybor_piwo_wyklad_2 == 1:
            print("Ile mozna?")
        elif wybor_piwo_wyklad_2:
            print("Idziesz na wyklad")
            break
    if piwo == 5:
        print("Znajomi zaciagaja cie na wyklad, bo ile mozna pic")

elif wybor_piwo_wyklad == 2:
    print("Jako grzeczny student idziesz na wyklad")

else:
    print("Zostala wprowadzona zla komenda")
print("piwo", piwo)
#albo po piwie, albo bez piwa, ale docieramy na wyklad

#WYBOR NIE POMOC CZY TAK
print("Profesor ma problem z projektorem. Pomozesz mu?\n1 - nie, 2 - tak")
wybor_nie_pomoc = int(input())
if wybor_nie_pomoc == 1:
    print("No slabo")
elif wybor_nie_pomoc == 2:
    #jak pomozesz to pozniej fajne rzeczy sie dzieja, likwiduje to pierwszy zly wybor!
    print("Super uwu")
else:
    print("Zostala wprowadzona zla komenda")

#EGZAMIN! Jesli piles piwo to jestes nieprzygotowany, jesli  nie piles to ogarniasz


#dodaje to jako funkcje, zeby skrocic kod. jest to wybor czy chcesz sciagac czy nie plus czy chcesz miec poprawke czy nie

def poprawka_czy_chcesz():
    print("Czy chcesz poprawke?\n1 - tak, 2 - nie")
    poprawka = int(input())
    if poprawka == 1:
        #przechodzi do opcji z poprawka
        print("Bedziesz mial poprawke")
    elif poprawka == 2:
        #zakonczenie z makiem
        print("Praca w maku")
    else:
        print("Zostala wprowadzona zla komenda")
    return poprawka

def sciaganie():
    print("Co wybierasz?\n1 - sciagasz, 2 - nie sciagasz")
    wybor_sciagasz_nie = int(input())
    #WYBOR SCIAGANIE - SCIAGA
    if wybor_sciagasz_nie == 1:
        #zostaje przylapany
        print("Zostalesz przylapany na sciaganiu")
        return poprawka_czy_chcesz()
    #WYBOR SCIAGANIE - NIE SCIAGA
    elif wybor_sciagasz_nie == 2:
        #szansa na zdanie jest losowa
        szansa_na_zdanie = random.randint(1,prawdopodobienstwo_zdania)
        if 1 < szansa_na_zdanie < 5:
            print("Nie udało ci się zdać")
            return poprawka_czy_chcesz()
        else:
            print("")
    else:
        print("Zostala wprowadzona zla komenda")
    #nie chcesz poprawki, wiec jest ona rowna -1
    return -1





print("Nadeszla sesja. Masz egzamin.")

if piwo == 0:
    print("Brales udzial w wykladach, byles odpowiedzialny, zdajesz bez problemu")
    poprawka = -1
elif 3 >= piwo > 0:
    #jak jestes srednio nauczony, to masz gorsze szanse zdania
    print("Jestes srednio nauczony. Mozesz sciagac, narazajac sie na przylapanie, albo sprobowac napisac to samemu (masz male szanse zdanie).")
    prawdopodobienstwo_zdania = 10
    poprawka = sciaganie()

elif 5 >= piwo > 3:
    #jak tylko byles na piwie, to w ogole slabe szanse
    print("Jestes zle nauczony. Mozesz sciagac, narazajac sie na przylapanie, albo sprobowac napisac to samemu (masz BARDZO male szanse zdanie).")
    prawdopodobienstwo_zdania = 7
    poprawka = sciaganie()


#dodaje to jako funkcje, zeby skrocic kod. jest to wybor czy chcesz sprobowac ponownie czy nie
def sprobuj_ponownie():
    print("Chcesz sprobowac od nowa?\n1 - tak, 2 - nie")
    wybor_od_nowa = int(input())
    if wybor_od_nowa == 1:
        print("witamy ponownie")
        #start programu od nowa, tylko z nowymi dialogami
    elif wybor_od_nowa == 2:
        #zakonczenie z makiem
        print("Pracujesz w maku")
    else:
        print("Zostala wprowadzona zla komenda")

if poprawka == 1:
    #tutaj sprawdzamy poprzednie wybory. Jesli ktos tylko pil piwo, to zdaje. Jesli ktos oprocz piwa recytowal mickiewicza, albo pyskowal - nie zdaje, chyba ze pozniej pomogl profesorowi z projektorem.
    if wybor_mickiewicz_slowacki == 1 and wybor_nie_pomoc == 1:
        print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach recytowales mickiewicza zamiast slowackiego, przez co nie zdajesz przedmiotu z gwiazdka.")
        sprobuj_ponownie()
    elif wybor_mickiewicz_slowacki == 1 and wybor_nie_pomoc == 2:
        print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach recytowales mickiewicza zamiast slowackiego, ale przypomina sobie, ze jego kolega cie chwalil, ze pomogles mu z projektorem, wiec jest pozytywnie do ciebie nastawiony i zdajesz")
    elif wybor_spoznienie_pizama == 1 and wybor_nie_pomoc == 1:
        print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach przyszedles w pizamie i odpyskowales, przez co nie zdajesz przedmiotu z gwiazdka.")
        sprobuj_ponownie()
    elif wybor_spoznienie_pizama == 1 and wybor_nie_pomoc == 2:
        print("Profesor na poprawce przypomina sobie, ze na pierwszych zajeciach przyszedles w pizamie i odpyskowales,ale przypomina sobie, ze jego kolega cie chwalil, ze pomogles mu z projektorem, wiec jest pozytywnie do ciebie nastawiony i zdajesz")

#tutaj leci historia dla tych, ktorzy zdali

print("Gratulacje, zdales!")
if wybor_przyjaciela == 1:
    print("Ty i twoja przyjaciolka alternatywka pomyslnie zdajecie pierwszy semestr")
elif wybor_przyjaciela == 2:
    print("Ty i twoja przyjaciolka koniara pomyslnie zdajecie pierwszy semestr")
elif wybor_przyjaciela == 3:
    print("Ty i twoj przyjaciel dzokej pomyslnie zdajecie pierwszy semestr")

if wybor_wf == 1:
    print("a ty odnosisz sukcesy pracujac w stajni w ramach WFu")
elif wybor_wf ==2:
    print("a ty odnosisz sukcesy w wyscigach konnych w ramach WFu")
elif wybor_wf == 3:
    print("a ty jestes zrelaksowany po calym semestrze jogi na koniach")


#D R U G I    S E M E S T R
