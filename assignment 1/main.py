"""
   PLEASE MAKE SURE TO UPDATE THE CREDENTIALS IN SETTINGS.PY

"""

import os
from xmlrpc.client import Boolean

from order import Order
from daofactory import DAOFactory


def display_menu() -> None:
    """
    This function displays the menu
    """
    print("Please choose an option to continue: ")
    print("\t1. Place a new order")
    print("\t2. View current orders")
    print("\t3. View all back orders")
    print("\t4. View stock list")
    print("\t5. View all fulfilled orders")
    print("\t6. View all unfulfilled orders")
    print("\t0. Exit")


def place_new_order() -> None:
    """
    This function displays the current stock list,
    get new order data and place a new order
    """
    print("STOCK LIST:\n")
    display_stock_list()

    print("\nEnter your order details:")
    book_id = input("\tEnter the book id: ")
    while not book_id.isdigit():
        print("\tThat's not a valid input. Please try again.")
        book_id = input("\tEnter the book id: ")
    orderer_name = input("\tEnter the orderer name: ")
    orderer_address = input("\tEnter the orderer address: ")
    quantity = input("\tEnter the quantity: ")
    while not quantity.isdigit():
        print("\tThat's not a valid input. Please try again.")
        quantity = input("\tEnter the quantity: ")

    order_obj = Order(
        book_id=book_id,
        orderer_name=orderer_name,
        orderer_address=orderer_address,
        quantity=quantity)
    order_sql_obj =  DAOFactory.get_order_dao("MYSQL")
    result = order_sql_obj.insert_order(order_obj)
    if result == 1:
        print("Order completed!!")
    elif result == 0:
        print("Order unfulfilled!!")


def display_current_orders() -> None:
    """"
    This function list all current orders
    """
    order_sql_obj =  DAOFactory.get_order_dao("MYSQL")
    orders = order_sql_obj.get_order_list()
    print("Order ID\tBook ID\t\tOrderer name\t\
        Orderer Address\t\tQuantity\tFulfulled")
    for order in orders:
        print("{:<15} {:<15} {:<23} {:<23} {:<15} {:<23}".format(
            order["OrderID"], order["BookID"],order["OrdererName"],
            order["OrdererAddress"],order["Quantity"], order["Fulfilled"]))


def display_back_orders() -> None:
    """
    This function lists call back orders
    """
    back_order_sql_obj =  DAOFactory.get_back_order_dao("MYSQL")
    back_orders = back_order_sql_obj.get_list()
    print("Back Order ID\t\tOrder ID\tQuantity\t")
    for back_order in back_orders:
        print("{:<23} {:<15} {:<15}".format(
        back_order["BackOrderID"], back_order["OrderID"],back_order["Quantity"]))


def display_stock_list() -> None:
    """
    This function lists all stock
    """
    stock_sql_obj = DAOFactory.get_stock_dao("MYSQL")
    stocks = stock_sql_obj.get_list()
    print("Book ID\t\tBook Titile\t\tAuthor\t\tQuantity In Stock")
    for stock in stocks:
        print("{:<15} {:<23} {:<15} {:<23}".format(
            stock["BookID"],stock["BookTitle"],
            stock["Author"],stock["QuantityInStock"]))


def display_filters_orders(fulfilled: Boolean) -> None:
    """
    This function filters order based on fulfilled column
    """
    order_sql_obj =  DAOFactory.get_order_dao("MYSQL")

    if fulfilled:
        orders = order_sql_obj.filter_orders(True)
    else:
        orders = order_sql_obj.filter_orders(False)

    print("Order ID\tBook ID\t\tOrderer name\t\
        Orderer Address\t\tQuantity")
    for order in orders:
        print("{:<15} {:<15} {:<23} {:<23} {:<15}".format(
            order["OrderID"], order["BookID"],order["OrdererName"],
            order["OrdererAddress"],order["Quantity"]))


def orchestrator(choice: int) -> None:
    """
    This function calls function based on user input
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == '1':
        place_new_order()
    elif choice == '2':
        display_current_orders()
    elif choice == '3':
        display_back_orders()
    elif choice == '4':
        display_stock_list()
    elif choice == '5':
        display_filters_orders(True)
    elif choice == '6':
        display_filters_orders(False)
    elif choice == '0':
        exit()
    else:
        print("Invalid choice!!")
    print("\nPress enter to continue.")
    input()


def main() -> None:
    """
    The main function
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()
        choice=input()
        orchestrator(choice)


if __name__ == "__main__":
    main()
