# Generated by Django 4.0.6 on 2023-01-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0031_product_til'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='kengligi',
            new_name='kengligi_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='uzunligi',
            new_name='kengligi_uz',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='material',
            new_name='material_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='material_uz',
        ),
        migrations.RemoveField(
            model_name='product',
            name='til',
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_ru',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_uz',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='uzunligi_ru',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uzunligi_uz',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]