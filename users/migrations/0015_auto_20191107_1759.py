# Generated by Django 2.2.4 on 2019-11-07 23:59

from django.db import migrations


def set_analysis_permissions_to_owner(apps, scheme):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20191107_1756'),
        ('analysis', '0001_initial')
    ]

    operations = [
        migrations.RunPython(set_analysis_permissions_to_owner)
    ]
