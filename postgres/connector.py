import psycopg2
from config_parser import config


def connect():
    """Connect to Postgres DB server"""
    conn = None
    try:
        # read connection parameters
        params = config()

        #connect to Postgres server
        print("connecting to postgres database")
        conn = psycopg2.connect(**params)

        #create cursor
        cur = conn.cursor()

        #execute statement
        print('postgres db version')
        cur.execute('SELECT version()')

        #display verison
        db_version = cur.fetchone()
        print(db_version)

        #close comm with postgres
        cur.close()

    except (Exception, psycopg2.DataError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("db closed")

if __name__=="__main__":
    connect()

