class conv():

    def __init__(self, unidade1, unidade2, valor):
        self.unidade1 = unidade1
        self.unidade2 = unidade2
        self.valor = valor
    def convteste(self):
        if self.unidade1 == 10 or self.unidade1 == str(10):
            return float(self.valor)*2, ' '
    def conv(self):
        
        if (self.unidade1 == 1 or self.unidade1 == str(1)) and (self.unidade2 == 2 or self.unidade2 == str(2)):
            try:
                return float(self.valor)/3.6, "m/s"
            except ValueError:
                return "Valor inválido", ' '
        
        elif (self.unidade1 == 1 or self.unidade1 == str(1)) and (self.unidade2 == 3 or self.unidade2 == str(3)):
            try:
                return float(self.valor)/1.609, "mi/h"
            except ValueError:
                return "Valor inválido", ' '
        
        elif (self.unidade1 == 2 or self.unidade1 == str(2)) and (self.unidade2 == 1 or self.unidade2 == str(1)):
            try:
                return float(self.valor)*3.6, "km/h"
            except ValueError:
                return "Valor inválido", ' '
        
        elif (self.unidade1 == 2 or self.unidade1 == str(2)) and (self.unidade2 == 3 or self.unidade2 == str(3)):
            try:
                return float(self.valor)*2.237, "mi/h"
            except ValueError:
                return "Valor inválido", ' '
        
        elif (self.unidade1 == 3 or self.unidade1 == str(3)) and (self.unidade2 == 1 or self.unidade2 == str(1)):
            try:
                return float(self.valor)*1.609, "km/h"
            except ValueError:
                return "Valor inválido", ' '

        elif (self.unidade1 == 3 or self.unidade1 == str(3)) and (self.unidade2 == 2 or self.unidade2 == str(2)):
            try:
                return float(self.valor)/2.237, "m/s"
            except ValueError:
                return "Valor inválido", ' '
        
        elif self.unidade1 == 10 or self.unidade1 == str(10):
            return conv.convteste(self)
        
        elif self.unidade1 == self.unidade2:
            try:
                float(self.unidade1)
                float(self.unidade2)
                return "Mesmo tipo de unidade inserida nas duas opções", ' '
            except ValueError:
                return "Unidade inválida", ' '
        
        else:
            try:
                float(self.unidade1)
                float(self.unidade2)
                return "Unidade inválida", ' '
            except ValueError:
                return "Unidade inválida", ' '
            except:
                return "error", ' '