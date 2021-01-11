# Generated by Django 2.1 on 2019-11-01 08:49

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191024_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_catagory', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='mfgdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='catagory_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='products',
            name='catagory',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='product.Catagory'),
        ),
    ]
