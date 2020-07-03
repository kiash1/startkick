#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # todo add dynamic path
    sys.path.append('/'.join([os.path.dirname(os.path.realpath(__file__)), 'scores_start/settings']))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scores_start.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
