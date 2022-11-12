from domain.pachet import creeaza_pachet, get_destinatie, get_id, durata, get_pret, get_data_inceput, get_data_sfarsit
from infrastructura.repository_pachete import adauga_pachet_lista, nr_pachete_lista, get_lista_pachete, \
    modifica_pachet_lista, sterge_pachet_lista
from validare.validator_pachet import valideaza_pachet


def adauga_pachet_service(lst, id, data_inceput, data_sfarsit, destinatie, pret):
    """
    creeaza un pachet pe baza id, data_inceput, data_sfarsit, destinatie, pret
    incearca sa il valideze si daca e valid incearca sa il adauge in lista de pachete lst
    :param lst: lista de pachete
    :param id: int
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: float
    :return:
    :raises: ValueError daca id-ul e < 0, "id invalid!\n" va fi concatenat la stringul de erori,
    daca destinatia este vida, "destinatie vida!\n" va fi concatenat la stringul de erori,
    daca pretul e <= 0.0, "pret invalid!\n" va fi concatenat la stringul de erori
    daca cel putin un mesaj e concatenat la str de erori se va arunca ValueError cu mesajul/mesajele respective
    :raises: ValueError cu mesajul "pachet de calatorie invalid!\n" daca in lista exista deja un pachet du acelasi id
    """
    pachet = creeaza_pachet(id, data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet)
    adauga_pachet_lista(lst, pachet)


def modifica_pachet_service(lst, id, data_inceput, data_sfarsit, destinatie, pret):
    """
    creeaza un pachet pe baza id, data_inceput, data_sfarsit, destinatie, pret
    incearca sa il valideze si daca e valid incearca sa il modifice din lista de pachete lst cu pachetul cu acelasi id
    :param lst: lista de pachete
    :param id: int
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: float
    :return:
    :raises: ValueError cu mesajul "pachet de calatorie invalid!\n" daca in lista exista deja un pachet cu acelasi id
    """
    pachet = creeaza_pachet(id, data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet)
    modifica_pachet_lista(lst, pachet)


def sterge_pachet_service(lst, id):
    """
    sterge pachetul cu id-ul id din lista de pachete
    :param lst:  lista de pachete
    :param id: int
    :return:
    :raises: ValueError cu mesajul "id inexistent!\n" daca in lista nu exista un pachet cu id-ul dat
    """
    sterge_pachet_lista(lst, id)


def sterge_destinatie_service(lst, dest):
    """
    sterge din lista toate pachetele cu o destinatie data
    :param lst: lista de pachete
    :param dest: string
    :return:
    """
    for i in range(0, len(lst)):
        if get_destinatie(lst[i]) == dest:
            sterge_pachet_lista(lst, get_id(lst[i]))


def sterge_durata_service(lst, zile):
    """
    sterge din lista toate pachetele cu o durata mai scurta de cat un numar de zile dat
    :param lst:  lista de pachete
    :param zile: int
    :return:
    """
    for i in range(0, len(lst)):
        if durata(lst[i]) < zile:
            sterge_pachet_lista(lst, get_id(lst[i]))


def sterge_pret_service(lst, pret):
    """
    sterge din lista toate pachetele cu o durata mai scurta de cat un numar de zile dat
    :param lst:  lista de pachete
    :param pret: float
    :return:
    """
    for i in range(0, len(lst)):
        if get_pret(lst[i]) > pret:
            sterge_pachet_lista(lst, get_id(lst[i]))


def cauta_pachet_data_interval(lst, data1, data2):
    """
    cauta toate pachetele care presupun un sejur într-un interval de date dat
    :param lst: lista de pachete
    :param data1: inceputul de interval
    :param data2: sfersitul de interval
    :return: lista cu pachetele valide
    """
    rezultat = []
    for p in lst:
        if get_data_inceput(p) >= data1 and get_data_sfarsit(p) <= data2:
            rezultat.append(p)
    return rezultat


def cauta_pachet_destinatie_pret(lst, dest, pret):
    """
    cauta toate pachetele cu o destinație dată și cu preț mai mic decât o sumă dată
    :param lst: lista de pachete
    :param dest: string
    :param pret: float
    :return: lista cu pachetele valide
    """
    rezultat = []
    for p in lst:
        if get_destinatie(p) == dest and get_pret(p) < pret:
            rezultat.append(p)
    return rezultat


def cauta_pachet_data_sfarsit(lst, data_s):
    """
    cauta toate pachetele cu o anumita data de sfarsit data
    :param lst: lista de pachete
    :param data_s: date
    :return: lista cu pachetele valide
    """
    rezultat = []
    for p in lst:
        if get_data_sfarsit(p) == data_s:
            rezultat.append(p)
    return rezultat


def nr_pachete_destinatie(lst, dest):
    """
    numara cate pachete exista cu o destinatie data
    :param lst: lista de pachete
    :param dest: string
    :return: numarul de pachete din lst cu destinatia dest
    """
    contor = 0
    for p in lst:
        if get_destinatie(p) == dest:
            contor = contor + 1
    return contor


def pachete_disponibile_data_interval_pret_cresc(lst, data1, data2):
    """
    cauta toate pachetele disponibile într-o anumită perioadă data în ordinea crescătoare a prețului
    :param lst: lista de pachete
    :param data1: inceputul de interval
    :param data2: sfarsitul de interval
    :return: o lista cu pachetele valide ordonate crescator in functie de pret
    """
    rezultat = cauta_pachet_data_interval(lst, data1, data2)
    rezultat.sort(key=lambda x: get_pret(x))
    return rezultat


def medie_pret_destinatie(lst, destinatie):
    """
    calculeaza media preturilor pachetelor cu o anumita destinatie
    :param lst: lista de pachete
    :param destinatie: string
    :return: media preturilor pachetelor cu o anumita destinatie
    """
    suma = 0
    cont = 0
    for p in lst:
        if get_destinatie(p) == destinatie:
            suma += get_pret(p)
            cont += 1
    if cont == 0:
        return 0
    return suma / cont


def filtreaza_pret_dest_service(lst, pret, dest):
    """
    filtreaza elementele listei
    Eliminarea ofertelor care au un preț mai mare decât cel dat și o destinație diferită de cea citită de la tastatură
    :param lst: lista de pachete
    :param pret: float
    :param dest: string
    :return:
    """
    sterge_pret_service(lst, pret)
    i = 0
    while i < len(lst):
        if get_destinatie(lst[i]) != dest:
            sterge_pachet_lista(lst, get_id(lst[i]))
        else:
            i = i + 1


def filtreaza_luna_service(lst, luna):
    """
    filtreaza elementele listei
    Eliminarea ofertelor în care sejurul presupune zile dintr-o anumită lună (citită de la tastatură
    sub forma unui număr natural între 1 și 12)
    :param lst: lista de pachete
    :param luna: int
    :return:
    """
    i = 0
    while i < len(lst):
        if get_data_inceput(lst[i]).month == luna or get_data_sfarsit(lst[i]).month == luna:
            sterge_pachet_lista(lst, get_id(lst[i]))
        else:
            i = i + 1


def nr_pachete_service(lst):
    """
    returneaza numarul de pachete din lista
    :param lst: lista de pachete
    :return: numarul de pachete din lista de pachete
    """
    return nr_pachete_lista(lst)


def get_lista_pachete_service(lst):
    """
    returneaza lista de pachete
    :param lst: lista de pachete
    :return: lista de pachete
    """
    return get_lista_pachete(lst)
