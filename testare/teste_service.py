import datetime

from business.service_pachete import nr_pachete_service, adauga_pachet_service, get_lista_pachete_service, \
    modifica_pachet_service, sterge_destinatie_service, sterge_durata_service, sterge_pret_service, \
    filtreaza_pret_dest_service, cauta_pachet_data_interval, cauta_pachet_destinatie_pret, cauta_pachet_data_sfarsit, \
    nr_pachete_destinatie, pachete_disponibile_data_interval_pret_cresc, medie_pret_destinatie, filtreaza_luna_service
from domain.pachet import creeaza_pachet
from infrastructura.repository_pachete import sterge_pachet_lista


def test_service_adauga():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5

    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)
    assert (get_lista_pachete_service(pachete) == [
        creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)])

    id_pachet2 = 1
    data_inceput2 = datetime.date(2022, 4, 17)
    data_sfarsit2 = datetime.date(2022, 4, 20)
    destinatie2 = "Alba"
    pret2 = 30.0
    try:
        adauga_pachet_service(pachete, id_pachet2, data_inceput2, data_sfarsit2, destinatie2, pret2)
        assert False
    except ValueError as ve:
        assert (str(ve) == "pachet invalid!\n")

    id_pachet3 = -2
    data_inceput3 = datetime.date(2022, 4, 17)
    data_sfarsit3 = datetime.date(2022, 4, 20)
    destinatie3 = ""
    pret3 = 0.0
    try:
        adauga_pachet_service(pachete, id_pachet3, data_inceput3, data_sfarsit3, destinatie3, pret3)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id invalid!\ndestinatie vida!\npret invalid!\n")


def test_service_modifica_pachet():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5

    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)
    assert (get_lista_pachete_service(pachete) == [
        creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)])

    id_pachetn = 1
    data_inceputn = datetime.date(2022, 3, 17)
    data_sfarsitn = datetime.date(2022, 3, 20)
    destinatien = "Alba"
    pretn = 30.2
    pachetn = creeaza_pachet(id_pachetn, data_inceputn, data_sfarsitn, destinatien, pretn)
    modifica_pachet_service(pachete, id_pachetn, data_inceputn, data_sfarsitn, destinatien, pretn)
    assert (get_lista_pachete_service(pachete) == [pachetn])

    id_pachetn = 5
    data_inceputn = datetime.date(2022, 3, 17)
    data_sfarsitn = datetime.date(2022, 3, 20)
    destinatien = "Alba"
    pretn = 30.2
    try:
        modifica_pachet_service(pachete, id_pachetn, data_inceputn, data_sfarsitn, destinatien, pretn)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id invalid!\n")


def test_service_sterge_id():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    try:
        sterge_pachet_lista(pachete, 2)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id inexistent!\n")

    assert (nr_pachete_service(pachete) == 1)
    sterge_pachet_lista(pachete, 1)
    assert (nr_pachete_service(pachete) == 0)


def test_service_sterge_destinatie():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5

    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    sterge_destinatie_service(pachete, "Cluj")
    assert (get_lista_pachete_service(pachete) == [])
    assert (nr_pachete_service(pachete) == 0)


def test_service_sterge_durata():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5

    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    sterge_durata_service(pachete, 2)
    assert (nr_pachete_service(pachete) == 1)
    sterge_durata_service(pachete, 4)
    assert (nr_pachete_service(pachete) == 0)


def test_service_sterge_pret():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5

    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    sterge_pret_service(pachete, 20)
    assert (nr_pachete_service(pachete) == 1)
    sterge_pret_service(pachete, 10)
    assert (nr_pachete_service(pachete) == 0)


def test_service_cautare_data_interval():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    lista = cauta_pachet_data_interval(pachete, datetime.date(2022, 3, 18), datetime.date(2022, 3, 25))
    assert (len(lista) == 0)
    lista = cauta_pachet_data_interval(pachete, datetime.date(2022, 3, 16), datetime.date(2022, 3, 20))
    assert (len(lista) == 1)


def test_service_cautare_destinatie_pret():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    lista = cauta_pachet_destinatie_pret(pachete, "Alba", 20)
    assert (len(lista) == 0)
    lista = cauta_pachet_destinatie_pret(pachete, "Cluj", 10)
    assert (len(lista) == 0)
    lista = cauta_pachet_destinatie_pret(pachete, "Cluj", 20)
    assert (len(lista) == 1)


def test_service_cautare_data_sfarsit():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    lista = cauta_pachet_data_sfarsit(pachete, datetime.date(2002, 3, 27))
    assert (len(lista) == 0)
    lista = cauta_pachet_data_sfarsit(pachete, datetime.date(2022, 3, 20))
    assert (len(lista) == 1)


def test_service_nr_pachete_destinatie():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    assert (nr_pachete_destinatie(pachete, "Alba") == 0)
    assert (nr_pachete_destinatie(pachete, "Cluj") == 1)


def test_service_pachete_disponibile_data_interval_pret_cresc():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 30
    pachet1 = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)
    id_pachet = 2
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Alba"
    pret = 20
    pachet2 = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 2)

    lista = pachete_disponibile_data_interval_pret_cresc(pachete,
                                                         datetime.date(2022, 3, 16), datetime.date(2022, 3, 23))
    assert (len(lista) == 2)
    assert (lista[0] == pachet2)
    assert (lista[1] == pachet1)


def test_service_medie_pret_destinatie():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 30
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)
    id_pachet = 2
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 20
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 2)

    assert (medie_pret_destinatie(pachete, "Alba") == 0)
    assert (medie_pret_destinatie(pachete, "Cluj") == 25)


def test_service_filtrare_pret_dest():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    id_pachet = 2
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Alba"
    pret = 50
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 2)

    filtreaza_pret_dest_service(pachete, 25, "Cluj")
    assert (nr_pachete_service(pachete) == 1)
    filtreaza_pret_dest_service(pachete, 25, "Alba")
    assert (nr_pachete_service(pachete) == 0)


def test_service_filtrare_luna():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    assert (nr_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 1)

    id_pachet = 2
    data_inceput = datetime.date(2022, 5, 17)
    data_sfarsit = datetime.date(2022, 5, 20)
    destinatie = "Alba"
    pret = 50
    adauga_pachet_service(pachete, id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_service(pachete) == 2)

    filtreaza_luna_service(pachete, 3)
    assert (nr_pachete_service(pachete) == 1)
    filtreaza_luna_service(pachete, 5)
    assert (nr_pachete_service(pachete) == 0)


def test_service_pachete():
    test_service_adauga()
    test_service_modifica_pachet()
    test_service_sterge_id()
    test_service_sterge_destinatie()
    test_service_sterge_durata()
    test_service_sterge_pret()
    test_service_cautare_data_interval()
    test_service_cautare_destinatie_pret()
    test_service_cautare_data_sfarsit()
    test_service_nr_pachete_destinatie()
    test_service_pachete_disponibile_data_interval_pret_cresc()
    test_service_medie_pret_destinatie()
    test_service_filtrare_pret_dest()
    test_service_filtrare_luna()
