from LOGGER_Base import log
from Conexion import Con
class CursorDelPool:
    def __init__(self):
        self._con = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo whit __enter__')
        self._con = Con.obtenerCon()
        self._cursor = self._con.cursor()
        return self._cursor


    def __exit__(self, tipo_exepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._con.rollback()
            log.error(f'Ocurrio una exepcion:{valor_excepcion} {tipo_exepcion} {detalle_excepcion}')
        else:
            self._con.commit()
            log.debug('Commit de la transaccion')

        self._cursor.close()
        Con.liberarCon(self._con)


if __name__ == '__main__':

    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM empleado')
        log.debug(cursor.fetchall())