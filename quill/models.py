from typing import Match
from django.db import models

class QuillNote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.EmailField(default='admin@quill-notes.com')
    title = models.CharField(max_length=500)
    quill_delta = models.TextField(default='', blank=True)
    raw_text = models.TextField(default='', blank=True)
    note_id = models.UUIDField(blank=False)
