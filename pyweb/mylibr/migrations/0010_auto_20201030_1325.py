# Generated by Django 3.1.2 on 2020-10-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibr', '0009_auto_20201029_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='author',
            field=models.ManyToManyField(related_name='author', to='mylibr.Authors'),
        ),
        migrations.AlterField(
            model_name='library',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='mylibr.Genres'),
        ),
        migrations.AlterField(
            model_name='library',
            name='year',
            field=models.ManyToManyField(related_name='year', to='mylibr.Years'),
        ),
    ]
