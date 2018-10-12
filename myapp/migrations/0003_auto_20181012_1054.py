# Created manually.

from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.db import migrations

GROUPS = {
	'employees': [
		'can_hear',
	],
}


def apply_migration(apps, schema_editor):
	for group_name, perm_list in GROUPS.items():
		group, created = Group.objects.get_or_create(name=group_name)
		# Assign permissions to groups.
		for permission_code in perm_list:
			permission = Permission.objects.get(codename=permission_code)
			group.permissions.add(permission)


def revert_migration(apps, schema_editor):
	# Not needed for demo app.
	pass


class Migration(migrations.Migration):

	dependencies = [
		('myapp', '0002_auto_20181012_1052'),
	]

	operations = [
		migrations.RunPython(apply_migration, revert_migration),
	]
