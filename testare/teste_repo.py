import datetime

from domain.pachet import creeaza_pachet
from infrastructura.repository_pachete import nr_pachete_lista, adauga_pachet_lista, get_lista_pachete, \
    modifica_pachet_lista, sterge_pachet_lista, cauta_pachet_id


def test_repository_adauga():
    pachete = []
    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_lista(pachete) == 0)
    adauga_pachet_lista(pachete, pachet)
    assert (nr_pachete_lista(pachete) == 1)

    id_pachet2 = 1
    data_inceput2 = datetime.date(2022, 4, 17)
    data_sfarsit2 = datetime.date(2022, 4, 20)
    destinatie2 = "Alba"
    pret2 = 30.0
    pachet2 = creeaza_pachet(id_pachet2, data_inceput2, data_sfarsit2, destinatie2, pret2)
    try:
        adauga_pachet_lista(pachete, pachet2)
        assert False
    except ValueError as ve:
        assert (str(ve) == "pachet invalid!\n")

    assert (get_lista_pachete(pachete) == [pachet])


def test_repository_cauta_id():
    pachete = []

    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_lista(pachete) == 0)
    adauga_pachet_lista(pachete, pachet)
    assert (nr_pachete_lista(pachete) == 1)

    assert (cauta_pachet_id(pachete, 1) == pachet)
    assert (cauta_pachet_id(pachete, 2) is None)


def test_repository_modifica():
    pachete = []
    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_lista(pachete) == 0)
    adauga_pachet_lista(pachete, pachet)
    assert (nr_pachete_lista(pachete) == 1)

    id_pachetn = 1
    data_inceputn = datetime.date(2022, 4, 17)
    data_sfarsitn = datetime.date(2022, 4, 20)
    destinatien = "Alba"
    pretn = 30.0
    pachet_n = creeaza_pachet(id_pachetn, data_inceputn, data_sfarsitn, destinatien, pretn)

    modifica_pachet_lista(pachete, pachet_n)
    assert (get_lista_pachete(pachete) == [pachet_n])

    id_pachet = 5
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    try:
        modifica_pachet_lista(pachete, pachet)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id invalid!\n")


def test_repository_sterge():
    pachete = []
    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (nr_pachete_lista(pachete) == 0)
    adauga_pachet_lista(pachete, pachet)
    assert (nr_pachete_lista(pachete) == 1)

    sterge_pachet_lista(pachete, 1)
    assert (nr_pachete_lista(pachete) == 0)


def test_repository_pachete():
    test_repository_adauga()
    test_repository_cauta_id()
    test_repository_modifica()
    test_repository_sterge()
