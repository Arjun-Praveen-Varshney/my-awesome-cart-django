# Generated by Django 4.0.1 on 2022-03-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_phone_order_phone1_order_phone2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(default=0, max_length=111),
        ),
    ]
