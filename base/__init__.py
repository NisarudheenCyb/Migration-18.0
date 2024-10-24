from . import pre_migration
from . import post_migration


def active_func():
    pre_migration.active_pre_func()