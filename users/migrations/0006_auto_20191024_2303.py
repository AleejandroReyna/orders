# Generated by Django 2.2.4 on 2019-10-25 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191023_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('create_collaborators', 'Create collaborator for company'), ('view_collaborators', 'View collaborators for company'), ('create_clients', 'Create client for company'), ('view_clients', 'View clients for company')]},
        ),
    ]
