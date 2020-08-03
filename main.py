import psycopg2
import pyodbc

from src.db_credentials import get_source, get_target
from src.services.log import log
from src.services.slack_integration import SlackPost


def main():
    try:
        log.info('Connecting to target URI...')
        target = get_target()
        target_cnx = psycopg2.connect(**target)
        target_cursor = target_cnx.cursor()
        log.info('Closing target connection...')
        target_cursor.close()
        target_cnx.close()
        log.info('Connecting to source URI...')
        source = get_source()
        source_cnx = pyodbc.connect(**source)
        source_cursor = source_cnx.cursor()
        source_cursor.close()
        source_cnx.close()
        log.info('Closing source connection...')
        log.info('Process finished with success!')
    except Exception as error:
        log.exception(str(error))
        slack = SlackPost()
        slack.send_message(str(error))


if __name__ == "__main__":
    main()
