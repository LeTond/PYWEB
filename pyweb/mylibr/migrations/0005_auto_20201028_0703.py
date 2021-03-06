# Generated by Django 3.1.2 on 2020-10-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibr', '0004_auto_20201028_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book', to='mylibr.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='style', to='mylibr.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.ManyToManyField(related_name='year', to='mylibr.Year'),
        ),
    ]
