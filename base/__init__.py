from . import pre_migration
from . import post_migration


def active_func():
    """
    Executes the pre-migration and post-migration functions.
    """
    pre_migration.active_pre_func()
    post_migration.active_post_func()
