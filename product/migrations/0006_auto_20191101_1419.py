# Generated by Django 2.1 on 2019-11-01 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191101_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Catagory'),
        ),
    ]
