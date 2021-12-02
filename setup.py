#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from version import __VERSION__
setup(
    name='d22d',
    version=__VERSION__,
    description=(
        'Migrating form DataBase to DataBase by 2 lines code'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='readerror',
    author_email='readerror@sina.com',
    maintainer='readerror',
    maintainer_email='readerror@sina.com',
    license='GPL License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/DJMIN/D2D',
    python_requires='>=3.6',
    install_requires=[
        "python-logstash",
        "gunicorn",
        "kafka-python",
        "chardet",
        "baostock",
        "flask_socketio",
        "async-timeout",
        "thrift",
        "pyquery",
        "dnspython",
        "Flask_Migrate",
        "coverage",
        "bs4",
        "itsdangerous",
        "pysocks",
        "Werkzeug",
        "pathlib2",
        "nose",
        "zipp",
        "pymongo",
        "psycopg2-binary",
        "Flask_login",
        "logstash_formatter",
        "PyMySQL",
        "urllib3",
        "Flask_Cache",
        "python-logstash-async",
        "gevent",
        "xlsxwriter",
        "mongoengine",
        "phone",
        "Flask_Cors",
        "click",
        "Flask",
        "rednose",
        "eventlet",
        "func_timeout",
        "simplejson",
        "PyHive",
        "cryptg",
        "msgpack",
        "concurrent-log-handler",
        "Flask-Migrate",
        "watchdog",
        "docker",
        "requests[socks]",
        "openpyxl",
        "pymysql",
        "flask",
        "lxml",
        "pandas",
        "python-dateutil",
        "pytest",
        "numpy",
        "SQLAlchemy",
        "Flask_SQLAlchemy",
        "Flask_Script",
        "rarfile",
        "bcrypt",
        "greenlet",
        "xlrd",
        "PySocks",
        "demjson",
        "tushare",
        "psutil",
        "arrow",
        "tornado",
        "flask_mongoengine",
        "celery",
        "flask_sqlalchemy",
        "setuptools",
        "pycryptodome",
        "wrapt",
        "twine",
        "sqlparse",
        "six",
        "requests>=2.22.0",
        "elasticsearch_dsl>=6.1",
        "PyMySQL>=0.9.3",
        "mmysql-connector-python>=8.0.27",
        "redis>=3.2.1",
        "DBUtils>=2.0",
        "elasticsearch>=6.1.1",
        "diskcache",
        "tomorrow3",
        "clickhouse_driver",
        "zip-files",
        "unrar-cffi",
        "paramiko",
        "pyftpdlib",
        "pysnooper",
        "walrus",
        "universal_object_pool",
        "requests-ftp",
        "webdriver_manager",
        "auto_run_on_remote",
        "pika>=1.2.0",
        "http-parser",
        "aiohttp",
        "PySnooper>=1.0.0",
        "decorator>=5.1.0",
        "cssselect>=1.1.0",
        "pyquery>=1.4.3",
        "future>=0.18.1",
        "PyHive>=0.6.3",
        "pyftpdlib>=1.5.5",
        "pycryptodome>=3.11.0",
        "nb_http_client",
    ],
)