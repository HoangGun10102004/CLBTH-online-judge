# Generated by Django 3.2.18 on 2023-12-06 01:28

from django.db import migrations, models


# Run this in shell
def migrate_revision(apps, schema_editor):
    Comment = apps.get_model("judge", "Comment")

    for c in Comment.objects.all():
        c.revision_count = c.versions.count()
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0175_add_profile_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="revision_count",
            field=models.PositiveIntegerField(default=1),
        ),
        # migrations.RunPython(
        #     migrate_revision, migrations.RunPython.noop, atomic=True
        # ),
    ]
