# Generated by Django 5.1 on 2024-08-18 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'default_permissions': ('add',)},
        ),
    ]
