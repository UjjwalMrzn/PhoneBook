# Generated by Django 4.2.7 on 2024-05-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_email_phone_alter_address_address_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
