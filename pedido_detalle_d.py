from LOGGER_Base import log
from Pedido import Pedido
from cursor_del_pool import CursorDelPool
from Detalle_Pedido import Detalle_Pedido
from todotable import TodoP


class Detalle_PedidoDAO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM pedido_stock ORDER BY id_pedido_stock'
    _INSERTAR = 'INSERT INTO detalle_pedido_stock(id_pedido_stock ,id_ingrediente, cantidad) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE detalle_pedido_stock SET id_pedido_stock=%s, id_ingrediente=%s, cantidad=%s WHERE id_ingrediente=%s'
    _ELIMINAR = 'DELETE FROM detalle_pedido_stock WHERE id_detalle_pedido_stock=%s'
    _BUSCAR = 'SELECT * FROM detalle_pedido_stock WHERE id_ingrediente=%s'
    _CONSULTA = 'select id_detalle_pedido_stock, (select nombre_ingrediente from ingrediente where id_ingrediente=detalle_pedido_stock.id_ingrediente), cantidad from  detalle_pedido_stock where id_pedido_stock = %s'
    _FILTRO = 'SELECT (select nombre_ingrediente from ingrediente where id_ingrediente=detalle_pedido_stock.id_ingrediente), cantidad from detalle_pedido_stock where id_pedido_stock=%s'




    def filtro(cls, detalle_pedido):
         with CursorDelPool() as cursor:
          valores = (detalle_pedido.id_PStock,)
          cursor.execute(cls._FILTRO, valores)
          registros = cursor.fetchall()
          lista = []
          for registro in registros:
              ped = Detalle_Pedido(registro[0], registro[1])
              print(ped)
              lista.append(ped)
          return lista


    @classmethod
    def buscar(cls, detalle_pedido):
        with CursorDelPool() as cursor:
         valores = (detalle_pedido.id_INGD,)
         cursor.execute(cls._BUSCAR, valores)
         registros = cursor.fetchall()
         for registro in registros:
             detalle_pedido = registro

        return detalle_pedido



    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            dpedidos = []
            for registro in registros:
                detalle_pedido = Detalle_Pedido(registro[0], registro[1], registro[2])
                dpedidos.append(detalle_pedido)
            return dpedidos

    @classmethod
    def insertar(cls, detalle_pedido):
        with CursorDelPool() as cursor:
            valores = (detalle_pedido.id_PStock, detalle_pedido.id_INGD, detalle_pedido.cant_i)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {detalle_pedido}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, detalle_pedido):
        with CursorDelPool() as cursor:
            valores = (detalle_pedido.id_PStock, detalle_pedido.id_INGD, detalle_pedido.cant_i, detalle_pedido.id_INGD)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {detalle_pedido}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, detalle_pedido):
        with CursorDelPool() as cursor:
            valores = (detalle_pedido.id_detalle_pedido,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{detalle_pedido}')
            return cursor.rowcount


