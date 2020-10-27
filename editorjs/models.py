
from uuid import uuid4
from django.db import models


class EditorNote(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    raw_data = models.TextField(default='')
    note_id = models.UUIDField(default=uuid4())
