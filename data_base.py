from os import waitid

import psycopg2
import base
# import copy_db
# import addons
import rename_db


database_params = {
    'dbname': 'odoo_17_base_test',
    'user': 'odoo17',
    'password': 'cool',
    'host': 'localhost',
    'port': '5432',
}


def execute_data(database_params):
    """
    Establishes a connection to the PostgreSQL database with the given parameters.
    Args:
        database_params (dict): A dictionary containing database connection parameters.
            - dbname (str): The name of the database.
            - user (str): The username to connect to the database.
            - password (str): The password to connect to the database.
            - host (str): The host where the database is running.
            - port (str): The port where the database is listening.
    Returns:
        psycopg2.extensions.connection: A connection object to the specified PostgreSQL database.
    """
    with psycopg2.connect(**database_params) as dest_conn:
        return dest_conn


if __name__ == "__main__":

    """
    Main block to execute database operations.
    - Establishes a connection to the database using `execute_data`.
    - Calls the `copy_database` function from the `copy_db` module to create a copy of the database.
    - Executes the `active_fun` function from the `base` module.
    - Calls the `update_product` function from the `addons.product_product.pre_migration` module to update product data.
    """

    data_cursor = execute_data(database_params)
    base.active_func()
    # addons.active_func()
    # rename_db.rename_database(database_params)
