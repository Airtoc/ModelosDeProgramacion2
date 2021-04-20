from Facade import Facade

def main():
    
    facade = Facade()

    print("Escoja el tipo de cuenta que desea crear: ")
    print("0. Cuenta Corriente")
    print("1. Cuenta de ahorros")

    print("¿Cuál opción desea?")
    accountSelection = input()

    if accountSelection == "0":
        facade.crearCuentaCorriente()
        print("Cuenta corriente.")

    elif accountSelection == "1":
        facade.crearCuentaAhorros()
        print("Cuenta de ahorros.")

if __name__ == "__main__":
    main()