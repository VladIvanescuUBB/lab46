from prezentare.ui import ui_adauga_pachet, ui_print_pachete, ui_modifica_pachet, ui_sterge_destinatie, \
    ui_sterge_durata, ui_sterge_pret, ui_cauta_data_interval, ui_cauta_dest_pret, ui_cauta_data_sfsrsit, \
    ui_nr_pachete_destinatie, ui_pachete_disponibile_data_interval_pret_cresc, ui_medie_pret_destinatie, \
    ui_filtreaza_pret_dest, ui_filtreaza_luna, ui_undo, print_meniu


def run_ui_lista_comenzi():
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
        comanda = comanda.split(";")
        if comanda == "":
            continue
        if comanda == "exit":
            return
        for i in range(0, len(comanda)):
            parti = comanda[i].split()
            nume_comanda = parti[0]
            if nume_comanda == "":
                continue
            if nume_comanda == "exit":
                return
            params = parti[1:]
            if nume_comanda in comenzi:
                try:
                    comenzi[nume_comanda](pachete, undo_stack, params)
                except ValueError as ve:
                    print(ve)
            else:
                print("comanda invalida!")
