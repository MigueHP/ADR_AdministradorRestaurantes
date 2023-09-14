from LOGGER_Base import log


class Orden:
    def __init__(self, id_orden=None, fecha_orden=None, id_empleado_orden=None, num_mesa=None):
        self._id_orden = id_orden
        self._fecha_orden = fecha_orden
        self._id_empleado_orden = id_empleado_orden
        self._num_mesa = num_mesa


    def __str__(self):
        return f'''
            ID Orden: {self._id_orden}, Fecha de orden: {self._fecha_orden},
            ID empleado: {self._id_empleado_orden} num mesa: {self._num_mesa}
        '''

   #Metodos get y set
    @property
    def id_orden(self):
        return self._id_orden
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden


    @property
    def fecha_orden(self):
         return self._fecha_orden
    @fecha_orden.setter
    def fecha_orden(self, fecha):
            self._fecha_orden = fecha

    @property
    def id_empleado_orden(self):
         return self._id_empleado_orden
    @id_empleado_orden.setter
    def id_empleado_orden(self, id_empleado_orden):
            self._id_empleado_orden =id_empleado_orden

    @property
    def num_mesa(self):
        return self._num_mesa
    @num_mesa.setter
    def num_mesa(self, num_mesa):
            self._num_mesa = num_mesa


   # Fin de metodos get y set