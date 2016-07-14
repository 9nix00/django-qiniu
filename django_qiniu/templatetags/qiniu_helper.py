# -*- coding: utf-8 -*-

from qiniu import Auth
from qiniustorage.backends import get_qiniu_config
from django.conf import settings
from django import template

register = template.Library()


def qiniu_private(base_url):
    """
    获取私有url
    """
    q = Auth(get_qiniu_config('QINIU_ACCESS_KEY'), get_qiniu_config('QINIU_SECRET_KEY'))
    expire = 3600 if not hasattr(settings, 'QINIU_PREVIEW_EXPIRE') else settings.QINIU_PREVIEW_EXPIRE
    private_url = q.private_download_url(base_url, expires=expire)
    return private_url


@register.simple_tag
def qiniu_preview(url, *args, **kwargs):
    """
    we use weui as default size.
    :param element:
    :param args:
    :return:
    """

    width = kwargs.get('width', 75)
    height = kwargs.get('height', 75)
    scale = kwargs.get('scale', True)
    domain = kwargs.get('domain', True)

    if domain:
        url = '{}://{}/{}'.format('http' if get_qiniu_config('QINIU_SECURE_URL') is not True else 'https',
                                  get_qiniu_config('QINIU_BUCKET_DOMAIN'), url)

    if scale:
        return qiniu_private('{}?imageView2/{}/w/{}/h/{}'.format(url, '2', width, height))
    else:
        return qiniu_private('{}?imageMogr2/thumbnail/{}x{}!'.format(url, width, height))

    pass
