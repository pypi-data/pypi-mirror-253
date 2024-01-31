# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anitya',
 'anitya.db',
 'anitya.db.migrations',
 'anitya.db.migrations.versions',
 'anitya.lib',
 'anitya.lib.backends',
 'anitya.lib.ecosystems',
 'anitya.lib.versions',
 'anitya.templates']

package_data = \
{'': ['*'],
 'anitya': ['static/*',
            'static/css/*',
            'static/css/fonts/*',
            'static/css/images/*',
            'static/ico/*',
            'static/img/*']}

install_requires = \
['Flask-Login>=0.6.3,<0.7.0',
 'Flask-WTF>=1.2.1,<2.0.0',
 'Flask>=3.0.0,<4.0.0',
 'Jinja2<3.1.4',
 'SQLAlchemy>=1.4.41,<2.0.0',
 'WTForms>=3.0.1,<4.0.0',
 'Werkzeug==3.0.1',
 'alembic>=1.8.1,<2.0.0',
 'anitya-schema>=2.0.1,<3.0.0',
 'arrow>=1.2.3,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'defusedxml>=0.7.1,<0.8.0',
 'fedora-messaging>=3.1.0,<4.0.0',
 'ordered-set>=4.1.0,<5.0.0',
 'packaging>=23.0,<24.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'semver>=3.0.0,<4.0.0',
 'social-auth-app-flask-sqlalchemy>=1.0.1,<2.0.0',
 'social-auth-app-flask>=1.0.0,<2.0.0',
 'straight.plugin>=1.5.0,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'webargs>=8.2.0,<9.0.0']

entry_points = \
{'console_scripts': ['check_service = anitya.check_service:main',
                     'sar = anitya.sar:main']}

setup_kwargs = {
    'name': 'anitya',
    'version': '1.9.0',
    'description': 'A cross-distribution upstream release monitoring project',
    'long_description': '\n.. image:: https://img.shields.io/pypi/v/anitya.svg\n  :target: https://pypi.org/project/anitya/\n\n.. image:: https://img.shields.io/pypi/pyversions/anitya.svg\n  :target: https://pypi.org/project/anitya/\n\n.. image:: https://readthedocs.org/projects/anitya/badge/?version=latest\n  :alt: Documentation Status\n  :target: https://anitya.readthedocs.io/en/latest/?badge=latest\n  \n.. image:: https://img.shields.io/badge/renovate-enabled-brightgreen.svg\n  :target: https://renovatebot.com/\n\n.. image::  https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit\n  :target:  https://pre-commit.com/\n  \n\n======\nAnitya\n======\n\nAnitya is a release monitoring project. It provides a user-friendly interface\nto add, edit, or browse projects. A cron job can be configured to regularly\nscan for new releases of projects. When Anitya discovers a new release for a\nproject, it publishes a RabbitMQ messages via `fedora messaging`_.\nThis makes it easy to integrate with Anitya and perform actions when a new\nrelease is created for a project. For example, the Fedora project runs a service\ncalled `the-new-hotness <https://github.com/fedora-infra/the-new-hotness/>`_\nwhich files a Bugzilla bug against a package when the upstream project makes a\nnew release.\n\nFor more information, check out the `documentation`_!\n\n\nDevelopment\n===========\n\nFor details on how to contribute, check out the `contribution guide`_.\n\n\n.. _documentation: https://anitya.readthedocs.io/\n.. _contribution guide: https://anitya.readthedocs.io/en/latest/contributing.html\n.. _fedora messaging: https://fedora-messaging.readthedocs.io/en/latest\n',
    'author': 'Pierre-Yves Chibon',
    'author_email': 'pingou@pingoured.fr',
    'maintainer': 'Michal Konecny',
    'maintainer_email': 'mkonecny@redhat.com',
    'url': 'https://release-monitoring.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.10,<4.0.0',
}


setup(**setup_kwargs)
