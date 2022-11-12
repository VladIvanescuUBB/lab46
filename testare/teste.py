from testare.teste_domain import test_pachet
from testare.teste_repo import test_repository_pachete
from testare.teste_service import test_service_pachete
from testare.teste_validare import test_validare_pachet


def ruleaza_toate_testele():
    test_pachet()
    print("teste pachet trecute cu succes!")
    test_validare_pachet()
    print("teste validare pachet trecute cu succes!")
    test_repository_pachete()
    print("teste repository pachete trecute cu succes!")
    test_service_pachete()
    print("teste service pachete trecute cu succes!")
