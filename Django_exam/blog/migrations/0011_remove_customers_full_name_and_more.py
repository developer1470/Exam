# Generated by Django 5.0.6 on 2024-06-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_customers_first_name_customers_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='customers',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customers',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
