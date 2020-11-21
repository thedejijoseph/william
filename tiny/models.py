
from uuid import uuid4

from django.db import models

class TinyNote(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    public_id = models.UUIDField(default=uuid4())
    content = models.TextField(default="")
