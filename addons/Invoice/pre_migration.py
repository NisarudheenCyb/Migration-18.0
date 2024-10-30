from upgrade_lib import upgrade_tools


class InvPreTableUpdater:
        _name = 'invoice.pre.migration'

        ADD_TABLES = {
            "account_account",
            "account_analytic_distribution_model",
            "account_analytic_plan",
            "account_bank_statement_line",
            "account_cash_rounding",
            "account_journal",
            "account_move",
            "account_payment",
            "account_payment_register",
            "account_reconcile_model",
            "account_report",
            "account_report_line",
            "account_tax",
            "account_tax_group",
        }

        ADD_COLUMNS = {
            "account_account": [("code_store", "JSONB"),],
            "account_analytic_distribution_model": [("sequence", "INTEGER")],
            "account_analytic_plan": [("default_applicability", "JSONB")],
            "account_bank_statement_line": [("journal_id", "INTEGER"),("company_id", "INTEGER")],
            "account_cash_rounding": [("profit_account_id", "JSONB"),("loss_account_id", "JSONB")],
            "account_journal": [("autocheck_on_post", "BOOLEAN")],
            "account_move": [
                ("origin_payment_id", "INTEGER"),
                ("preferred_payment_method_line_id", "INTEGER"),
                ("sending_data", "JSONB"),
                ("invoice_currency_rate", "NUMERIC"),
                ("amount_untaxed_in_currency_signed", "NUMERIC"),
                ("checked", "BOOLEAN"),
                ("made_sequence_gap", "BOOLEAN"),
                ("is_manually_modified", "BOOLEAN"),
            ],
            "account_move_line": [("is_imported", "BOOLEAN")],
            "account_payment": [
                ("journal_id", "INTEGER"),
                ("company_id", "INTEGER"),
                ("name", "CHARACTER VARYING"),
                ("state", "CHARACTER VARYING"),
                ("memo", "CHARACTER VARYING"),
                ("date", "DATE"),
                ("is_sent", "BOOLEAN"),
            ],
            "account_payment_register": [
                ("custom_user_currency_id", "INTEGER"),
                ("installments_mode", "CHARACTER VARYING"),
                ("custom_user_amount", "NUMERIC"),
            ],
            "account_reconcile_model": [("counterpart_type", "CHARACTER VARYING")],
            "account_report": [
                ("integer_rounding", "CHARACTER VARYING"),
                ("currency_translation", "CHARACTER VARYING"),
                ("filter_budgets", "BOOLEAN")
            ],
            "account_report_line": [("horizontal_split_side", "CHARACTER VARYING")],
            "account_tax": [("price_include_override", "CHARACTER VARYING"),("invoice_legal_notes", "TEXT")],
            "account_tax_group": [("pos_receipt_label", "CHARACTER VARYING")]
        }

        def add_column(self):
            print("inv_pre")
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
    InvPreTableUpdater.add_column(InvPreTableUpdater)