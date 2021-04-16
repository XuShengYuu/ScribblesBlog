# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='scribbles',
    version='0.1',
    description='Blog System base on Django',
    author='scribbles',
    author_email='191955126@qq.com',
    url='https://www.scribbles.cn',
    license='MIT',
    packages=find_packages('scribbles'),
    package_dir={'':'scribbles'},


    include_package_data=True, 
    install_requires=[
        'django==2.0.9',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'xadmin==2.0.1',
        'mysqlclient==1.3.13',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.3',
        'Pillow==4.3.0',
        'coreapi==2.3.3',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        'django-debug-toolbar==1.11.1',
        'django-silk==2.0.0',
        'django-simple-captcha==0.5.9',
        'captcha==0.2.4',
        'raven==6.9.0'
    ],
    scripts=[
        'scribbles/scribbles/manage.py',
        'scribbles/scribbles/scribbles/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'scribbles_manage = manage:main',
        ]
    },
    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)