# -*- coding: utf-8 -*-

from django.db import models


class FileField(models.Field):

    description = "Qiniu private file filed"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10240
        super(HandField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(FileField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs




