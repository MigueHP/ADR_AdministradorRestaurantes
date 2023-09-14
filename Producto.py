from LOGGER_Base import log


class Producto:
    def __init__(self, id_producto=None, nombre_producto=None, descripcion_producto=None, precio_producto=None):
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._descripcion_producto = descripcion_producto
        self._precio_producto = precio_producto


    def __str__(self):
        return f'''
            ID Producto: {self._id_producto}, Nombre: {self._nombre_producto} ,
            Descripcion: {self._descripcion_producto}, Precio: {self._precio_producto}
        '''

   #Metodos get y set
    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto


    @property
    def nombre_producto(self):
         return self._nombre_producto
    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
            self._nombre_producto = nombre_producto

    @property
    def descripcion_producto(self):
         return self._descripcion_producto
    @descripcion_producto.setter
    def descripcion_producto(self, descripcion_producto):
            self._descripcion_producto =descripcion_producto

    @property
    def precio_producto(self):
        return self._precio_producto
    @precio_producto.setter
    def precio_producto(self, precio_producto):
            self._precio_producto = precio_producto


   # Fin de metodos get y set
if __name__ == '__main__':
    empleado1 = Empleado(nombre_empleado='Pedro Moreno', rol_empleado='Cocinero')
    log.debug(empleado1)