# Generated by Django 3.0.6 on 2020-06-16 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cotent',
            new_name='content',
        ),
    ]
