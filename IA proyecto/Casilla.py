class Casilla():
    def __init__(self,nCalle,nid,dist,trecorid):
        self.nombreCalle=nCalle
        self.numeroid=nid
        self.distancia=dist
        self.tiempoRecorrido=trecorid
    
    def getnCalle(self):
        return self.nombreCalle
    
    def getnID(self):
        return self.numeroid

    def getDistancia(self):
        return self.distancia
    
    def getTRecorrido(self):
        return self.tiempoRecorrido
