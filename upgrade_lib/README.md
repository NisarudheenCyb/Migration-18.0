This module provides a set of functions to manage and manipulate database tables and their columns.
Each function interacts with the database to perform specific operations like
updating records, renaming tables, altering columns, and more.
Below are the detailed descriptions of each function:
________________________________________________________________________________________________________
    _rename_model
    _rename_model in a specified table based on a condition.

Parameters:

    table (str): The name of the table to update.
    column (str): The column to update.
    data (str/int/float): The new data to set in the specified column.
    condition_column (str): The column used to determine which rows to update.
    operation_type (str): The operation type for the condition (e.g., '=', '>', '<', etc.).
    condition (str/int/float): The value to compare against the condition column.
________________________________________________________________________________________________________

    rename_table
    Renames a table in the database.

Parameters:

    old_table_name (str): The current name of the table.
    new_table_name (str): The new name for the table.
________________________________________________________________________________________________________

    execute_query
    Executes a given SQL query and logs the result.
Parameters:

    conn: The database connection object.
    query (str): The SQL query to execute.
    success_message (str): The message to log upon successful execution.
    warning_message (str): The message to log upon an exception.
________________________________________________________________________________________________________
    change_data_type
    Changes the data type of a specified column in a table to JSONB.

Parameters:

    table (str): The name of the table to be altered.
    column (str): The name of the column whose data type needs to be changed.
________________________________________________________________________________________________________

    rename_field_name
    Renames a specified column in a table to a new column name.

Parameters:

    table (str): The name of the table to be altered.
    column (str): The name of the column to be renamed.
    new_column (str): The new name for the column.

________________________________________________________________________________________________________
    drop_column
    Drops a specified column from a table.

Parameters:

    table (str): The name of the table to be altered.
    column (str): The name of the column to be dropped.
________________________________________________________________________________________________________
    Add_column
    Adds a new column to a specified table with the given data type.
Parameters:

    table (str): The name of the table to be altered.
    column (str): The name of the column to be added.
    data_type (str): The data type of the new column.

________________________________________________________________________________________________________

These functions are designed to facilitate various database operations in a seamless and efficient manner.
By utilizing these functions, you can easily manage your database schema and data without writing repetitive 
SQL queries manually. Each function leverages the execute_query function to handle the execution and logging of 
SQL commands, ensuring consistency and error handling across all operations.






