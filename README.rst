django qiniu
========================

qiniu file(image) upload helper utils for `Django <https://github.com/django/django>`_


Requirements
------------------

* `Qiniu SDK <https://github.com/qiniu/python-sdk>`_
* `Django-Qiniu-Storage <https://github.com/glasslion/django-qiniu-storage>`_
* `Django-Account-Helper <https://github.com/9nix00/django-account-helper>`_


those packages will auto install when install django_qiniu use pip.



Install
------------------

.. code-block::

    pip install django-qiniu




Config
------------------


#. add `account_helper.middleware.CurrentUserMiddleware` in  MIDDLEWARE_CLASSES

#. set qiniu config follow qiniu-storage document `Configurations <https://github.com/glasslion/django-qiniu-storage/blob/master/README.md#Configurations>`_.

#. edit settings.py.

.. code-block::

    DEFAULT_FILE_STORAGE = 'django_qiniu.backends.QiniuStorage'

    QINIU_PREVIEW_EXPIRE = 300         # 300 seconds,default is 3600 if not set






How to use
---------------------------

feature 1: simple upload progress

edit your models file.

.. code-block::

    from django_qiniu.utils import user_upload_dir


    # ...fields definition...

    pic_00 = models.ImageField('picture 00', upload_to=user_upload_dir, blank=True)



feature 2: show qiniu image easily.
by default, we use weui as default our theme. so default size is 75x75


.. code-block::

    {% load qiniu_helper %}
    <li class="weui_uploader_file" style="background:url({% qiniu_preview image_url %})"></li>
    {# set width,height and scale #}
    <li class="weui_uploader_file" style="background:url({% qiniu_preview image_url width=80 height=90 scale=False %})"></li>
    {# disable add domain-url when request %}
    <li class="weui_uploader_file" style="background:url({% qiniu_preview image_url width=80 height=90 scale=False domain=False %})"></li>













