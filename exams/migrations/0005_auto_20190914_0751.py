# Generated by Django 2.2.4 on 2019-09-14 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20190914_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='dynamic_exam_group',
            new_name='dynamic_exam_assignation',
        ),
    ]
