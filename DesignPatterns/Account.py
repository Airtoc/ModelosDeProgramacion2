class Account:

    def __init__(self):

        self.__name = None
        self.__password = None
        self.__accountType = None

    def setName(self, name):
        self.__name = name

    def setPassword(self, password):
        self.__password = password

    def setAccountType(self, accountType):
        self.__accountType = accountType

    def getAccountInfo(self):
        print("Nombre: "+self.__name.name)
        print("Contraseña: "+self.__password.Password)
        print("Tipo de cuenta: "+self.__accountType.accountType)