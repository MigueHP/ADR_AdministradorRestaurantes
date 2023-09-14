from LOGGER_Base import log
from cursor_del_pool import CursorDelPool
from Producto import Producto



class ProductoDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM producto ORDER BY id_producto'
    _INSERTAR = 'INSERT INTO producto(nombre_producto, descripcion_producto, precio_producto) VALUES(%s, %s, %s);'
    _ACTUALIZAR = 'UPDATE producto SET nombre_producto=%s, descripcion_producto=%s, precio_producto=%s WHERE id_producto=%s'
    _ELIMINAR = 'DELETE FROM producto WHERE id_producto=%s'
    _BUSCAR = 'SELECT * FROM producto WHERE id_producto=%s'
    _CONSULTA = 'select id_detalle_pedido_stock, (select nombre_ingrediente from ingrediente where id_ingrediente=detalle_pedido_stock.id_ingrediente), cantidad from  detalle_pedido_stock where id_pedido_stock = %s'
    _ID = 'SELECT id_producto from producto ORDER BY id_producto DESC LIMIT 1'
    _PRECIO = 'select precio_producto from producto WHERE id_producto = %s'


    @classmethod
    def precio(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.id_producto,)
            cursor.execute(cls._PRECIO, valores)
            registros = cursor.fetchone()
            for registro in registros:
                producto = registro

        return producto


    @classmethod
    def id(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ID)
            registros = cursor.fetchone()
            for registro in registros:
                producto = registro
            return producto







    @classmethod
    def buscar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.id_producto,)
            cursor.execute(cls._BUSCAR, valores)
            registros = cursor.fetchall()
            for registro in registros:
                producto = registro

        return producto

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3])
                productos.append(producto)
            return productos

    @classmethod
    def insertar(cls, productos):
        with CursorDelPool() as cursor:
            valores = (productos.nombre_producto, productos.descripcion_producto, productos.precio_producto)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {productos}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.nombre_producto, producto.descripcion_producto, producto.precio_producto, producto.id_producto)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {producto}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.id_producto,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{producto}')
            return cursor.rowcount

if __name__ == '__main__':
    pa = ProductoDAO.precio(Producto(id_producto=4013))
    print (pa)
