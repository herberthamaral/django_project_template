#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    if 'django_project_template' in os.listdir(root):
        os.rename(os.path.join(root, 'django_project_template'), os.path.join(root, '{{project_name}}'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
