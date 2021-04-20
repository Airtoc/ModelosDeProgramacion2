from Account import Account

class Director:

    __builder = None

    def setBuilder(self, builder):

        self.__builder = builder

    def getAccount(self):

        account = Account()

        name = self.__builder.getNameAccount()
        account.setName(name)

        password = self.__builder.getPasswordAcount()
        account.setPassword(password)

        accountType = self.__builder.getAccountType()
        account.setAccountType(accountType)

        return account