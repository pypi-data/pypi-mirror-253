=====
ArtD Product
=====
Art Product is a package that makes it possible to manage categories, products, taxes, brands, etc.
Quick start
-----------
1. Add to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'artd_location',
        'artd_partner',
        'django-json-widget'
    ]
2. Run `python manage.py migrate` to create the models.