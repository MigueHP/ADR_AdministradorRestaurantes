from LOGGER_Base import log


class Factura:
    def __init__(self, nombre_factura=None, rfc_factura=None, regimen_fiscal=None, dire_factura=None, id_orden_fac=None, concepto=None):
        self._nombre_factura = nombre_factura
        self._rfc_factura = rfc_factura
        self._regimen_fiscal = regimen_fiscal
        self._dire_factura = dire_factura
        self._id_orden_fac = id_orden_fac
        self._concepto = concepto


    def __str__(self):
        return f'''
            ID empleado: {self._nombre_factura}, Nombre empleado: {self._rfc_factura},
            Rol empleado: {self._regimen_fiscal} CURP empleado: {self._dire_factura},
            RFC empleado: {self._concepto}, Domicilio empleado: {self._id_orden_fac}
        '''

   #Metodos get y set
    @property
    def nombre_factura(self):
        return self._nombre_factura
    @nombre_factura.setter
    def nombre_factura(self, nombre_factura):
        self._nombre_factura = nombre_factura


    @property
    def rfc_factura(self):
         return self._rfc_factura
    @rfc_factura.setter
    def rfc_factura(self, rfc_factura):
            self._rfc_factura = rfc_factura

    @property
    def regimen_fiscal(self):
         return self._regimen_fiscal
    @regimen_fiscal.setter
    def regimen_fiscal(self, regimen_fiscal):
            self._regimen_fiscal = regimen_fiscal

    @property
    def dire_factura(self):
        return self._dire_factura
    @dire_factura.setter
    def dire_factura(self, dire_factura):
            self._dire_factura = dire_factura

    @property
    def concepto(self):
        return self._concepto
    @concepto.setter
    def concepto(self, concepto):
            self._concepto = concepto

    @property
    def id_orden_fac(self):
        return self._id_orden_fac
    @id_orden_fac.setter
    def id_orden_fac(self, id_orden_fac):
            self._id_orden_fac = id_orden_fac

   # Fin de metodos get y set

