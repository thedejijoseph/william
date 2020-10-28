# Generated by Django 3.1.2 on 2020-10-27 08:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('editorjs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editornote',
            name='note_id',
            field=models.UUIDField(default=uuid.UUID('6ba2237a-1990-4004-9717-5382e0c1b24f')),
        ),
        migrations.AlterField(
            model_name='editornote',
            name='blocks',
            field=models.TextField(default=''),
        ),
    ]
