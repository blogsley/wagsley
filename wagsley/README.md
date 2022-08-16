## Wagtail + Puput
Create a Home page of type HomePage
Create a Blog page of type Blog as a child of Home

## Notes

Had to fork wordpress-to-puput to update dependencies
Had to add 'django.contrib.sites' to INSTALLED_APPS
Add SITE_ID = 1 to settings/base.py
Run python manage.py migrate

python manage.py runserver