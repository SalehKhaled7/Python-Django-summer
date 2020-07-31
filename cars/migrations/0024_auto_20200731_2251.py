# Generated by Django 3.0.8 on 2020-07-31 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0023_auto_20200731_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('new', 'NEW'), ('used', 'USED')], max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
