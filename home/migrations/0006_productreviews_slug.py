# Generated by Django 5.0.3 on 2024-03-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_productreviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviews',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]