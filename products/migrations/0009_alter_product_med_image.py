# Generated by Django 4.0.3 on 2022-08-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_med_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='med_image',
            field=models.ImageField(default='default_photo.jpg', upload_to='static/img/'),
        ),
    ]
