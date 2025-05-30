# Generated by Django 5.1.6 on 2025-02-14 16:11

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boyovut', '0010_alter_togaraklar_body_alter_togaraklar_nomi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='togarak_turlari',
            options={'verbose_name': "To'garak turi", 'verbose_name_plural': "To'garak turlari"},
        ),
        migrations.AlterField(
            model_name='iqtibostlar',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name='togaraklar',
            name='body_small',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=250, verbose_name="To'garak haqida qisqacha"),
        ),
        migrations.AlterField(
            model_name='ustozlar',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name='yangilik_va_tadbirlar',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name='yangilik_va_tadbirlar',
            name='body_small',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=250),
        ),
    ]
