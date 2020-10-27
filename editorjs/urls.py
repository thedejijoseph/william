
from django.urls import path

from .import views

app_name = 'editorjs'
urlpatterns = [
    path('', views.index, name='index'),
    path('editor', views.editor, name='editor'),
    path('<uuid:note_id>', views.view_note, name='view_note'),
    path('api/update', views.update_note, name='update_note'),
    path('api/fetch', views.fetch_note, name='fetch_note'),
]
