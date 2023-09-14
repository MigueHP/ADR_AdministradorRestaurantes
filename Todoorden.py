from LOGGER_Base import log


class TodoO:
    def __init__(self, fecha_ordenT=None, nombre_empleadoO=None, num_Mesa=None,
                 nombre_productoO=None, cantidadO=None):
        self._fecha_ordenT = fecha_ordenT
        self._nombre_empleadoO = nombre_empleadoO
        self._num_Mesa = num_Mesa
        self._nombre_productoO = nombre_productoO
        self._cantidadO = cantidadO

    def __str__(self):
        return f'''
             Fecha pedido: {self._fecha_ordenT}, Nombre proveedor: {self._nombre_empleadoO},
            Nombre empleado: {self._num_Mesa} ,
            Nombre Ingrediente: {self._nombre_productoO}, Cantidad: {self._cantidadO},

        '''

    # Metodos get y set    @property


    @property
    def fecha_ordenT(self):
        return self._fecha_ordenT

    @fecha_ordenT.setter
    def fecha_ordenT(self, fecha_ordenT):
        self._fecha_ordenT = fecha_ordenT

    @property
    def nombre_empleadoO(self):
        return self._nombre_empleadoO

    @nombre_empleadoO.setter
    def nombre_empleadoO(self, nombre_empleadoO):
        self._nombre_empleadoO = nombre_empleadoO

    @property
    def num_Mesa(self):
        return self._num_Mesa

    @num_Mesa.setter
    def num_Mesa(self, num_Mesa):
        self._num_Mesa = num_Mesa

    @property
    def nombre_productoO(self):
        return self._nombre_productoO

    @nombre_productoO.setter
    def nombre_productoO(self, nombre_productoO):
        self._nombre_productoO = nombre_productoO

    @property
    def cantidadO(self):
        return self._cantidadO

    @cantidadO.setter
    def cantidadO(self, cantidadO):
        self._cantidadO = cantidadO
