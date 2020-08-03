from os import getenv


def get_source():
    return {
        'driver': 'ODBC Driver 17 for SQL Server',
        'server': getenv('SRC_HOST'),
        'database': getenv('SRC_DATABASE'),
        'user': getenv('SRC_USER'),
        'password': getenv('SRC_PASS'),
        'autocommit': False
    }


def get_target():
    environment = getenv('ENVIRONMENT', 'development')
    if environment == 'production':
        return {
            'host': getenv('TGT_HOST'),
            'database': getenv('TGT_DATABASE'),
            'user': getenv('TGT_USER'),
            'password': getenv('TGT_PASS')
        }
    return {
        'host': 'localhost',
        'database': 'test_db',
        'user': 'test_user',
        'password': 'somesecret'
    }
