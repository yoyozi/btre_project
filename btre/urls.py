from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), # home page
    path('listings/', include('listings.urls')), # listings page
    path('accounts/', include('accounts.urls')), # accounts page
    path('contacts/', include('contacts.urls')), # accounts page
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
