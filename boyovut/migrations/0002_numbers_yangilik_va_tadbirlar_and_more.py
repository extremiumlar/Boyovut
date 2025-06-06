# Generated by Django 5.1.5 on 2025-02-13 12:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boyovut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fanlar', models.IntegerField(default=0)),
                ('oquvchilar', models.IntegerField(default=0)),
                ('labaratoriyalar', models.IntegerField(default=0)),
                ('oqituvchilar', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Yangilik_va_tadbirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='yangilik_images')),
                ('manzil', models.CharField(max_length=150)),
                ('boshlanish_sanasi', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('body_small', models.TextField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Yangilik va Tadbirlar',
                'ordering': ['-boshlanish_sanasi'],
            },
        ),
        migrations.AlterModelOptions(
            name='togaraklar',
            options={'ordering': ['-boshlanish_sanasi'], 'verbose_name_plural': "Tog'araklar"},
        ),
        migrations.RemoveField(
            model_name='togaraklar',
            name='publish_time',
        ),
    ]
