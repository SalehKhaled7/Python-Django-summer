# Generated by Django 3.0.8 on 2020-08-03 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0032_auto_20200803_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
        migrations.AlterField(
            model_name='image',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car'),
        ),
    ]
