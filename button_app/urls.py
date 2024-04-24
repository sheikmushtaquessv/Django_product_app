from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('scrape/', scrape_data, name='scrape_and_download'),
]
