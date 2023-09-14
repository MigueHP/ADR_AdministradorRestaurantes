from Conexion import Con
from LOGGER_Base import log
from Proveedor import Proveedor
from cursor_del_pool import CursorDelPool


class ProveedorDaO:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM proveedores ORDER BY id_proveedor'
    _INSERTAR = 'INSERT INTO proveedores(nombre_proveedor, telefono_proveedor, direccion_proveedor) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE proveedores SET nombre_proveedor=%s, telefono_proveedor=%s, direccion_proveedor=%s WHERE id_proveedor=%s'
    _ELIMINAR = 'DELETE FROM proveedores WHERE id_proveedor=%s'
    _BUSCAR = 'SELECT * FROM proveedores WHERE id_proveedor=%s'

    @classmethod
    def buscar(cls, proveedor):
        with CursorDelPool() as cursor:
         valores = (proveedor.id_proveedor,)
         cursor.execute(cls._BUSCAR, valores)
         registros = cursor.fetchall()
         for registro in registros:
             proveedor = registro

        return proveedor

    @classmethod
    def seleccionar_2(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            proveedores = []
            for registro in registros:
                proveedor = Proveedor(registro[0], registro[1])
                proveedores.append(proveedor)
            return proveedores

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            proveedores = []
            for registro in registros:
                proveedor = Proveedor(registro[0], registro[1], registro[2], registro[3])
                proveedores.append(proveedor)
            return proveedores

    @classmethod
    def insertar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.nombre_proveedor, proveedor.telefono_proveedor, proveedor.dire_proveedor)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {proveedor}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.nombre_proveedor, proveedor.telefono_proveedor, proveedor.dire_proveedor, proveedor.id_proveedor)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {proveedor}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.id_proveedor,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{proveedor}')
            return cursor.rowcount



if __name__ == '__main__':
    # Insertar registro

    empleado1 = Proveedor(id_proveedor=1001, nombre_proveedor='Carnes la ultima Lucha', telefono_proveedor=3338414118,
                          dire_proveedor='Sierra mojada 336')
    empleados_insertados = ProveedorDaO.insertar(empleado1)
   # empleado1 = Empleado(id_empleado=1002, nombre_empleado='Pedro Moreno', rol_empleado='Cocinero',
    #                     curp_empleado='HEPMPMWMWD', rfc_empleado='HEPMWDOMDW', domicilio_empleado='Federalismo 233',
                       # telefono_empleado='333698546')
    #empleados_insertados = EmpleadoDao.insertar(empleado1)
    log.debug(f'Personas insertadas {empleados_insertados}')

    # Actualizar registro
    # empleado1 = Empleado(1003,'Alejandra Tellez','Mesero','APELEPLS','hepm1012','Jose ma. Rodriguez','38240266')
    # empleado_actualizados = EmpleadoDao.actualizar(empleado1)
    # log.debug(f'Personas actualizadas: {empleado_actualizados}')

       #ELIMINAR REGISTRO
        #empleado1 = Empleado(id_empleado=1001)
        #personas_eliminadas = EmpleadoDao.buscar(empleado1)
        #log.debug(F'Personas eliminadas : {personas_eliminadas}')