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


def _rename_model(table, column, data, condition_column, operation_type, condition):
    """
       Update records in a specified table in the database.

       Parameters:
       table (str): The name of the table to update.
       column (str): The column to update.
       data (str/int/float): The new data to set in the specified column.
       condition_column (str): The column used to determine which rows to update.
       operation_type (str): The operation type for the condition (e.g., '=', '>', '<', etc.).
       condition (str/int/float): The value to compare against the condition column.

       Returns:
       None
       """
    conn = data_base.execute_data(data_base.database_params)
    update_model_name = f"UPDATE {table} SET {column} = '{data}' WHERE {condition_column} {operation_type} '{condition}';"
    update_model_data = f"UPDATE ir_model_data SET model = '{data}' WHERE model = '{condition}';"
    update_model_field = f"UPDATE ir_model_fields SET model = '{data}' WHERE model = '{condition}';"
    update_ir_attachment = f"UPDATE ir_attachment SET res_model = '{data}' WHERE res_model = '{condition}';"
    update_ir_filters = f"UPDATE ir_filters SET model_id = '{data}' WHERE model_id = '{condition}';"

    execute_query(conn, update_model_name,
                  f"Data converted to {data} from table {table}",
                  f"Failed to update data {data}")

    execute_query(conn, update_model_data,
                  f"Data updated to {data} from table {table}",
                  f"Failed to update data {data}"
                  )

    execute_query(conn, update_model_field,
                  f"Data updated to {data} from table {table}",
                  f"Failed to update data {data}"
                  )
    execute_query(conn, update_ir_attachment,
                  f"Data updated to {data} from table {table}",
                  f"Failed to update data {data}"
                  )
    execute_query(conn, update_ir_filters,
                  f"Data updated to {data} from table {table}",
                  f"Failed to update data {data}"
                  )


def rename_table(old_table_name, new_table_name):
    """
    Rename a table in the database.

    This function renames a table in the database by executing an ALTER TABLE SQL query.

    Parameters:
    old_table_name (str): The current name of the table.
    new_table_name (str): The new name for the table.

    Returns:
    None
    """
    # Assuming data_base.execute_data and execute_query functions are properly defined elsewhere

    # Initialize database connection
    conn = data_base.execute_data(data_base.database_params)

    # Define SQL queries
    query = f"ALTER TABLE {old_table_name} RENAME TO {new_table_name};"
    update_model_data_name = (f"UPDATE ir_model_data SET name='model_{new_table_name}' "
                              f"WHERE name='model_{old_table_name}' AND model = 'ir.model';")

    # Execute SQL queries
    execute_query(conn, query,
                  f"Table renamed from {old_table_name} to {new_table_name}",
                  f"Failed to rename table from {old_table_name} to {new_table_name}")

    execute_query(conn, update_model_data_name,
                  f"Data updated from {old_table_name} to {new_table_name}",
                  f"Failed to update data from {old_table_name} to {new_table_name}")


def drop_model(model):
    """
    Drops a specific model from the 'ir_model' table in the database.

    Parameters:
    model (str): The name of the model to be removed.

    This function creates a connection to the database and executes a DELETE SQL query
    to remove the model from the 'ir_model' table. Logs a success message if the model
    is removed successfully, or an error message if the removal fails.
    """
    conn = data_base.execute_data(data_base.database_params)
    remove_model = f"""DELETE FROM ir_model WHERE model = '{model}';"""
    remove_action = f"""DELETE FROM ir_act_window WHERE res_model = '{model}';"""
    remove_field = f"""DELETE FROM ir_model_fields WHERE relation = '{model}';"""
    remove_access = f"""DELETE FROM ir_model_access WHERE name = 'access.{model}';"""
    execute_query(conn, remove_model,
                  f"Model removed from ir_model where name contains {model}",
                  f"Failed to remove {model} model from ir_model")
    execute_query(conn, remove_action,
                  f"action removed from ir_act_window where res_model contains {model}",
                  f"Failed to remove action from {model} model contains ir_act_window ")
    execute_query(conn, remove_field,
                  f"field removed from ir_model_fields where model contains {model}",
                  f"Failed to remove field from {model} model contains ir_model_fields")
    execute_query(conn, remove_access,
                  f"access removed from ir_model_access where name contains access.{model}",
                  f"Failed to remove access for access.{model} model contains ir_model_access")
