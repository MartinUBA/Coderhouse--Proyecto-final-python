from urllib import request


class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("Carro")
        if not carro:
            carro= self.session["Carro"]= {}
        #else:
        self.carro=carro

    def agregar(self,juego):
        if (str(juego.id)not in self.carro.keys ()):
            self.carro[juego.id]={
                "juego_id": juego.id,
                "nombre": juego.nombre,
                "precio":str(juego.precio),
                "cantidad":1,
                "imagen":juego.imagen.url

            }
        else:
            for key, value in self.carro.items():
                if key == str(juego.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+juego.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,juego):
        juego.id=str(juego.id)
        if juego.id in self.carro:
            del self.carro[juego.id]
            self.guardar_carro()

    def restar_producto (self,juego):
        for key, value in self.carro.items():
                if key == str(juego.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-juego.precio
                    if value["cantidad"]<1:
                        self.eliminar(juego)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["Carro"]= {}
        self.session.modified=True 