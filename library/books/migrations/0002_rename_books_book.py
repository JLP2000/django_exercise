# Generated by Django 4.1.5 on 2023-01-25 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
