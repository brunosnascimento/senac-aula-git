class Calculadora:
    def __init__(self, num1=20, num2=30):
        self.num1 = num1
        self.num2 = num2
    # metodo - está dentro da classe
    def somar(self):
        return self.num1 + self.num2

    def somar(num1, num2):
        return num1 + num2