from pymysql import IntegrityError
from utils import connect_to_db
from dao_classes import OrderDAO, BasicDAO


class OrderDaoImplMysql(OrderDAO):
    """
    This class all db function related to order table
    """

    def __init__(self):
        super().__init__()
        self._connection = connect_to_db()

    def get_order_list(self):
        """
        Function that gets the list of all orders
        """
        statement = "SELECT * from OrderList"
        result  = []
        if self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(statement)
                result = cursor.fetchall()
        return result

    def get_order(self, order_id):
        """
        Function to get a specific order
        """
        statement = "SELECT * from OrderList where OrderID = %d" % (order_id)
        result = ""
        if self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(statement)
                result = cursor.fetchone()
        return result

    def insert_order(self, new_order):
        """
        Function to place a new order
        """
        result = None
        if self._connection:
            with self._connection.cursor() as cursor:
                args = (
                    new_order.get_book_id(),
                    new_order.get_orderer_name(),
                    new_order.get_orderer_address(),
                    new_order.get_quantity(), 0)

                try:
                    # call the stored procedure
                    cursor.callproc("spNewOrder", args)
                    # commits the changes
                    self._connection.commit()
                    result = cursor.execute('SELECT @_spNewOrder_4')
                    result = cursor.fetchone()
                    result = result['@_spNewOrder_4']
                except IntegrityError:
                    # Exception to handle error thrown by foreign key constraint
                    print("Oops! It seems that you have enter wrong book id.")
                    print("Operation failed. Please try again!")
                except Exception:
                    print("Oops something went wrong. Please try again.")

        return result

    def filter_orders(self, fulfilled=True):
        """
        Function to retrive either fulfilled or unfulfilled order
        based on the <Fulfilled> column
        """
        if fulfilled:
            statement = "SELECT * from OrderList where Fulfilled = 1"
        else:
            statement = "SELECT * from OrderList where Fulfilled = 0"
        with self._connection.cursor() as cursor:
            cursor.execute(statement)
            result = cursor.fetchall()
        return result


class StockDaoImplMysql(BasicDAO):
    """
    This class handles db operations of StockList table
    """

    def __init__(self):
        super().__init__()
        self._connection = connect_to_db()

    def get_list(self):
        """
        Function to list all stock
        """
        statement = "SELECT * from StockList"
        result = []
        if self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(statement)
                result = cursor.fetchall()
        return result



class BackOrderDaoImplMysql(BasicDAO):
    """
    This function lists all operations related to backorder table
    """

    def __init__(self):
        super().__init__()
        self._connection = connect_to_db()

    def get_list(self):
        """
        Function to list all back orders
        """
        statement = "SELECT * from BackOrderList"
        result = []
        if self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(statement)
                result = cursor.fetchall()
        return result
