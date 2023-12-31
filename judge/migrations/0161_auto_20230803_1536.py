# Generated by Django 3.2.18 on 2023-08-03 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("judge", "0160_migrate_bookmark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmark",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="bookmark",
            name="object_id",
            field=models.PositiveIntegerField(),
        ),
    ]
