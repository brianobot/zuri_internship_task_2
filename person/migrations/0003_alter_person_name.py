# Generated by Django 4.2.4 on 2023-09-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0002_alter_person_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
