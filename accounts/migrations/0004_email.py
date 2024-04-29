# Generated by Django 4.2.7 on 2024-04-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, null=True)),
                ('email_type', models.CharField(choices=[('Home', 'Home'), ('Personal', 'Personal'), ('Office', 'Office'), ('College', 'College')], max_length=200, null=True)),
            ],
        ),
    ]
