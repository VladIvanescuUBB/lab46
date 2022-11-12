import datetime

from domain.pachet import creeaza_pachet
from validare.validator_pachet import valideaza_pachet


def test_validare_pachet():
    id_pachet = 1
    data_inceput = datetime.date(2022, 3, 17)
    data_sfarsit = datetime.date(2022, 3, 20)
    destinatie = "Cluj"
    pret = 12.5
    pachet = creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet)

    id_pachet2 = -3
    data_inceput2 = datetime.date(2022, 3, 17)
    data_sfarsit2 = datetime.date(2022, 3, 20)
    destinatie2 = ""
    pret2 = 0.0
    pachet2 = creeaza_pachet(id_pachet2, data_inceput2, data_sfarsit2, destinatie2, pret2)
    try:
        valideaza_pachet(pachet2)
        assert False
    except ValueError as ve:
        assert (str(ve) == "id invalid!\ndestinatie vida!\npret invalid!\n")
