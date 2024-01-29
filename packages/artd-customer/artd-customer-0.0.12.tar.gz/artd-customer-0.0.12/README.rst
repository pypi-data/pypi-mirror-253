=====
ArtD Customer
=====
Art Customer is a package that makes it possible to manage customers, tags, addresses and additional fields.
Quick start
-----------
1. Add to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'artd_location',
        'artd_partner',
        'django-json-widget'
        'artd_customer'
    ]
2. Run `python manage.py migrate` to create the models.