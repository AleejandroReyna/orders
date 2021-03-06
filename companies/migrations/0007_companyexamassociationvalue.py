# Generated by Django 2.2.4 on 2019-09-25 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_response_types', '0005_auto_20190906_0656'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0006_auto_20190925_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyExamAssociationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('static', 'static'), ('dynamic', 'dynamic')], max_length=20)),
                ('min', models.FloatField(null=True)),
                ('max', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_exam_association', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.CompanyExamAssociation')),
                ('response_type_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_response_types.ResponseTypeGroup')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_response_types.Unit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
