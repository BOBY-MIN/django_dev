# Generated by Django 3.2 on 2021-05-03 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_devboardbsc_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devboardbsc',
            options={'managed': False, 'ordering': ('-insert_dt',), 'verbose_name': 'board', 'verbose_name_plural': 'boards'},
        ),
    ]
