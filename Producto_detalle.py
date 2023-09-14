from LOGGER_Base import log


class Producto_Detalle:
    def __init__(self, id_producto_detalle=None, id_producto_=None, id_ingrediente_receta=None, cantidad_receta=None):
        self._id_producto_detalle = id_producto_detalle
        self._id_producto_ = id_producto_
        self._id_ingrediente_receta = id_ingrediente_receta
        self._cantidad_receta = cantidad_receta


    def __str__(self):
        return f'''
            ID RECETa: {self._id_producto_detalle}, ID Producto: {self._id_producto_} ,
            Id ingrediente: {self._id_ingrediente_receta}, cantidad: {self._cantidad_receta}
        '''

   #Metodos get y set
    @property
    def id_producto_detalle(self):
        return self._id_producto_detalle
    @id_producto_detalle.setter
    def id_producto_detalle(self, id_producto_detalle):
        self._id_producto_detalle = id_producto_detalle


    @property
    def id_producto_(self):
         return self._id_producto_
    @id_producto_.setter
    def id_producto_(self, id_producto_):
            self._id_producto_ = id_producto_

    @property
    def id_ingrediente_receta(self):
         return self._id_ingrediente_receta
    @id_ingrediente_receta.setter
    def id_ingrediente_receta(self, id_ingrediente_receta):
            self._id_ingrediente_receta =id_ingrediente_receta

    @property
    def cantidad_receta(self):
        return self._cantidad_receta
    @cantidad_receta.setter
    def cantidad_receta(self, cantidad_receta):
            self._cantidad_receta = cantidad_receta


   # Fin de metodos get y set
if __name__ == '__main__':
    empleado1 = Empleado(nombre_empleado='Pedro Moreno', rol_empleado='Cocinero')
    log.debug(empleado1)