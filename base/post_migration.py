import data_base
import console


class BasePostMigration:

    @staticmethod
    def execute_query(conn, query, params=None):
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    @staticmethod
    def update_version():
        """
        Update the version of installed modules and activate companies.
        """
        update_version_query = """
            UPDATE ir_module_module 
            SET latest_version = '18.0.1.0' 
            WHERE state = 'installed';
        """
        activate_company_query = """
            UPDATE res_company 
            SET active = TRUE;
        """
        conn = data_base.execute_data(data_base.database_params)
        with conn:
            BasePostMigration.execute_query(conn, update_version_query)
            BasePostMigration.execute_query(conn, activate_company_query)

        console.logger.info(
            "Updated version to '18.0.1.0' in ir_module_module for installed modules",
            extra={'log_type': 'INFO'}
        )
        console.logger.info(
            "Activated all companies in res_company",
            extra={'log_type': 'INFO'}
        )

    @staticmethod
    def remove_data():
        """
        Remove specific data from the ir_model table.
        """
        delete_records_query = """
            DELETE FROM ir_model 
            WHERE model = 'ir.property';
        """
        conn = data_base.execute_data(data_base.database_params)
        with conn:
            BasePostMigration.execute_query(conn, delete_records_query)

        console.logger.info(
            "Deleted model 'ir.property' from table ir_model",
            extra={'log_type': 'INFO'}
        )

    @staticmethod
    def active_remove_view():
        """
        Remove all entries from report_layout and ir_ui_view tables.
        """
        delete_report_layout_query = "DELETE FROM report_layout;"
        delete_ir_ui_view_query = "DELETE FROM ir_ui_view;"

        conn = data_base.execute_data(data_base.database_params)
        with conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(delete_report_layout_query)
                    cursor.execute(delete_ir_ui_view_query)
                    conn.commit()  # Commit after all deletions
            except Exception as e:
                console.logger.error(
                    "An error occurred while deleting views: %s", e,
                    extra={'log_type': 'ERROR'}
                )
                conn.rollback()  # Rollback in case of error


def active_post_func():
    BasePostMigration.remove_data()
    BasePostMigration.update_version()
    BasePostMigration.active_remove_view()  # If you also want to call this method
