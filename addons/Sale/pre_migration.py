from upgrade_lib import upgrade_tools


class SalePreTableUpdater:
    _name = 'sale.pre.migration'

    ADD_TABLES = {
        "sale_order_line",
        "sale_order_option",
        "sale_order_transaction_rel",
    }

    ADD_COLUMNS = {
        "sale_order_line": [("customizable_pdf_form_fields", "JSONB")],
        "sale_order_option":[
                ("linked_line_id", "INTEGER"),
                ("combo_item_id", "INTEGER"),
                ("virtual_id", "VARCHAR"),
                ("linked_virtual_id", "VARCHAR"),
                ("technical_price_unit", "DOUBLE PRECISION")],
        "sale_order_transaction_rel" : [("sequence", "INTEGER"),("journal_id", "JSONB")]}



    def add_column(self):
        print("sale_pre")
        """
        Adds new columns to specified tables in the database.

        This function iterates over the tables and their corresponding columns
        defined in the ADD_COLUMNS dictionary. For each table, it adds the
        specified columns with the given data types using the `Add_column` method
        from the `upgrade_tools` module.
        """
        for table, columns in self.ADD_COLUMNS.items():
            for column_name, data_type in columns:
                print(column_name,table)
                upgrade_tools.DatabaseMigrationTool.add_column(table, column_name, data_type)

def active_pre_func():
    """
    Activates the pre-function to add new columns.
    """
    SalePreTableUpdater.add_column(SalePreTableUpdater)