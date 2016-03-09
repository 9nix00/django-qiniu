# -*- coding: utf-8 -*-

from qiniustorage import backends
from django.utils.encoding import filepath_to_uri
from six.moves.urllib_parse import urljoin
from django.conf import settings

class QiniuStorage(backends.QiniuStorage):
    def url(self, name):
        name = self._normalize_name(self._clean_name(name))
        name = filepath_to_uri(name)

        expire = 3600 if not hasattr(settings, 'QINIU_PREVIEW_EXPIRE') else settings.QINIU_PREVIEW_EXPIRE

        protocol = 'https://' if self.secure_url else 'http://'
        url = urljoin(protocol + self.bucket_domain, name)
        return self.auth.private_download_url(url, expires=expire)

    pass
