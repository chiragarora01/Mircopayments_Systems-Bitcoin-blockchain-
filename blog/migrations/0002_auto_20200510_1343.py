# Generated by Django 2.2.5 on 2020-05-10 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='lastname',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]
