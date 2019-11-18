# Generated by Django 2.2.4 on 2019-11-07 20:13

from django.db import migrations


def owner_and_collaborator_analysis_permissions(apps, scheme_editor):
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    permission_model = apps.get_model('auth', 'Permission')
    group_model = apps.get_model('auth', 'Group')
    users_content_type = content_type_model.objects.get(app_label='analysis', model='analysis')

    permissions = permission_model.objects.filter(content_type=users_content_type,
                                                  codename__in=['view_analysis', 'add_analysis', 'change_analysis',
                                                                'delete_analysis'])

    groups = group_model.objects.filter(name__in=['collaborator', 'owner'])

    for group in groups:
        for permission in permissions:
            group_permission = group.permissions.add(permission)
            print(group_permission)


def client_analysis_permissions(apps, scheme_editor):
    content_type_model = apps.get_model('contenttypes', 'ContentType')
    permission_model = apps.get_model('auth', 'Permission')
    group_model = apps.get_model('auth', 'Group')
    users_content_type = content_type_model.objects.get(app_label='analysis', model='analysis')

    permissions = permission_model.objects.filter(content_type=users_content_type,
                                                  codename__in=['view_analysis'])

    groups = group_model.objects.filter(name__in=['client'])

    for group in groups:
        for permission in permissions:
            group_permission = group.permissions.add(permission)
            print(group_permission)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191107_1309'),
        ('analysis', '0001_initial')
    ]

    operations = [
        migrations.RunPython(owner_and_collaborator_analysis_permissions),
        migrations.RunPython(client_analysis_permissions)
    ]
