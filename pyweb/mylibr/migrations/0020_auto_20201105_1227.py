# Generated by Django 3.1.2 on 2020-11-05 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibr', '0019_auto_20201105_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['name']},
        ),
    ]
