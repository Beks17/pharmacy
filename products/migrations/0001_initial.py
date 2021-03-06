# Generated by Django 4.0.3 on 2022-06-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MedClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('reg_num', models.CharField(max_length=15)),
                ('med_isntruction', models.TextField(max_length=2000)),
                ('release_form', models.CharField(max_length=30)),
                ('min_order', models.IntegerField()),
                ('price_exw', models.DecimalField(decimal_places=2, max_digits=10)),
                ('med_image', models.ImageField(upload_to='')),
                ('active_ingredient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.activeingredient')),
                ('med_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.medclass')),
            ],
        ),
    ]
