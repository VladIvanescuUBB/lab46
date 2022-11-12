import datetime

from domain.pachet import creeaza_pachet, get_id, get_data_inceput, get_data_sfarsit, get_destinatie, get_pret, \
    egal_pachete, to_string_pachet, durata


def test_pachet():
    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    assert (id_pachet == get_id(pachet))
    assert (data_inceput == get_data_inceput(pachet))
    assert (data_sfarsit == get_data_sfarsit(pachet))
    assert (destinatie == get_destinatie(pachet))
    assert (abs(pret - get_pret(pachet)) < 0.0001)
    assert (durata(pachet) == 3)

    assert (to_string_pachet(pachet) == "[1], 2022-03-17->2022-03-20, Cluj, 12.5")

    id_pachet2 = 2
    data_inceput2 = datetime.date(2022, 3, 17)
    data_sfarsit2 = datetime.date(2022, 3, 20)
    destinatie2 = "alba"
    pret2 = 5.0
    pachet2 = creeaza_pachet(id_pachet2, data_inceput2, data_sfarsit2, destinatie2, pret2)
    assert (egal_pachete(pachet, pachet) is True)
    assert (egal_pachete(pachet, pachet2) is False)
