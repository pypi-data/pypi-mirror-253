# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lib2opds']

package_data = \
{'': ['*'], 'lib2opds': ['templates/*']}

install_requires = \
['defusedxml>=0.7.1,<0.8.0',
 'jinja2>=3.1.2,<4.0.0',
 'pillow>=10.0.1,<11.0.0',
 'pypdf>=3.17.0,<4.0.0']

entry_points = \
{'console_scripts': ['lib2opds = lib2opds.app:cli']}

setup_kwargs = {
    'name': 'lib2opds',
    'version': '0.1.1',
    'description': 'Directory based library to OPDS feeds generator',
    'long_description': '# Lib2OPDS\n\n`lib2opds` generates [OPDS](https://opds.io/) ([version 1.2](https://specs.opds.io/opds-1.2)) catalog for local e-book library so it can be hosted utilizing web server. Currently meta data extraction is supported only for ePUB format.\n\n## Features\n\n- Directory hierarchy support\n- Virtual directories: new books, authors, etc.\n- ePUB format: metadata extraction, thumbnail generation\n- PDF format: metadata extraction, thumbnail generation\n- "Lazy" updating of feeds. `lib2opds` re-generates feeds only when new files are added into the library\n- Sidecar files for metadata extraction\n- Global and local configuration files as well as command line options\n- Caching for better processing of libraries with many books\n\n## How to install\n\n`lib2opds` is distributed on PyPI. The best way to install it is with [pipx](https://pipx.pypa.io).\n\n```\npipx install lib2opds\n```\n\n## How to use\n\n```\n$ tree ./test-library/\n./test-library/\n├── Linux\n│\xa0\xa0 └── How Linux Works - Brian Ward.epub\n└── Science Fiction\n    ├── All Systems Red.epub\n    └── I, Robot - Isaac Asimov.epub\n\n$ lib2opds --opds-base-uri "/opds/" --library-base-uri "/library/" --library-dir "./test-library" --opds-dir "./output"\n\n$ tree ./output/\n./output/\n\n├── covers\n│\xa0\xa0 ├── 03e1b3fe-66b2-43eb-b9f1-da72813419e2\n│\xa0\xa0 ├── 14cdd72c-680c-491c-a017-ddd0d2dbb1d2\n│\xa0\xa0 └── e01dab66-3f78-402a-9ac8-83ebc6b24f11\n├── feeds\n│\xa0\xa0 ├── 101bcb13-37bf-4e13-a543-22c5ff3567d3.xml\n│\xa0\xa0 ├── 127ae484-af53-4056-9cff-517984321e26.xml\n│\xa0\xa0 └── db1d5760-72f5-4f23-af42-d9d6406207c9.xml\n└── index.xml\n```\n\n`/etc/lib2opds.ini` is used by default and options can be overridden via command line arguments.\n\nExample of configuration file for Nginx:\n\n```nginx\nlocation /library {\n        alias /library-dir;\n}\n\nlocation /opds {\n        auth_basic  "Library Area";\n        auth_basic_user_file /etc/nginx/htpasswd;\n        alias /opds-dir;\n        index root.xml index.xml;\n}\n\nlocation /opds/covers {\n        alias /opds-dir/covers;\n}\n```\n\nLibrary location here is not protected with basic auth because of the bug in some e-book reader software.\n\n## Tested devices and applications\n\n* PocketBook devices\n* KyBook 3 EBook Reader\n',
    'author': 'Taras Ivashchenko',
    'author_email': 'oxdef@oxdef.info',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
