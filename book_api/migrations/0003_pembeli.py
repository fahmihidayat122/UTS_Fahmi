# Generated by Django 5.0.4 on 2024-05-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0002_remove_book_number_of_pages_remove_book_publish_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
