# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def set_namespace(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Roles = apps.get_model("main", "Role")
    for role in Roles.objects.using(db_alias).all().order_by(
            'github_user', 'name', '-modified'
    ):
        try:
            role.namespace = role.owner.username
            role.save()
        except Exception:
            pass


class Migration(migrations.Migration):
    dependencies = [('main', '0017_auto_20151104_1700')]

    operations = [migrations.RunPython(set_namespace)]
