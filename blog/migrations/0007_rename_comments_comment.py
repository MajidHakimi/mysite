# Generated by Django 4.1 on 2023-06-17 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_activate_comments_active_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comment",
        ),
    ]
