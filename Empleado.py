from LOGGER_Base import log


class Empleado:
    def __init__(self, id_empleado=None, nombre_empleado=None, rol_empleado=None, curp_empleado=None, rfc_empleado=None, domicilio_empleado=None, telefono_empleado=None):
        self._id_empleado = id_empleado
        self._nombre_empleado = nombre_empleado
        self._rol_empleado = rol_empleado
        self._curp_empleado = curp_empleado
        self._rfc_empleado = rfc_empleado
        self._domicilio_empleado = domicilio_empleado
        self._telefono_empleado = telefono_empleado

    def __str__(self):
        return f'''
            ID empleado: {self._id_empleado}, Nombre empleado: {self._nombre_empleado},
            Rol empleado: {self._rol_empleado} CURP empleado: {self._curp_empleado},
            RFC empleado: {self._rfc_empleado}, Domicilio empleado: {self._domicilio_empleado},
            Telefono empleado: {self._telefono_empleado}
        '''

   #Metodos get y set
    @property
    def id_empleado(self):
        return self._id_empleado
    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado


    @property
    def nombre_empleado(self):
         return self._nombre_empleado
    @nombre_empleado.setter
    def nombre_empleado(self, nombre_empleado):
            self._nombre_empleado = nombre_empleado

    @property
    def rol_empleado(self):
         return self._rol_empleado
    @rol_empleado.setter
    def rol_empleado(self, rol_empleado):
            self._rol_empleado = rol_empleado

    @property
    def curp_empleado(self):
        return self._curp_empleado
    @curp_empleado.setter
    def curp_empleado(self, curp_empleado):
            self._curp_empleado = curp_empleado

    @property
    def rfc_empleado(self):
        return self._rfc_empleado
    @rfc_empleado.setter
    def rfc_empleado(self, rfc_empleado):
            self._rfc_empleado = rfc_empleado

    @property
    def domicilio_empleado(self):
        return self._domicilio_empleado
    @domicilio_empleado.setter
    def domicilio_empleado(self, domicilio_empleado):
            self._domicilio_empleado = domicilio_empleado

    @property
    def telefono_empleado(self):
            return self._telefono_empleado
    @telefono_empleado.setter
    def telefono_empleado(self, telefono_empleado):
            self._telefono_empleado = telefono_empleado

   # Fin de metodos get y set

if __name__ == '__main__':
    empleado1 = Empleado(nombre_empleado='Pedro Moreno', rol_empleado='Cocinero')
    log.debug(empleado1)
