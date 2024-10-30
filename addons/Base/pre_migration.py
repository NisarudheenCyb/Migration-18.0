from upgrade_lib import upgrade_tools


class BaseTableUpdater:
    _name = "a_base.pre.migration"

    ADD_TABLES = {
        "res_company",
        "res_currency",
        "res_groups",
        "res_lang",
        "res_partner",
        "res_partner_bank",
        "res_users",
        "res_users_apikeys",
        "res_users_apikeys_description",
        "res_users_identitycheck",
        "res_users_settings"
    }

    ADD_COLUMNS = {
        "res_company": [
            ("batch_payment_sequence_id", "INTEGER"),
            ("account_price_include", "CHARACTER VARYING"),
            ("sale_lock_date", "DATE"),
            ("purchase_lock_date", "DATE"),
            ("hard_lock_date", "DATE"),
            ("display_invoice_tax_company_currency", "BOOLEAN"),
            ("check_account_audit_trail", "BOOLEAN"),
            ("autopost_bills", "BOOLEAN")],
        "res_currency": [("iso_numeric", "INTEGER")],
        "res_groups": [("api_key_duration", "DOUBLE PRECISION")],
        "res_lang": [("short_time_format", "CHARACTER VARYING")],
        "res_partner": [
            ("barcode", "JSONB"),
            ("specific_property_product_pricelist", "JSONB"),
            ("invoice_template_pdf_report_id", "INTEGER"),
            ("autopost_bills", "CHARACTER VARYING"),
            ("credit_limit", "JSONB"),
            ("property_account_payable_id", "JSONB"),
            ("property_account_receivable_id", "JSONB"),
            ("property_account_position_id", "JSONB"),
            ("property_payment_term_id", "JSONB"),
            ("property_supplier_payment_term_id", "JSONB"),
            ("trust", "JSONB"),
            ("ignore_abnormal_invoice_date", "JSONB"),
            ("ignore_abnormal_invoice_amount", "JSONB"),
            ("invoice_sending_method", "JSONB"),
            ("invoice_edi_format_store", "JSONB"),
            ("property_outbound_payment_method_line_id", "JSONB"),
            ("property_inbound_payment_method_line_id", "JSONB")
        ],
        "res_partner_bank": [("aba_routing", "CHARACTER VARYING")],
        "res_users": [("tour_enabled", "BOOLEAN")],
        "res_users_apikeys": [("expiration_date", "TIMESTAMP WITHOUT TIME ZONE")],
        "res_users_apikeys_description": [
            ("duration", "CHARACTER VARYING"),
            ("expiration_date", "TIMESTAMP WITHOUT TIME ZONE")
        ],
        "res_users_identitycheck": [("auth_method", "CHARACTER VARYING")],
        "res_users_settings": [
            ("channel_notifications", "CHARACTER VARYING"),
            ("mute_until_dt", "TIMESTAMP WITHOUT TIME ZONE")
        ]
    }

    def add_column(self):
        print("base_pre")
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
    BaseTableUpdater.add_column(BaseTableUpdater)