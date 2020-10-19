# Generated by Django 3.1.2 on 2020-10-18 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20201018_2052"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FamilCard",
            new_name="FamilyCard",
        ),
        migrations.AlterModelOptions(
            name="family",
            options={"verbose_name_plural": "Families"},
        ),
        migrations.AlterField(
            model_name="family",
            name="hash_number",
            field=models.PositiveIntegerField(
                blank=True, validators=[django.core.validators.MaxValueValidator(9999)]
            ),
        ),
    ]
