# Generated by Django 4.0.3 on 2022-08-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_med_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='med_image',
            field=models.ImageField(blank=True, null=True, upload_to='..\\static\\img'),
        ),
    ]
