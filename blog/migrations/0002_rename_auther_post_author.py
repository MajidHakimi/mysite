# Generated by Django 4.1 on 2023-04-20 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="auther",
            new_name="author",
        ),
    ]
