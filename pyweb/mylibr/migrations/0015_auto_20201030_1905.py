# Generated by Django 3.1.2 on 2020-10-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibr', '0014_auto_20201030_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Years',
            new_name='Year',
        ),
    ]
