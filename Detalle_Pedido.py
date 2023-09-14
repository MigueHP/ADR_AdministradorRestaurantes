from LOGGER_Base import log


class Detalle_Pedido:
    def __init__(self, id_PStock=None, id_INGD=None, cant_i=None):
        self._id_PStock = id_PStock
        self._id_INGD = id_INGD
        self._cant_i = cant_i


    def __str__(self):
        return f'''
             ID pedido: {self._id_PStock},
            ID ingrediente: {self._id_INGD} Cantidad de ingrediente: {self._cant_i}
        '''

   #Metodos get y set


    @property
    def id_PStock(self):
         return self._id_PStock
    @id_PStock.setter
    def id_PStock(self, id_PStock):
            self._id_PStock = id_PStock

    @property
    def id_INGD(self):
         return self._id_INGD
    @id_INGD.setter
    def id_INGD(self, id_INGD):
            self._id_INGD =id_INGD

    @property
    def cant_i(self):
        return self._cant_i
    @cant_i.setter
    def cant_i(self, cant_i):
            self._cant_i = cant_i


   # Fin de metodos get y set

