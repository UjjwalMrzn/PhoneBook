# Generated by Django 4.2.7 on 2024-05-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_person_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='phone',
        ),
        migrations.AddField(
            model_name='address',
            name='Address_type',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office')], max_length=200, null=True),
        ),
    ]
