# Generated by Django 3.1.5 on 2021-02-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210211_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=3, null=True, upload_to='images/'),
        ),
    ]
