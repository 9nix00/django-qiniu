# -*- coding: utf-8 -*-

from qiniu import Auth
from qiniustorage.backends import get_qiniu_config
from django.conf import settings
from django import template

import requests

register = template.Library()


def qiniu_private(base_url):
    """
    get private resource
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

    # use original image
    if width == 'auto' and height == 'auto':
        return qiniu_private(url)

    if scale:
        width_str = '/w/{}'.format(width) if width != 'auto' else ''
        height_str = '/h/{}'.format(height) if height != 'auto' else ''
        return qiniu_private('{}?imageView2/{}{}{}'.format(url, '2', width_str, height_str))  # mode=2,limit width and height
    else:
        width_str = width if width != 'auto' else ''
        height_str = height if height != 'auto' else ''
        return qiniu_private('{}?imageMogr2/thumbnail/{}x{}!'.format(url, width_str, height_str))

    pass


@register.simple_tag
def qiniu_image_info(url, *args, **kwargs):
    """
    get image info

    ..todo::
        maybe we should add cache support

    :param element:
    :param args:
    :return:
    """

    domain = kwargs.get('domain', True)

    if domain:
        url = '{}://{}/{}'.format('http' if get_qiniu_config('QINIU_SECURE_URL') is not True else 'https',
                                  get_qiniu_config('QINIU_BUCKET_DOMAIN'), url)

    url = qiniu_private('{}?imageInfo'.format(url))
    rtn = requests.get(url)
    return rtn.json()


@register.simple_tag
def qiniu_image_scale_height(url, width, *args, **kwargs):
    """
    get scale height with width
    used for masonry style

    ..todo::
         maybe we should add cache support

    :param element:
    :param args:
    :return:
    """

    info = qiniu_image_info(url, *args, **kwargs)

    image_width = info.get('width')
    ratio = width / image_width

    print((info.get('width'), info.get('height'), width, int(ratio * info.get('height'))))

    return int(ratio * info.get('height'))
