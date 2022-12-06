import pymysql
import settings

def connect_to_db():
    """
    A util function that connects to the DB
    """
    connection = None
    try:
        connection = pymysql.connect(host=settings.HOST,
                                user=settings.USER,
                                password=settings.PASSWORD,
                                db=settings.DB,
                                charset=settings.CHARSET,
                                cursorclass=pymysql.cursors.DictCursor)
    except Exception:
        print("Something went wrong while connecting to database...")
        print("Transaction unsuccessful!!")
        exit()
    return connection