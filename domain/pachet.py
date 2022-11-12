def creeaza_pachet(id_pachet, data_inceput, data_sfarsit, destinatie, pret):
    """
    Creeaza un pachet de calatorie
    :param id_pachet: int
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: float
    :return: pachet cu id-ul id_pachet, data de inceput data_inceput, data de sfarsit data_sfarsit,
    destinatia destinatie, pretul pret
    """
    # return [id_pachet, data_inceput, data_sfarsit, destinatie, pret]
    return {"id_pachet": id_pachet, "data_inceput": data_inceput, "data_sfarsit": data_sfarsit,
            "destinatie": destinatie, "pret": pret}


def get_id(pachet):
    """
    returneaza id-ul int al pachetului
    :param pachet: pachet
    :return: id-ul pachetului pachet
    """
    return pachet["id_pachet"]


def get_data_inceput(pachet):
    """
    returneaza data_inceput date a pachetului
    :param pachet: pachet
    :return: data_inceput a pachetului pachet
    """
    return pachet["data_inceput"]


def get_data_sfarsit(pachet):
    """
    returneaza data_sfarsit date a pachetului
    :param pachet: pachet
    :return: data_sfarsit a pachetului pachet
    """
    return pachet["data_sfarsit"]


def get_destinatie(pachet):
    """
    returneaza destinatia string a pachetului
    :param pachet: pachet
    :return: destinatia pachetului pachet
    """
    return pachet["destinatie"]


def get_pret(pachet):
    """
    returneaza pretul float al pachetului
    :param pachet: pachet
    :return: pretul pachetului pachet
    """
    return pachet["pret"]


def durata(pachet):
    """
    returneaza durata calatoriei in zile
    :param pachet: pachet
    :return: durata calatoriei in zile (int)
    """
    return abs((pachet["data_sfarsit"] - pachet["data_inceput"]).days)


def egal_pachete(pachet1, pachet2):
    """
    verifica daca pachet1 si pachet2 au acelasi id
    :param pachet1: pachet
    :param pachet2: pachet
    :return: True, daca pachetele au acelasi id, False altfel
    """
    return get_id(pachet1) == get_id(pachet2)


def to_string_pachet(pachet):
    """
    returneaza pachetul pachet sub forma de string
    :param pachet: pachet
    :return: pachetul pachet sub forma de string
    """
    return f"[{get_id(pachet)}], {get_data_inceput(pachet)}->{get_data_sfarsit(pachet)}, " \
           f"{get_destinatie(pachet)}, {get_pret(pachet)}"
