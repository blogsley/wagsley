from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from ariadne_django.views import GraphQLView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from puput import urls as puput_urls

from search import views as search_views
from wagsley.schema import schema
print(schema)
urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    #path('search/', search_views.search, name='search'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = urlpatterns + [
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),

    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    path('events/', include('events.urls')),

    re_path(r'^comments/', include('django_comments_xtd.urls')),
    path("", include(puput_urls)),
    path("", include(wagtail_urls)),

    path('', include('home.urls')),

]