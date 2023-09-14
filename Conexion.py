
from psycopg2 import pool
from LOGGER_Base import log
import sys

class Con:
    _DATABASE = 'ADR System'
    _USERNAME = 'postgres'
    _PASSWORD = 'emmanuel'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None


    @classmethod
    def obtenerPool(cls):
     if cls._pool is None:
        try:
            cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
            log.debug(f'Creacion de pool exitosa: {cls._pool}')
            return cls._pool

        except Exception as e:
            log.error(f'Ocurrio un error al obtener pool {e}')
            sys.exit()

     else:
            return cls._pool

    @classmethod
    def obtenerCon(cls):
     conexion = cls.obtenerPool().getconn()
     log.debug(f'Conexion obtenida del pool: {conexion}')
     return conexion

    @classmethod
    def liberarCon(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regrsamos conexion al pool: {conexion}')

    @classmethod
    def cerrarCon(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':


     cone1 = Con.obtenerCon()
     Con.liberarCon(cone1)
     cone2 = Con.obtenerCon()
     cone3  = Con.obtenerCon()

