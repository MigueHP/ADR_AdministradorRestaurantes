from LOGGER_Base import log
from Proveedor import Proveedor
from cursor_del_pool import CursorDelPool
from Orden_Detalle import Orden_Detalle
from Todoorden import TodoO

class Orden_DetalleDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _COMPLETO = 'select id_producto, (select nombre_producto from producto where id_producto = detalle_orden.id_producto), cantidad, precio_actual from detalle_orden where id_orden=%s'
    _PRECIO = 'select SUM(producto.precio_producto * detalle_orden.cantidad) from producto INNER JOIN detalle_orden ON (producto.id_producto = detalle_orden._id_producto )'
    _INSERTAR = 'INSERT INTO detalle_orden(id_orden, id_producto, cantidad, precio_actual ) VALUES(%s,%s,%s,%s)'
    _ID = 'SELECT id_detalle_orden from detall_orden ORDER BY id_detalle_orden DESC LIMIT 1'
    _SUMA = 'select sum(detalle_orden.precio_actual) from detalle_orden where detalle_orden.id_orden = %s'
    _ACTUALIZAR = 'UPDATE detalle_orden SET  cantidad=%s, precio_actual=%s WHERE id_producto=%s and id_orden = %s'
    _ELIMINAR = 'DELETE FROM detalle_orden WHERE id_producto=%s AND id_orden=%s'
    _BUSCAR = 'SELECT * FROM detalle_orden WHERE id_pedido_stock=%s'
    _CONSULTA = 'select fecha_pedido, (select proveedores.nombre_proveedor from proveedores where id_proveedor=pedido_stock.id_proveedor),(select nombre_empleado from empleado where id_empleado = pedido_stock.id_empleado) FROM pedido_stock where id_pedido_stock = %s'
    _SELECCIONAR = 'SELECT fecha_orden,(select nombre_empleado from empleado where id_empleado = orden.id_empleado),num_mesa, (select nombre_producto from producto where id_producto=detalle_orden.id_producto), cantidad FROM orden JOIN detalle_orden ON orden.id_orden = %s'

    @classmethod
    def suma(cls, orden_detalle):
            with CursorDelPool() as cursor:
                valores = (orden_detalle.id_orden_,)
                cursor.execute(cls._SUMA, valores)
                registros = cursor.fetchone()
                for registro in registros:
                    orden_detalle = registro

            return orden_detalle

    @classmethod
    def id(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ID)
            registros = cursor.fetchone()
            for registro in registros:
                pedido = registro
            return pedido

    @classmethod
    def precio(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (orden_detalle.id_prod,)
            cursor.execute(cls._PRECIO, valores,)
            registros = cursor.fetchall()
            for registro in registros:
                orden_detalle = registro
                return orden_detalle

    def completo(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (orden_detalle.id_orden_,)
            cursor.execute(cls._COMPLETO, valores)
            registros = cursor.fetchall()
            lista = []
            for registro in registros:
                orden_detalle = Orden_Detalle(registro[0], registro[1], registro[2], registro[3])
                print(orden_detalle)
                lista.append(orden_detalle)
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
    def seleccionar(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (orden_detalle.id_orden_,)
            cursor.execute(cls._SELECCIONAR, valores)
            registros = cursor.fetchall()
            lista = []
            for registro in registros:
                ped = TodoO(registro[0], registro[1], registro[2], registro[3], registro[4])
                print(ped)
                lista.append(ped)

            return lista

    @classmethod
    def insertar(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (
            orden_detalle.id_orden_, orden_detalle.id_prod, orden_detalle.cant_p,orden_detalle.precio_actual)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {orden_detalle}')
            return cursor.rowcount




    @classmethod
    def actualizar(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (orden_detalle.cant_p, orden_detalle.precio_actual, orden_detalle.id_prod, orden_detalle.id_orden_)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {orden_detalle}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, orden_detalle):
        with CursorDelPool() as cursor:
            valores = (orden_detalle.id_prod, orden_detalle.id_orden_)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{orden_detalle}')
            return cursor.rowcount


if __name__ == '__main__':

    pa = Orden_DetalleDAO.seleccionar(Orden_Detalle(id_orden_=5061))


