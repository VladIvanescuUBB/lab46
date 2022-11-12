from domain.pachet import egal_pachete, get_id


def adauga_pachet_lista(lst, pachet):
    """
    adauga pachetul pachet in lista de pachete lst
    :param lst: lista pachete
    :param pachet: pachet
    :return:
    :raises: ValueError cu mesajul "pachet invalid!\n" daca in lista exista deja un pachet cu acelasi id
    """
    for p in lst:
        if egal_pachete(p, pachet):
            raise ValueError("pachet invalid!\n")
    lst.append(pachet)


def cauta_pachet_id(lst, id):
    """
    cauta in lista pachetul cu un id dat
    :param lst: lista de pachete
    :param id: int
    :return: pachetul cu id-ul id sau None daca acesta nu exista
    """
    for p in lst:
        if get_id(p) == id:
            return p
    return None


def modifica_pachet_lista(lst, pachet):
    """
    modifica in lista pachetul cu id-ul pachetului primit ca parametru
    :param lst: lista de pachete
    :param pachet: pachet
    :return:
    :raises: ValueError cu mesajul "pachet invalid!\n" daca in lista nu exista un pachet cu id-ul pachetului pachet
    """
    if cauta_pachet_id(lst, get_id(pachet)) is None:
        raise ValueError("id invalid!\n")
    for i in range(0, len(lst)):
        if get_id(lst[i]) == get_id(pachet):
            lst[i] = pachet


def sterge_pachet_lista(lst, id):
    """
    sterge din lista pachetul cu id-ul dat
    :param lst:  lista de pachete
    :param id: int
    :return:
    """
    if cauta_pachet_id(lst, id) is None:
        raise ValueError("id inexistent!\n")
    i = 0
    while i < len(lst):
        if get_id(lst[i]) == id:
            lst.remove(lst[i])
        else:
            i = i + 1


def nr_pachete_lista(lst):
    """
    returneaza numarul de pachete din lista
    :param lst: lista de pachete
    :return: numarul de pachete din lista de pachete
    """
    return len(lst)


def get_lista_pachete(lst):
    """
    returneaza lista de pachete
    :param lst: lista de pachete
    :return: lista de pachete
    """
    return lst[:]
