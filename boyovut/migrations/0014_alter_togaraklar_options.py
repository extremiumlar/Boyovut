# Generated by Django 5.1.6 on 2025-02-24 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boyovut', '0013_alter_contact_options_contact_publish_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='togaraklar',
            options={'ordering': ['boshlanish_sanasi'], 'verbose_name': "To'garak", 'verbose_name_plural': "To'garaklar"},
        ),
    ]
