# Generated by Django 4.0.1 on 2022-03-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_phone1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone1',
            field=models.CharField(max_length=13),
        ),
    ]
