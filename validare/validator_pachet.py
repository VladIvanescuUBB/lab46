from domain.pachet import get_id, get_destinatie, get_pret


def valideaza_pachet(pachet):
    """
    verifica daca id-ul pachetului e >= 0, destinatia nu e vida si pretul e > 0.0
    :param pachet: pachet
    :return:
    :raises ValueError: daca id-ul e < 0, "id invalid!\n" va fi concatenat la stringul de erori,
    daca destinatia este vida, "destinatie vida!\n" va fi concatenat la stringul de erori,
    daca pretul e <= 0.0, "pret invalid!\n" va fi concatenat la stringul de erori
    daca cel putin un mesaj e concatenat la str de erori se va arunca ValueError cu mesajul/mesajele respective
    """
    erori = ""
    if get_id(pachet) < 0:
        erori += "id invalid!\n"
    if get_destinatie(pachet) == "":
        erori += "destinatie vida!\n"
    if get_pret(pachet) <= 0.0:
        erori += "pret invalid!\n"
    if len(erori) > 0:
        raise ValueError(erori)
