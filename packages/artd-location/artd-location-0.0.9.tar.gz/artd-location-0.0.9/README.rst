=====
ArtD Location
=====
ArtD location is a package that makes it possible to have countries, regions and cities with their respective coding, by default we have all the regions and cities of Colombia.
Quick start
-----------
1. Add "polls" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'artd_location',
    ]
2. Run `python manage.py migrate` to create the polls models.