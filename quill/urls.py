
from django.urls import path

from . import views

app_name='quill-notes'
urlpatterns = [
    path('', views.index, name='index')
]