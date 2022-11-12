import datetime

from business.service_pachete import adauga_pachet_service, nr_pachete_service, get_lista_pachete_service, \
    modifica_pachet_service, sterge_destinatie_service, sterge_durata_service, sterge_pret_service, \
    cauta_pachet_data_interval, cauta_pachet_destinatie_pret, cauta_pachet_data_sfarsit, nr_pachete_destinatie, \
    pachete_disponibile_data_interval_pret_cresc, medie_pret_destinatie, filtreaza_pret_dest_service, \
    filtreaza_luna_service
from domain.pachet import to_string_pachet


def ui_adauga_pachet(lst, undo, params):
    try:
        if len(params) != 5:
            print("numar parametri invalid!")
            return
        id = int(params[0])
        data_inceput = datetime.date(int(params[1].split(',')[0]),
                                     int(params[1].split(',')[1]),
                                     int(params[1].split(',')[2]))
        data_sfarsit = datetime.date(int(params[2].split(',')[0]),
                                     int(params[2].split(',')[1]),
                                     int(params[2].split(',')[2]))
        destinatia = str(params[3])
        pret = float(params[4])
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        adauga_pachet_service(lst, id, data_inceput, data_sfarsit, destinatia, pret)
    except ValueError as ve:
        print(str(ve))


def ui_print_pachete(lst, undo, params):
    if len(params) != 0:
        print("numar parametri invalid!")
        return
    if nr_pachete_service(lst) == 0:
        print("nu exista pachete in stoc!")
        return
    pachete = get_lista_pachete_service(lst)
    for p in pachete:
        print(to_string_pachet(p))


def ui_modifica_pachet(lst, undo, params):
    try:
        if len(params) != 5:
            print("numar parametri invalid!")
            return
        id = int(params[0])
        data_inceput = datetime.date(int(params[1].split(',')[0]),
                                     int(params[1].split(',')[1]),
                                     int(params[1].split(',')[2]))
        data_sfarsit = datetime.date(int(params[2].split(',')[0]),
                                     int(params[2].split(',')[1]),
                                     int(params[2].split(',')[2]))
        destinatia = str(params[3])
        pret = float(params[4])
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        modifica_pachet_service(lst, id, data_inceput, data_sfarsit, destinatia, pret)
    except ValueError as ve:
        print(str(ve))


def ui_sterge_destinatie(lst, undo, params):
    try:
        if len(params) != 1:
            print("numar parametri invalid!")
            return
        destinatie = params[0]
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        sterge_destinatie_service(lst, destinatie)
    except ValueError as ve:
        print(str(ve))


def ui_sterge_durata(lst, undo, params):
    try:
        if len(params) != 1:
            print("numar parametri invalid!")
            return
        zile = int(params[0])
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        sterge_durata_service(lst, zile)
    except ValueError as ve:
        print(str(ve))


def ui_sterge_pret(lst, undo, params):
    try:
        if len(params) != 1:
            print("numar parametri invalid!")
            return
        pret = float(params[0])
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        sterge_pret_service(lst, pret)
    except ValueError as ve:
        print(str(ve))


def ui_cauta_data_interval(lst, undo, params):
    if len(params) != 2:
        print("numar parametri invalid!")
        return
    data1 = datetime.date(int(params[0].split(',')[0]),
                          int(params[0].split(',')[1]),
                          int(params[0].split(',')[2]))
    data2 = datetime.date(int(params[1].split(',')[0]),
                          int(params[1].split(',')[1]),
                          int(params[1].split(',')[2]))
    lista = cauta_pachet_data_interval(lst, data1, data2)
    for i in lista:
        print(to_string_pachet(i))


def ui_cauta_dest_pret(lst, undo, params):
    if len(params) != 2:
        print("numar parametri invalid!")
        return
    dest = params[0]
    pret = float(params[1])
    lista = cauta_pachet_destinatie_pret(lst, dest, pret)
    for i in lista:
        print(to_string_pachet(i))


def ui_cauta_data_sfsrsit(lst, undo, params):
    if len(params) != 1:
        print("numar parametri invalid!")
        return
    data = datetime.date(int(params[0].split(',')[0]),
                         int(params[0].split(',')[1]),
                         int(params[0].split(',')[2]))
    lista = cauta_pachet_data_sfarsit(lst, data)
    for i in lista:
        print(to_string_pachet(i))


def ui_nr_pachete_destinatie(lst, undo, params):
    if len(params) != 1:
        print("numar parametri invalid!")
        return
    dest = params[0]
    print(nr_pachete_destinatie(lst, dest))


def ui_pachete_disponibile_data_interval_pret_cresc(lst, undo, params):
    if len(params) != 2:
        print("numar parametri invalid!")
        return
    data1 = datetime.date(int(params[0].split(',')[0]),
                          int(params[0].split(',')[1]),
                          int(params[0].split(',')[2]))
    data2 = datetime.date(int(params[1].split(',')[0]),
                          int(params[1].split(',')[1]),
                          int(params[1].split(',')[2]))
    lista = pachete_disponibile_data_interval_pret_cresc(lst, data1, data2)
    for i in lista:
        print(to_string_pachet(i))


def ui_medie_pret_destinatie(lst, undo, params):
    if len(params) != 1:
        print("numar parametri invalid!")
        return
    dest = params[0]
    print(medie_pret_destinatie(lst, dest))


def ui_filtreaza_pret_dest(lst, undo, params):
    try:
        if len(params) != 2:
            print("numar parametri invalid!")
            return
        pret = float(params[0])
        dest = params[1]
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        filtreaza_pret_dest_service(lst, pret, dest)
    except ValueError as ve:
        print(str(ve))


def ui_filtreaza_luna(lst, undo, params):
    try:
        if len(params) != 1:
            print("numar parametri invalid!")
            return
        luna = int(params[0])
        lst_copy = [None] * len(lst)
        for i in range(0, len(lst)):
            lst_copy[i] = lst[i]
        undo.append(lst_copy)
        filtreaza_luna_service(lst, luna)
    except ValueError as ve:
        print(str(ve))


def ui_undo(lst, undo, params):
    if len(params) != 0:
        print("numar parametri invalid!")
        return
    if len(undo) == 0:
        raise ValueError("nu se poate face undo!\n")
    un = undo.pop()
    lst.clear()
    lst[:] = un[:]


def print_meniu():
    print("\nadauga_pachet id(int), data inceput(y,m,d) data sfarsit(y,m,d) destinatie(string) pret(float)")
    print("print_pachete")
    print("modifica_pachet id(int), data inceput(y,m,d) data sfarsit(y,m,d) destinatie(string) pret(float)")
    print("sterge_destinatie destinatie(string)")
    print("sterge_durata zile(int)")
    print("sterge_pret pret(float)")
    print("cauta_data_interval data1(y,m,d) data2(y,m,d)")
    print("cauta_destinatie_pret destinatie(string) pret(float)")
    print("cauta_data_sfarsit data(y,m,d)")
    print("nr_destinatie destinatie(string)")
    print("pachete_disponibile data1(y,m,d) data2(y,m,d)")
    print("media_pret destinatie(string)")
    print("filtreaza_pret_dest pret(float) destinatie(string)")
    print("filtreaza_luna luna(int)")
    print("undo")
    print("exit")


def run_ui():
    pachete = []
    undo_stack = []
    comenzi = {
        "adauga_pachet": ui_adauga_pachet,
        "print_pachete": ui_print_pachete,
        "modifica_pachet": ui_modifica_pachet,
        "sterge_destinatie": ui_sterge_destinatie,
        "sterge_durata": ui_sterge_durata,
        "sterge_pret": ui_sterge_pret,
        "cauta_data_interval": ui_cauta_data_interval,
        "cauta_destinatie_pret": ui_cauta_dest_pret,
        "cauta_data_sfarsit": ui_cauta_data_sfsrsit,
        "nr_destinatie": ui_nr_pachete_destinatie,
        "pachete_disponibile": ui_pachete_disponibile_data_interval_pret_cresc,
        "media_pret": ui_medie_pret_destinatie,
        "filtreaza_pret_dest": ui_filtreaza_pret_dest,
        "filtreaza_luna": ui_filtreaza_luna,
        "undo": ui_undo
    }
    while True:
        print_meniu()
        comanda = input(">>>")
        comanda = comanda.strip()
        if comanda == "":
            continue
        if comanda == "exit":
            return
        parti = comanda.split()
        nume_comanda = parti[0]
        params = parti[1:]
        if nume_comanda in comenzi:
            try:
                comenzi[nume_comanda](pachete, undo_stack, params)
            except ValueError as ve:
                print(ve)
        else:
            print("comanda invalida!")
