# Generated by Django 4.1.5 on 2023-01-29 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_rename_date_contact_date2_rename_user_contact_user2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date2',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='user2',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='value2',
            new_name='value',
        ),
    ]
