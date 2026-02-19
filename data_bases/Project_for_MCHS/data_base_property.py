import pymysql
from pony.orm import Database

db = Database()
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'db': 'MCHS_db'
}

def init_db(db: Database, provider='sqlite', file_name='MCHS.db') -> Database:
    if provider=='sqlite':
        db.bind(provider=provider, filename='MCHS.db', create_db=True)
        db.generate_mapping(create_tables=True)
        return db
    elif provider == 'mysql':
        create_database_if_not_exists()
        db.bind(
            provider='mysql',
            host=MYSQL_CONFIG['host'],
            user=MYSQL_CONFIG['user'],
            passwd=MYSQL_CONFIG['passwd'],
            db=MYSQL_CONFIG['db']
        )
        db.generate_mapping(create_tables=True)
        return db


def create_database_if_not_exists():
    # Подключаемся к MySQL без указания базы данных
    connection = pymysql.connect(
        host=MYSQL_CONFIG['host'],
        user=MYSQL_CONFIG['user'],
        password=MYSQL_CONFIG['passwd']
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_CONFIG['db']}")
        connection.commit()
    finally:
        connection.close()