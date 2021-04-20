from Director import Director
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class Facade:

    director = Director()

    def crearCuentaAhorros(self):
        cuentaAhorrosBuilder = CuentaAhorros()
        director = Director()
        director.setBuilder(cuentaAhorrosBuilder)
        cuentaAhorros = director.getAccount()
        cuentaAhorros.getAccountInfo()
        print("Creando cuenta de ahorros.")

    def crearCuentaCorriente(self):
        cuentaCorrienteBuilder = CuentaCorriente()
        director = Director()
        director.setBuilder(cuentaCorrienteBuilder)
        cuentaCorriente = director.getAccount()
        cuentaCorriente.getAccountInfo()
        print("Creando cuenta corriente.")