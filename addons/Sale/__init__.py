from . import pre_migration


def active_func():
    print("sale")
    """
    Executes the pre-migration and post-migration functions.
    """
    pre_migration.active_pre_func()
