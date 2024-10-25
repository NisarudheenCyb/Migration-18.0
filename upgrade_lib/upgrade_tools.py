import data_base
import console


class DatabaseMigrationTool:

    @staticmethod
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
                console.logger.warning(f"{warning_message}: {e}", extra={'log_type': 'Warning'})

    @staticmethod
    def rename_model(table, column, data, condition_column, operation_type, condition):
        """
        Update records in a specified table in the database.
        """
        conn = data_base.execute_data(data_base.database_params)
        update_model_name = f"UPDATE {table} SET {column} = '{data}' WHERE {condition_column} {operation_type} '{condition}';"
        update_model_data = f"UPDATE ir_model_data SET model = '{data}' WHERE model = '{condition}';"
        update_model_field = f"UPDATE ir_model_fields SET model = '{data}' WHERE model = '{condition}';"
        update_ir_attachment = f"UPDATE ir_attachment SET res_model = '{data}' WHERE res_model = '{condition}';"
        update_ir_filters = f"UPDATE ir_filters SET model_id = '{data}' WHERE model_id = '{condition}';"

        DatabaseMigrationTool.execute_query(conn, update_model_name,
                                              f"Data converted to {data} from table {table}",
                                              f"Failed to update data {data}")
        DatabaseMigrationTool.execute_query(conn, update_model_data,
                                              f"Data updated to {data} from table {table}",
                                              f"Failed to update data {data}")
        DatabaseMigrationTool.execute_query(conn, update_model_field,
                                              f"Data updated to {data} from table {table}",
                                              f"Failed to update data {data}")
        DatabaseMigrationTool.execute_query(conn, update_ir_attachment,
                                              f"Data updated to {data} from table {table}",
                                              f"Failed to update data {data}")
        DatabaseMigrationTool.execute_query(conn, update_ir_filters,
                                              f"Data updated to {data} from table {table}",
                                              f"Failed to update data {data}")

    @staticmethod
    def rename_table(old_table_name, new_table_name):
        """
        Rename a table in the database.
        """
        conn = data_base.execute_data(data_base.database_params)
        query = f"ALTER TABLE {old_table_name} RENAME TO {new_table_name};"
        update_model_data_name = (f"UPDATE ir_model_data SET name='model_{new_table_name}' "
                                  f"WHERE name='model_{old_table_name}' AND model = 'ir.model';")

        DatabaseMigrationTool.execute_query(conn, query,
                                              f"Table renamed from {old_table_name} to {new_table_name}",
                                              f"Failed to rename table from {old_table_name} to {new_table_name}")
        DatabaseMigrationTool.execute_query(conn, update_model_data_name,
                                              f"Data updated from {old_table_name} to {new_table_name}",
                                              f"Failed to update data from {old_table_name} to {new_table_name}")

    @staticmethod
    def drop_model(model):
        """
        Drops a specific model from the 'ir_model' table in the database.
        """
        conn = data_base.execute_data(data_base.database_params)
        remove_model = f"DELETE FROM ir_model WHERE model = '{model}';"
        remove_action = f"DELETE FROM ir_act_window WHERE res_model = '{model}';"
        remove_field = f"DELETE FROM ir_model_fields WHERE relation = '{model}';"
        remove_access = f"DELETE FROM ir_model_access WHERE name = 'access.{model}';"

        DatabaseMigrationTool.execute_query(conn, remove_model,
                                              f"Model removed from ir_model where name contains {model}",
                                              f"Failed to remove {model} model from ir_model")
        DatabaseMigrationTool.execute_query(conn, remove_action,
                                              f"Action removed from ir_act_window where res_model contains {model}",
                                              f"Failed to remove action for {model} model in ir_act_window")
        DatabaseMigrationTool.execute_query(conn, remove_field,
                                              f"Field removed from ir_model_fields where model contains {model}",
                                              f"Failed to remove field for {model} model in ir_model_fields")
        DatabaseMigrationTool.execute_query(conn, remove_access,
                                              f"Access removed from ir_model_access where name contains access.{model}",
                                              f"Failed to remove access for access.{model} model in ir_model_access")

    @staticmethod
    def change_data_type(table, column):
        """
        Changes the data type of a specified column in a table to JSONB.

        Args:
            table (str): The name of the table to be altered.
            column (str): The name of the column whose data type needs to be changed.
        """
        conn = data_base.execute_data(data_base.database_params)

        create_column = f"ALTER TABLE {table} ADD COLUMN {column}_new JSONB;"
        DatabaseMigrationTool.execute_query(conn, create_column,
                                              f"{table} altered with column {column}_new with type JSONB",
                                              "Failed to add new JSONB column")

        change_data = f"UPDATE {table} SET {column}_new = jsonb_build_object('en_US', {column});"
        DatabaseMigrationTool.execute_query(conn, change_data,
                                              f"Updated {table} with {column}_new = jsonb_build_object('en_US', {column})",
                                              "Failed to update new column with JSONB data")

        drop_column = f"ALTER TABLE {table} DROP COLUMN {column};"
        DatabaseMigrationTool.execute_query(conn, drop_column,
                                              f"Dropped {column} from {table}",
                                              "Failed to drop original column")

        rename_column = f"ALTER TABLE {table} RENAME COLUMN {column}_new TO {column};"
        DatabaseMigrationTool.execute_query(conn, rename_column,
                                              f"Renamed column {column}_new to {column} in {table}",
                                              "Failed to rename new column to original column name")

    @staticmethod
    def rename_field_name(table, column, new_column):
        """
        Renames a specified column in a table to a new name.

        Args:
            table (str): The name of the table to be altered.
            column (str): The name of the column to be renamed.
            new_column (str): The new name for the column.
        """
        conn = data_base.execute_data(data_base.database_params)
        query = f"ALTER TABLE {table} RENAME COLUMN {column} TO {new_column};"
        DatabaseMigrationTool.execute_query(conn, query,
                                              f"Renamed column {column} to {new_column} in {table}",
                                              "Failed to rename column")

    @staticmethod
    def drop_column(table, column):
        """
        Drops a specified column from a table.

        Args:
            table (str): The name of the table to be altered.
            column (str): The name of the column to be dropped.
        """
        conn = data_base.execute_data(data_base.database_params)
        query = f"ALTER TABLE {table} DROP COLUMN {column};"
        DatabaseMigrationTool.execute_query(conn, query,
                                              f"Dropped column {column} from {table}",
                                              "Failed to drop column")

    @staticmethod
    def add_column(table, column, data_type):
        """
        Adds a new column to a specified table with the given data type.

        Args:
            table (str): The name of the table to be altered.
            column (str): The name of the column to be added.
            data_type (str): The data type of the new column.
        """
        conn = data_base.execute_data(data_base.database_params)
        query = f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {column} {data_type};"
        DatabaseMigrationTool.execute_query(conn, query,
                                              f"Column {column} added to {table}",
                                              "Failed to add column")
