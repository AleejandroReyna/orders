# Generated by Django 2.2.4 on 2019-09-26 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20190919_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='dynamic_exam_assignation',
        ),
        migrations.AddField(
            model_name='dynamicexamassignation',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exams.Exam'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dynamicexamassignation',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_response_types.Unit'),
        ),
    ]
