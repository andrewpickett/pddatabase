from contextlib import contextmanager

from mysql.connector import pooling, DatabaseError

from pddatabase_config import pddatabase_config

dbconfig = {
    "database": pddatabase_config['mysql']['schema'],
    "user": pddatabase_config['mysql']['username'],
    "password": pddatabase_config['mysql']['password'],
    "host": pddatabase_config['mysql']['host'],
    "autocommit": pddatabase_config['mysql']['autocommit']
}

db_pool = pooling.MySQLConnectionPool(pool_name=pddatabase_config['mysql']['pool_name'],
                                      pool_size=pddatabase_config['mysql']['pool_size'],
                                      **dbconfig)


@contextmanager
def open_db_connection():
    connection = db_pool.get_connection()
    cursor = connection.cursor(prepared=True)
    try:
        yield cursor
    except DatabaseError:
        if cursor:
            cursor.execute("ROLLBACK")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    if not dbconfig["autocommit"]:
        cursor.execute("COMMIT")
