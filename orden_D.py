from LOGGER_Base import log
from Proveedor import Proveedor
from cursor_del_pool import CursorDelPool
from Oden_P import Orden


class OrdenDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM orden ORDER BY id_orden'
    _ID = 'SELECT id_orden from orden ORDER BY id_orden DESC LIMIT 1'
    _INSERTAR = 'INSERT INTO orden(fecha_orden, id_empleado, num_mesa) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE orden SET fecha_pedido=%s, id_proveedor=%s, id_empleado=%s WHERE id_pedido_stock=%s'
    _ELIMINAR = 'DELETE FROM orden WHERE id_orden=%s'
    _BUSCAR = 'SELECT * FROM pedido_stock WHERE id_pedido_stock=%s'
    _CONSULTA = 'select fecha_pedido, (select proveedores.nombre_proveedor from proveedores where id_proveedor=pedido_stock.id_proveedor),(select nombre_empleado from empleado where id_empleado = pedido_stock.id_empleado) FROM pedido_stock where id_pedido_stock = %s'
    _COMPLETO = 'select pedido_stock.fecha_pedido,(select proveedores.nombre_proveedor from proveedores where id_proveedor=pedido_stock.id_proveedor),(select nombre_empleado from empleado where id_empleado = pedido_stock.id_empleado), (select nombre_ingrediente from ingrediente where id_ingrediente=detalle_pedido_stock.id_ingrediente),detalle_pedido_stock.cantidad from pedido_stock JOIN detalle_pedido_stock  ON pedido_stock.id_pedido_stock = %s AND detalle_pedido_stock.id_pedido_stock=%s'

    @classmethod
    def id(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ID)
            registros = cursor.fetchone()
            for registro in registros:
                pedido = registro
            return pedido

    def completo(cls, todop):
        with CursorDelPool() as cursor:
            valores = (todop.ID, todop.ID,)
            cursor.execute(cls._COMPLETO, valores)
            registros = cursor.fetchall()
            lista = []
            for registro in registros:
                todop = TodoP(registro[0], registro[1], registro[2], registro[3], registro[4])
                print(todop)
                lista.append(todop)
            return lista

    @classmethod
    def consulta(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_pedido_stock,)
            cursor.execute(cls._CONSULTA, valores)
            registros = cursor.fetchall()
            for registro in registros:
                pedido = registro
                return pedido

    @classmethod
    def buscar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_pedido_stock,)
            cursor.execute(cls._BUSCAR, valores)
            registros = cursor.fetchall()
            for registro in registros:
                pedido = registro

        return pedido

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            pedidos = []
            for registro in registros:
                pedido = Orden(registro[0], registro[1], registro[2], registro[3])
                pedidos.append(pedido)
            return pedidos

    @classmethod
    def insertar(cls, orden):
        with CursorDelPool() as cursor:
            valores = (orden.fecha_orden,orden.id_empleado_orden, orden.num_mesa)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {orden}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.fecha, pedido.id_proveedor_, pedido.id_empleado_, pedido.id_pedido_stock)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {pedido}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, pedido):
        with CursorDelPool() as cursor:
            valores = (pedido.id_pedido_stock,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{pedido}')
            return cursor.rowcount


if __name__ == '__main__':
    personas_eliminadas = PedidoDaO.id()
    log.debug(F'Personas eliminadas : {personas_eliminadas}')

