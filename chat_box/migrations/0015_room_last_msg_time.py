# Generated by Django 3.2.18 on 2023-11-02 01:41

from django.db import migrations, models


def migrate(apps, schema_editor):
    Room = apps.get_model("chat_box", "Room")
    Message = apps.get_model("chat_box", "Message")

    for room in Room.objects.all():
        messages = room.message_set
        last_msg = messages.first()
        if last_msg:
            room.last_msg_time = last_msg.time
            room.save()


class Migration(migrations.Migration):

    dependencies = [
        ("chat_box", "0014_userroom_unread_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="last_msg_time",
            field=models.DateTimeField(
                db_index=True, null=True, verbose_name="last seen"
            ),
        ),
        migrations.RunPython(migrate, migrations.RunPython.noop, atomic=True),
    ]
