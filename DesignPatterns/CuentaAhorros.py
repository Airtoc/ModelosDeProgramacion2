from Name import Name
from Password import Password
from AccountType import AccountType
from Builder import Builder

class CuentaAhorros(Builder):

    def getAccountType(self):
        accountType = AccountType()
        accountType.accountType = "AHORROS"
        return accountType

    def getNameAccount(self):

        name = Name()

        print("¿Cómo se llama?")
        inName = input()
        print(f"Bienvenido, {inName}")
        name.name = inName

        return name

    def getPasswordAcount(self):

        password = Password()

        print("¿Cómo será su contraseña?")
        inPassword = input()
        print(f"Contraseña:, {inPassword}")
        password.Password = inPassword

        return password