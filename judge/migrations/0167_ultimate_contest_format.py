# Generated by Django 3.2.18 on 2023-09-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0166_display_rank_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contest",
            name="format_name",
            field=models.CharField(
                choices=[
                    ("atcoder", "AtCoder"),
                    ("default", "Default"),
                    ("ecoo", "ECOO"),
                    ("icpc", "ICPC"),
                    ("ioi", "IOI"),
                    ("ioi16", "New IOI"),
                    ("ultimate", "Ultimate"),
                ],
                default="default",
                help_text="The contest format module to use.",
                max_length=32,
                verbose_name="contest format",
            ),
        ),
    ]
