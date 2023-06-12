class Casilla():
    def __init__(self,nCalle,dist,trecorid):
        self.nombreCalle=nCalle
        self.distancia=dist
        self.tiempoRecorrido=trecorid
    
    def getnCalle(self):
        return self.nombreCalle
    

    def getDistancia(self):
        return self.distancia
    
    def getTRecorrido(self):
        return self.tiempoRecorrido
