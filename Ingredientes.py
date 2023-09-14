from LOGGER_Base import log


class Ingrediente:
    def __init__(self, id_ingrediente=None, nombre_ingrediente=None, id_prov=None, cantidad=None):
        self._id_ingrediente = id_ingrediente
        self._nombre_ingrediente = nombre_ingrediente
        self._id_prov = id_prov
        self._cantidad = cantidad
    def __str__(self):
        return f'''
            ID ingrediente: {self._id_ingrediente}, Nombre ingrediente: {self._nombre_ingrediente},
            ID Provedoor: {self._id_prov} Cantidad: {self._cantidad},
        '''

   #Metodos get y set
    @property
    def id_ingrediente(self):
        return self._id_ingrediente
    @id_ingrediente.setter
    def id_ingrediente(self, id_ingrediente):
        self._id_ingrediente = id_ingrediente


    @property
    def nombre_ingrediente(self):
         return self._nombre_ingrediente
    @nombre_ingrediente.setter
    def nombre_ingrediente(self, nombre_ingrediente):
            self._nombre_ingrediente = nombre_ingrediente

    @property
    def id_prov(self):
         return self._id_prov
    @id_prov.setter
    def id_prov(self, id_prov):
            self._id_prov = id_prov

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
            self._cantidad = cantidad

   # Fin de metodos get y set

if __name__ == '__main__':
    empleado1 = Empleado(nombre_empleado='Pedro Moreno', rol_empleado='Cocinero')
    log.debug(empleado1)
