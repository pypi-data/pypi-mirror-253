=====
ArtD Order
=====
Art Order is a package that makes it possible to manage orders.
Quick start
-----------
1. Add to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'django_json_widget',
        'artd_location',
        'artd_partner',
        'artd_customer',
        'artd_product',
        'artd_price_list',
        'artd_stock',
        'artd_order',
    ]
2. Run `python manage.py migrate` to create the models.