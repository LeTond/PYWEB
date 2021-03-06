# Generated by Django 3.1.2 on 2020-10-27 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='mylibr.author')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='style', to='mylibr.style')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year', to='mylibr.year')),
            ],
        ),
    ]
