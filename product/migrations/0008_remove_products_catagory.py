# Generated by Django 2.1 on 2019-11-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20191102_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='catagory',
        ),
    ]
