from LOGGER_Base import log


class Orden_Detalle:
    def __init__(self, id_detalle_orden=None, id_orden_=None, id_prod=None, cant_p=None, precio_actual=None):
        self._id_detalle_orden = id_detalle_orden
        self._id_orden_ = id_orden_
        self._id_prod = id_prod
        self._cant_p = cant_p
        self._precio_actual = precio_actual


    def __str__(self):
        return f'''
           ID Orden: {self._id_detalle_orden} ID Orden: {self._id_orden_}, Fecha de orden: {self._id_prod},
            ID empleado: {self._cant_p} num mesa: {self._precio_actual}
        '''

   #Metodos get y set
    @property
    def id_detalle_orden(self):
        return self._id_detalle_orden
    @id_detalle_orden.setter
    def id_detalle_orden(self, id_detalle_orden):
        self._id_detalle_orden = id_detalle_orden

    @property
    def id_orden_(self):
        return self._id_orden_
    @id_orden_.setter
    def id_orden_(self, id_orden_):
        self._id_orden_ = id_orden_


    @property
    def id_prod(self):
         return self._id_prod
    @id_prod.setter
    def id_prod(self, id_prod):
            self._id_prod = id_prod

    @property
    def cant_p(self):
         return self._cant_p
    @cant_p.setter
    def cant_p(self, cant_p):
            self._cant_p =cant_p

    @property
    def precio_actual(self):
        return self._precio_actual
    @precio_actual.setter
    def precio_actual(self, precio_actual):
            self._precio_actual = precio_actual


   # Fin de metodos get y set