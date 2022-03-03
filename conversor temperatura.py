class Termometro():
    def __init__(self):
        self.__unidadM = 'C'
        self.__termperatura = 0
        
    def conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".formar(temperatura - 32 * 5/9)
        else:
            return "unidad incorrecta"
            
            
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidadM)rantanplan = PerroAsistencia('Ran Tan Plan', 4, 8, 'Lucky Luke')
    
    def unidadmedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if self.uniM == 'F' or uniM == 'C':
                self.unidadM = uniM
                
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else
            self.__temperatura = temperatura
            
        def mide(self, uniM=None):
            if uniM == None or uniM == self.unidadM:
                return self.__srt__()
            else:
                return self.conversor(self.temperatura, uniM)
            
            
            
            
            
            
            
            
            
            
            