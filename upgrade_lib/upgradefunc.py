import data_base
import console


def execute_query(conn, query, success_message, warning_message):
    """
    Executes a given SQL query and logs the result.

    Args:
        conn: The database connection object.
        query (str): The SQL query to execute.
        success_message (str): The message to log upon successful execution.
        warning_message (str): The message to log upon an exception.
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query)
            conn.commit()
            console.logger.info(success_message, extra={'log_type': 'INFO'})
        except Exception as e:
            console.logger.info(f"{warning_message}: {e}", extra={'log_type': 'Warning'})


def change_data_type(table, column):
    """
    Changes the data type of a specified column in a table to JSONB.

    Args:
        table (str): The name of the table to be altered.
        column (str): The name of the column whose data type needs to be changed.
    """
    conn = data_base.execute_data(data_base.database_params)

    create_column = f"ALTER TABLE {table} ADD COLUMN {column}_new JSONB;"
    execute_query(conn, create_column,
                  f"{table} altered with column {column}_new with type JSONB",
                  "Failed to add new JSONB column")

    change_data = f"UPDATE {table} SET {column}_new = jsonb_build_object('en_US', {column});"
    execute_query(conn, change_data,
                  f"Updated {table} with {column}_new = jsonb_build_object('en_US', {column})",
                  "Failed to update new column with JSONB data")

    drop_column = f"ALTER TABLE {table} DROP COLUMN {column};"
    execute_query(conn, drop_column,
                  f"Dropped {column} from {table}",
                  "Failed to drop original column")

    rename_column = f"ALTER TABLE {table} RENAME COLUMN {column}_new TO {column};"
    execute_query(conn, rename_column,
                  f"Renamed column {column}_new to {column} in {table}",
                  "Failed to rename new column to original column name")


def rename_field_name(table, column,new_column):
    """
    Renames a specified column in a table to 'partner_id'.

    Args:
        table (str): The name of the table to be altered.
        column (str): The name of the column to be renamed.
    """
    conn = data_base.execute_data(data_base.database_params)
    query = f"ALTER TABLE {table} RENAME COLUMN {column} TO {new_column};"
    execute_query(conn, query,
                  f"Renamed column {column} to {new_column} in {table}",
                  "Failed to rename column")


def drop_column(table, column):
    """
    Drops a specified column from a table.

    Args:
        table (str): The name of the table to be altered.
        column (str): The name of the column to be dropped.
    """
    conn = data_base.execute_data(data_base.database_params)
    query = f"ALTER TABLE {table} DROP COLUMN {column};"
    execute_query(conn, query,
                  f"Dropped column {column} from {table}",
                  "Failed to drop column")


def Add_column(table, column, data_type):
    """
    Adds a new column to a specified table with the given data type.

    Args:
        table (str): The name of the table to be altered.
        column (str): The name of the column to be added.
        data_type (str): The data type of the new column.
    """
    conn = data_base.execute_data(data_base.database_params)
    query = f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {column} {data_type};"
    execute_query(conn, query,
                  f"Column {column} added to {table}",
                  "Failed to add column")

