
from django.urls import path

from . import views

app_name = 'tiny-notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('editor', views.editor, name='editor'),
    path('<uuid:note_id>', views.view_note, name='note'),
    path('api/save-note', views.save_note, name='save-note'),
    path('api/load-note', views.load_note, name='load-note'),
]