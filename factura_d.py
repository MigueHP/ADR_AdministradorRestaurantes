
from LOGGER_Base import log
from cursor_del_pool import CursorDelPool
from Factura import Factura



class FacturaDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM facturacion ORDER BY id_factura'
    _INSERTAR = 'INSERT INTO facturacion(nombre_autonomo, rfc, regimen, direccion_fiscal, id_orden, concepto) VALUES(%s,%s,%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE facturacion SET nombre_empleado=%s, rol_empleado=%s, curp_empleado=%s, rfc_empleado=%s, domicilio_empleado=%s,telefono_empleado=%s WHERE id_empleado=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE id_empleado=%s'
    _BUSCAR = 'SELECT * FROM facturacion WHERE id_facturacion=%s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            factura = []
            for registro in registros:
                empleado = Factura(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                factura.append(empleado)
            return factura

    @classmethod
    def insertar(cls, factura):
        with CursorDelPool() as cursor:
            valores = (factura.nombre_factura, factura.rfc_factura, factura.regimen_fiscal, factura.dire_factura, factura.id_orden_fac, factura.concepto)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {factura}')
            return cursor.rowcount







