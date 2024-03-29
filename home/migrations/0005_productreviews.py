# Generated by Django 5.0.3 on 2024-03-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_description_product_scpecification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('review', models.TextField(blank=True)),
                ('stars', models.IntegerField(default=1)),
            ],
        ),
    ]
