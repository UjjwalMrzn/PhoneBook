# Generated by Django 4.2.7 on 2024-05-03 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_remove_address_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.phone'),
        ),
    ]
