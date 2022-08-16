# Wagsley

## Development

https://direnv.net/

https://docs.djangoproject.com/en/4.1/topics/migrations/#dependencies for more

wagtail.images.edit_handlers.ImageChooserPanel is obsolete and should be replaced by wagtail.admin.panels.FieldPanel

```bash
git clone https://github.com/blogsley/wagsley
cd wagsley
poetry shell
yarn
cd wagsley
poetry install
./manage.py makemigrations
./manage.py migrate
./manage.py puput_initial_data
./manage.py runserver
```