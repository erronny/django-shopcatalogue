# Generated by Django 2.1 on 2019-11-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20191101_1419'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catagories',
        ),
        migrations.AddField(
            model_name='catagory',
            name='catagory_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
