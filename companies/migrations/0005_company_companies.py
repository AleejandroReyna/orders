# Generated by Django 2.2.4 on 2019-09-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20190919_0020'),
        ('companies', '0004_companyexamassociation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='companies',
            field=models.ManyToManyField(through='companies.CompanyExamAssociation', to='exams.Exam'),
        ),
    ]
