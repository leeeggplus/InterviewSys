# Generated by Django 2.0.4 on 2018-05-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180522_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',)},
        ),
    ]