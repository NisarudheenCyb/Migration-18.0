import data_base
import console  # Assuming this is where console.logger is defined
from upgrade_lib import upgradefunc



ADD_TABLES = {
    "auth_totp_device",
    "iap_account",
    "ir_act_client",
    "ir_act_report_xml",
    "ir_act_server",
    "ir_act_url",
    "ir_act_window",
    "ir_actions",
    "ir_cron",
    "ir_filters",
    "ir_mail_server",
    "ir_model_fields",
    "report_paperformat",
    "res_config_settings",
    "res_currency",
    "res_groups",
    "res_lang",
    "res_partner",
    "res_users",
    "res_users_apikeys",
    "res_users_apikeys_description",
    "res_users_identitycheck",
    "web_tour_tour"
}

ADD_COLUMNS = {
    "auth_totp_device": [("expiration_date", "TIMESTAMP WITHOUT TIME ZONE")],
    "iap_account": [
        ("service_id", "INTEGER"),
        ("balance", "VARCHAR"),
        ("state", "VARCHAR"),
        ("service_locked", "BOOLEAN"),
        ("warning_threshold", "DOUBLE PRECISION")
    ],
    "ir_act_client": [("path", "VARCHAR")],
    "ir_act_report_xml": [
        ("path", "VARCHAR"),
        ("domain", "VARCHAR")
    ],
    "ir_act_server": [("path", "VARCHAR")],
    "ir_act_url": [("path", "VARCHAR")],
    "ir_act_window": [("path", "VARCHAR")],
    "ir_actions": [("path", "VARCHAR")],
    "ir_cron": [
        ("failure_count", "INTEGER"),
        ("first_failure_date", "TIMESTAMP WITHOUT TIME ZONE")
    ],
    "ir_filters": [
        ("embedded_action_id", "INTEGER"),
        ("embedded_parent_res_id", "INTEGER")
    ],
    "ir_mail_server": [("max_email_size", "DOUBLE PRECISION")],
    "ir_model_fields": [("company_dependent", "BOOLEAN")],
    "report_paperformat": [("css_margins", "BOOLEAN")],
    "res_config_settings": [("module_sms", "BOOLEAN")],
    "res_currency": [("iso_numeric", "INTEGER")],
    "res_groups": [("api_key_duration", "DOUBLE PRECISION")],
    "res_lang": [("short_time_format", "VARCHAR")],
    "res_partner": [("barcode", "JSONB")],
    "res_users": [("tour_enabled", "BOOLEAN")],
    "res_users_apikeys": [("expiration_date", "TIMESTAMP WITHOUT TIME ZONE")],
    "res_users_apikeys_description": [
        ("duration", "VARCHAR"),
        ("expiration_date", "TIMESTAMP WITHOUT TIME ZONE")
    ],
    "res_users_identitycheck": [("auth_method", "VARCHAR")],
    "web_tour_tour": [
        ("sequence", "INTEGER"),
        ("create_uid", "INTEGER"),
        ("write_uid", "INTEGER"),
        ("url", "VARCHAR"),
        ("rainbow_man_message", "JSONB"),
        ("custom", "BOOLEAN"),
        ("create_date", "TIMESTAMP WITHOUT TIME ZONE"),
        ("write_date", "TIMESTAMP WITHOUT TIME ZONE")
    ]
}



def add_column():

    """
    Adds new columns to specified tables in the database.

    This function iterates over the tables and their corresponding columns
    defined in the ADD_COLUMNS dictionary. For each table, it adds the
    specified columns with the given data types using the `Add_column` method
    from the `upgradefunc` module.
    """

    for table, columns in ADD_COLUMNS.items():
        for column_name, data_type in columns:
            upgradefunc.Add_column(table, column_name, data_type)


def active_pre_func():
    add_column()

