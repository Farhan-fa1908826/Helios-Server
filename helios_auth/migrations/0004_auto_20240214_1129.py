# Generated by Django 2.2.4 on 2024-02-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios_auth', '0003_user_server_user_face_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='server_user_face_share',
            field=models.TextField(blank=True, null=True),
        ),
    ]
