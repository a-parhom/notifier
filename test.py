#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notifier.settings")
    from django.conf import settings
    print settings.FORUM_DIGEST_EMAIL_SUBJECT
