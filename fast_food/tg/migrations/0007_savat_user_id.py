# Generated by Django 4.1 on 2022-08-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0006_savat'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
