# Generated by Django 2.2 on 2020-08-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_status',
            field=models.CharField(default='active', max_length=100),
        ),
    ]
