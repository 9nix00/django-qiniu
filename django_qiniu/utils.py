# -*- coding: utf-8 -*-

from account_helper.middleware import get_current_user_id
from django.utils import timezone
from django.conf import settings
from hashlib import sha1
import os


def user_upload_dir(instance, filename):
    name_struct = os.path.splitext(filename)
    current_user_id = get_current_user_id()
    expire = 3600 if not hasattr(settings, 'QINIU_PREVIEW_EXPIRE') else settings.QINIU_PREVIEW_EXPIRE

    return '{4}/{0}/{3}/{1}{2}'.format(current_user_id,
                                       sha1(filename.encode('utf-8')).hexdigest(),
                                       name_struct[-1] if len(name_struct) > 1 else '',
                                       timezone.now().strftime('%Y-%m-%d-%H-%M'),
                                       expire)
