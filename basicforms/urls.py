from formapp import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'formpage/',views.index,name="formname")
]
