from abc import ABCMeta, abstractmethod


class OrderDAO(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_order_list(self):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass

    @abstractmethod
    def insert_order(self, new_order):
        pass

    @abstractmethod
    def filter_orders(self, fulfilled):
        pass


class BasicDAO(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_list(self):
        pass
