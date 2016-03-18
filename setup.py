from setuptools import find_packages, setup

import django_qiniu

setup(
        name='django-qiniu',
        version=django_qiniu.version,
        packages=find_packages(exclude=["tests"]),
        install_requires=['qiniu', 'django-qiniu-storage', 'django-account-helper'],
        url='https://github.com/9nix00/django-qiniu',
        license='http://opensource.org/licenses/MIT',
        download_url='https://github.com/9nix00/django-qiniu/archive/master.zip',
        include_package_data=True,
        author='wangwenpei',
        author_email='wangwenpei@nextoa.com',
        description='qiniu file(image) upload helper utils',
        keywords='django_qiniu,',
)
