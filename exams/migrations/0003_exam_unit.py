# Generated by Django 2.2.4 on 2019-09-06 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_response_types', '0004_unit'),
        ('exams', '0002_auto_20190905_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_response_types.Unit'),
        ),
    ]
