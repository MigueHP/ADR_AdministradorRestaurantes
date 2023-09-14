from LOGGER_Base import log


class Proveedor:
    def __init__(self, id_proveedor=None, nombre_proveedor=None, telefono_proveedor=None, dire_proveedor=None):
        self._id_proveedor = id_proveedor
        self._nombre_proveedor = nombre_proveedor
        self._telefono_proveeor = telefono_proveedor
        self._dire_proveedor = dire_proveedor


    def __str__(self):
        return f'''
            ID proveedor: {self._id_proveedor}, Nombre proveedor: {self._nombre_proveedor},
            Telefono proveedor: {self._telefono_proveeor} Direccion proveedor: {self._dire_proveedor}
        '''

   #Metodos get y set
    @property
    def id_proveedor(self):
        return self._id_proveedor
    @id_proveedor.setter
    def id_proveedor(self, id_proveedor):
        self._id_proveedor = id_proveedor


    @property
    def nombre_proveedor(self):
         return self._nombre_proveedor
    @nombre_proveedor.setter
    def nombre_proveedor(self, nombre_proveedor):
            self._nombre_proveedor = nombre_proveedor

    @property
    def telefono_proveedor(self):
         return self._telefono_proveeor
    @telefono_proveedor.setter
    def telefono_proveedor(self, telefono_proveedor):
            self._telefono_proveeor =telefono_proveedor

    @property
    def dire_proveedor(self):
        return self._dire_proveedor
    @dire_proveedor.setter
    def dire_proveedor(self, dire_proveedor):
            self._dire_proveedor = dire_proveedor


   # Fin de metodos get y set

