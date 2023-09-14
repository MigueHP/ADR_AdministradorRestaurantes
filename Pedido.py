from LOGGER_Base import log


class Pedido:
    def __init__(self, id_pedido_stock=None, fecha=None, id_proveedor_=None, id_empleado_=None):
        self._id_pedido_stock = id_pedido_stock
        self._fecha = fecha
        self._id_prov = id_proveedor_
        self._id_empleado_ = id_empleado_


    def __str__(self):
        return f'''
            ID Pedido: {self._id_pedido_stock}, Fecha de pedido: {self.fecha},
            ID Proveedor: {self._id_prov} ID empleado: {self._id_empleado_}
        '''

   #Metodos get y set
    @property
    def id_pedido_stock(self):
        return self._id_pedido_stock
    @id_pedido_stock.setter
    def id_pedido_stock(self, id_pedido_stock):
        self._id_pedido_stock = id_pedido_stock


    @property
    def fecha(self):
         return self._fecha
    @fecha.setter
    def fecha(self, fecha):
            self._fecha = fecha

    @property
    def id_proveedor_(self):
         return self._id_prov
    @id_proveedor_.setter
    def id_proveedor_(self, id_proveedor_):
            self._id_prov =id_proveedor_

    @property
    def id_empleado_(self):
        return self._id_empleado_
    @id_empleado_.setter
    def id_empleado_(self, id_empleado_):
            self._id_empleado_ = id_empleado_


   # Fin de metodos get y set