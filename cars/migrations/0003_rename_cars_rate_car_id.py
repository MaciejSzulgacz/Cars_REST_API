# Generated by Django 4.0 on 2022-01-03 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_rate_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='cars',
            new_name='car_id',
        ),
    ]
