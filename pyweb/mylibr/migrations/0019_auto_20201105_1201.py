# Generated by Django 3.1.2 on 2020-11-05 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibr', '0018_auto_20201104_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
    ]
