from LOGGER_Base import log
from cursor_del_pool import CursorDelPool
from Producto_detalle import Producto_Detalle



class Producto_detalleDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR1 = 'SELECT * FROM receta_producto ORDER BY id_receta_producto'
    _SELECCIONAR = 'SELECT id_receta_producto,(select ingrediente.nombre_ingrediente from ingrediente where id_ingrediente = receta_producto.id_ingrediente), cantidad FROM receta_producto WHERE id_producto=%s'
    _INSERTAR = 'INSERT INTO receta_producto(id_producto, id_ingrediente, cantidad) VALUES(%s, %s, %s);'
    _ACTUALIZAR = 'UPDATE receta_producto SET cantidad=%s WHERE id_receta_producto=%s'
    _ELIMINAR = 'DELETE FROM receta_producto WHERE id_receta_producto=%s'
    _BUSCAR = 'SELECT * FROM receta_producto WHERE id_producto=%s'
    _CONSULTA ='select (select ingrediente.nombre_ingrediente from ingrediente where id_ingrediente = receta_producto.id_ingrediente), cantidad from receta_producto where id_producto =%s'
    _ID = 'SELECT id_producto from producto ORDER BY id_producto DESC LIMIT 1'


    @classmethod
    def seleccionar1(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR1)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto_Detalle(registro[0], registro[1], registro[2], registro[3])
                productos.append(producto)
            return productos

    @classmethod
    def buscar(cls, producto_detalle):
        with CursorDelPool() as cursor:
            valores = (producto_detalle.id_producto_detalle,)
            cursor.execute(cls._BUSCAR, valores)
            registros = cursor.fetchall()
            for registro in registros:
                producto = registro

        return producto

    @classmethod
    def seleccionar(cls, producto_detalle):
        with CursorDelPool() as cursor:
            valores = (producto_detalle.id_producto_,)
            cursor.execute(cls._SELECCIONAR, valores)
            registros = cursor.fetchall()
            lista = []
            for registro in registros:
                ped = Producto_Detalle(registro[0], registro[1], registro[2])
                print(ped)
                lista.append(ped)
            return lista

    @classmethod
    def insertar(cls, producto_detalle):
        with CursorDelPool() as cursor:
            valores = (producto_detalle.id_producto_, producto_detalle.id_ingrediente_receta, producto_detalle.cantidad_receta)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {producto_detalle}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, producto_detalle):
        with CursorDelPool() as cursor:
            valores = (producto_detalle.cantidad_receta, producto_detalle.id_producto_detalle)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {producto_detalle}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, producto_detalle):
        with CursorDelPool() as cursor:
            valores = (producto_detalle.id_producto_detalle,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{producto_detalle}')
            return cursor.rowcount
    @classmethod
    def consulta(cls, producto_detalle):
         with CursorDelPool() as cursor:
          valores = (producto_detalle.id_producto_,)
          cursor.execute(cls._CONSULTA, valores)
          registros = cursor.fetchall()
          lista = []
          for registro in registros:
              ped = Producto_Detalle(registro[0], registro[1])
              print(ped)
              lista.append(ped)
          return lista

    @classmethod
    def id(cls):
            with CursorDelPool() as cursor:
                cursor.execute(cls._ID)
                registros = cursor.fetchone()
                for registro in registros:
                    pedido = registro
                return pedido

if __name__ == '__main__':

    pa =Producto_detalleDAO.seleccionar(Producto_Detalle(id_producto_=4013))
    print(pa)
