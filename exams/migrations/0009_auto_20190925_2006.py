# Generated by Django 2.2.4 on 2019-09-26 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_remove_exam_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicexamassignation',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam'),
        ),
    ]
