# Generated by Django 2.2 on 2020-08-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.CharField(choices=[('python', 'python'), ('jave', 'java'), ('php', 'php'), ('android', 'android')], default='', max_length=100),
        ),
    ]
