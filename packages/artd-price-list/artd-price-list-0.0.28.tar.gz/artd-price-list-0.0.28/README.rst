=====
ArtD Price List
=====
Art Product is a package that makes it possible to manage price lists and price changes.
Quick start
-----------
1. Add to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'django-json-widget'
        'artd_location',
        'artd_partner',
        'artd_product',
        'artd_product_price',
    ]
2. Run `python manage.py migrate` to create the models.