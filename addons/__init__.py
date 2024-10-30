from addons import Base
from addons import Product
from addons import Sale
from addons import Invoice



def active_func():
    Base.active_func()
    Product.active_func()
    Sale.active_func()
    Invoice.active_func()