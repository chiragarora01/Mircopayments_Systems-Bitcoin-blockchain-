# Generated by Django 2.2.5 on 2020-05-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdata',
            name='username',
            field=models.CharField(default=models.CharField(max_length=30), max_length=8),
        ),
    ]
