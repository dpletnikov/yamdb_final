# Generated by Django 2.2.16 on 2022-05-17 22:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_auto_20220518_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='titles',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'title')},
        ),
    ]
