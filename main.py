from prezentare.ui import run_ui
from prezentare.ui_lista_comenzi import run_ui_lista_comenzi
from testare.teste import ruleaza_toate_testele


def main():
    print("Start")
    ruleaza_toate_testele()
    tip = int(input("Alegeti tipul de UI (1. meniu / 2. linie de comanda): "))
    if tip == 1:
        run_ui()
    elif tip == 2:
        run_ui_lista_comenzi()
    print("Stop")


main()
