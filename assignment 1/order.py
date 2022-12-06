class Order(object):

    """
    This class handles the new orders placed
    """

    def __init__(
        self, book_id, orderer_name,
        orderer_address, quantity, order_id=None) -> None:
        self._order_id = order_id
        self._book_id = book_id
        self._orderer_name =orderer_name
        self._orderer_address = orderer_address
        self._quantity = quantity

    def get_order_id(self) -> int:
        return self._order_id

    def get_book_id(self) -> int:
        return self._book_id

    def get_orderer_name(self) -> str:
        return self._orderer_name

    def get_orderer_address(self) -> str:
        return self._orderer_address

    def get_quantity(self) -> int:
        return self._quantity
