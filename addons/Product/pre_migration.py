from upgrade_lib import upgrade_tools


class ProductPreTableUpdater:
    _name = 'product.pre.migration'

    ADD_TABLES = {
        "product_attribute",
        "product_attribute_value",
        "product_category",
        "product_document",
        "product_pricelist_item",
        "product_product",
        "product_tag",
        "product_template"
    }

    ADD_COLUMNS = {
        "product_attribute": [
            ("active", "BOOLEAN")
        ],
        "product_attribute_value": [
            ("active", "BOOLEAN")
        ],
        "product_category": [
            ("property_account_income_categ_id", "JSONB"),
            ("property_account_expense_categ_id", "JSONB"),
            ("property_account_downpayment_categ_id", "JSONB")
        ],
        "product_document": [
            ("sequence", "INTEGER"),
            ("attached_on_sale", "CHARACTER VARYING")
        ],
        "product_pricelist_item": [
            ("display_applied_on", "CHARACTER VARYING"),
            ("price_markup", "NUMERIC")
        ],
        "product_product": [
            ("standard_price", "JSONB")
        ],
        "product_tag": [
            ("sequence", "INTEGER")
        ],
        "product_template": [
            ("service_tracking", "CHARACTER VARYING"),
            ("is_favorite", "BOOLEAN"),
            ("property_account_income_id", "JSONB"),
            ("property_account_expense_id", "JSONB")
        ]
    }


    def add_column(self):
        print('product_pre')
        """
        Adds new columns to specified tables in the database.

        This function iterates over the tables and their corresponding columns
        defined in the ADD_COLUMNS dictionary. For each table, it adds the
        specified columns with the given data types using the `Add_column` method
        from the `upgrade_tools` module.
        """
        for table, columns in self.ADD_COLUMNS.items():
            for column_name, data_type in columns:
                upgrade_tools.DatabaseMigrationTool.add_column(table, column_name, data_type)

def active_pre_func():
    """
    Activates the pre-function to add new columns.
    """
    ProductPreTableUpdater.add_column(ProductPreTableUpdater)