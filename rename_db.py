import psycopg2
from psycopg2 import sql


def rename_database(database_params):
    current_db_name = database_params.get('dbname')
    new_db_name = 'upgrade_database'
    user = database_params.get('user')
    password = database_params.get('password')
    host = database_params.get('host')
    port = int(database_params.get('port', 5432))
    try:
        # Connect to the default 'postgres' database to perform the rename operation
        conn = psycopg2.connect(
            dbname='postgres',
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True

        with conn.cursor() as cursor:
            # Terminate all connections to the current database
            cursor.execute(sql.SQL("""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = %s
                AND pid <> pg_backend_pid();
            """), [current_db_name])

            # Ensure the new database name does not already exist
            cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [new_db_name])
            if cursor.fetchone():
                raise ValueError(f"The database '{new_db_name}' already exists.")

            # Rename the database
            cursor.execute(sql.SQL("ALTER DATABASE {} RENAME TO {}").format(
                sql.Identifier(current_db_name),
                sql.Identifier(new_db_name)
            ))
            print(f"Database '{current_db_name}' has been renamed to '{new_db_name}'.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
