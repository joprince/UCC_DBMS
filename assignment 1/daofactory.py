from mysql_classes import OrderDaoImplMysql, BackOrderDaoImplMysql, StockDaoImplMysql


class DAOFactory(object):
    @staticmethod
    def get_order_dao(daotype):
        if daotype.upper() == "MYSQL":
            return OrderDaoImplMysql()

    @staticmethod
    def get_back_order_dao(daotype):
        if daotype.upper() == "MYSQL":
            return BackOrderDaoImplMysql()

    @staticmethod
    def get_stock_dao(daotype):
        if daotype.upper() == "MYSQL":
            return StockDaoImplMysql()
