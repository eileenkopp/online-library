# Generated by Django 4.2.18 on 2025-04-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0003_alter_collectionrequest_collection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/book_covers'),
        ),
    ]
