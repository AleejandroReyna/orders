# Generated by Django 2.2.4 on 2019-10-10 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('exams', '0009_auto_20190925_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_group',
        ),
        migrations.AddField(
            model_name='exam',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Category'),
        ),
    ]
