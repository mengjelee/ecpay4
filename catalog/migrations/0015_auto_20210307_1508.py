# Generated by Django 3.1.1 on 2021-03-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20210301_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(1, 'Tutor'), (2, 'Student')]),
        ),
    ]
