# Generated by Django 4.0.6 on 2022-11-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0014_remove_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='menu',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='lang',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
