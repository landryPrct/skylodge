# Generated by Django 3.2.14 on 2022-07-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20220722_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('PAID', 'P'), ('NOT_PAID', 'N')], default='P', max_length=100),
        ),
    ]