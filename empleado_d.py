from Conexion import Con
from Empleado import Empleado
from Proveedor import Proveedor
from LOGGER_Base import log
from cursor_del_pool import CursorDelPool



class EmpleadoDao:
    '''
    DAO (Data Acces Object)
    CRUD (Created-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre_empleado, rol_empleado, curp_empleado, rfc_empleado, domicilio_empleado, telefono_empleado) VALUES(%s,%s,%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre_empleado=%s, rol_empleado=%s, curp_empleado=%s, rfc_empleado=%s, domicilio_empleado=%s,telefono_empleado=%s WHERE id_empleado=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE id_empleado=%s'
    _BUSCAR = 'SELECT * FROM empleado WHERE id_empleado=%s'



    @classmethod
    def buscar(cls, empleado):
        with CursorDelPool() as cursor:
         valores = (empleado.id_empleado,)
         cursor.execute(cls._BUSCAR,valores)
         registros = cursor.fetchall()
         for registro in registros:
             empleado = registro

        return empleado






    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for registro in registros:
                empleado = Empleado(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                                    registro[6])
                empleados.append(empleado)
            return empleados

    @classmethod
    def insertar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre_empleado, empleado.rol_empleado, empleado.curp_empleado,
                       empleado.rfc_empleado, empleado.domicilio_empleado, empleado.telefono_empleado)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {empleado}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.nombre_empleado, empleado.rol_empleado, empleado.curp_empleado, empleado.rfc_empleado,
                       empleado.domicilio_empleado, empleado.telefono_empleado, empleado.id_empleado)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada {empleado}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.id_empleado,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado:{empleado}')
            return cursor.rowcount

if __name__ == '__main__':
    empleado1 = Empleado(id_empleado=1)
    personas_eliminadas = EmpleadoDao.eliminar(empleado1)
    log.debug(F'Personas eliminadas : {personas_eliminadas}')




