# Generated by Django 3.0.3 on 2020-02-14 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commment',
            new_name='comment',
        ),
    ]
