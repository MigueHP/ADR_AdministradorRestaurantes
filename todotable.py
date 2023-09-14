from LOGGER_Base import log


class TodoP:
    def __init__(self, fecha_pedidoP=None, nombre_proveedorP=None, nombre_empleadoP=None,
                 nombre_ingredienteP=None, cantidadP=None, ID=None):

        self._fecha_pedidoP = fecha_pedidoP
        self._nombre_proveedorP = nombre_proveedorP
        self._nombre_empleadoP = nombre_empleadoP
        self._ID = ID
        self._nombre_ingredienteP = nombre_ingredienteP
        self._cantidadP = cantidadP

    def __str__(self):
        return f'''
             Fecha pedido: {self._fecha_pedidoP}, Nombre proveedor: {self._nombre_proveedorP},
            Nombre empleado: {self._nombre_empleadoP} ,
            Nombre Ingrediente: {self._nombre_ingredienteP}, Cantidad: {self._cantidadP},
            
        '''

    # Metodos get y set    @property

    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, ID):
        self._ID = ID



    @property
    def fecha_pedidoP(self):
        return self._fecha_pedidoP
    @fecha_pedidoP.setter
    def fecha_pedidoP(self, fecha_pedidoP):
        self._fecha_pedidoP = fecha_pedidoP

    @property
    def nombre_proveedorP(self):
        return self._nombre_proveedorP
    @nombre_proveedorP.setter
    def nombre_proveedorP(self, nombre_proveedorP):
        self._nombre_proveedorP = nombre_proveedorP

    @property
    def nombre_empleadoP(self):
        return self._nombre_empleadoP
    @nombre_empleadoP.setter
    def nombre_empleadoP(self, nombre_empleadoP):
        self._nombre_empleadoP = nombre_empleadoP

    @property
    def nombre_ingredienteP(self):
        return self._nombre_ingredienteP
    @nombre_ingredienteP.setter
    def nombre_ingredienteP(self, nombre_ingredienteP):
        self._nombre_ingredienteP = nombre_ingredienteP

    @property
    def cantidadP(self):
        return self._cantidadP
    @cantidadP.setter
    def cantidadP(self, cantidadP):
        self._cantidadP = cantidadP


# Fin de metodos get y set

if __name__ == '__main__':
    empleado1 = Empleado(nombre_empleado='Pedro Moreno', rol_empleado='Cocinero')
    log.debug(empleado1)
