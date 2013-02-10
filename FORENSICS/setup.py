try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Forensic scripts',
    'author': 'Jon',
    'url': 'www.',
    'download_url': 'https://github.com/Geordie-Jon/My_Python.git',
    'author_email': 'geordie.jon@btinternet.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'install_requires': ['BeatifulSoup'],
    'install_requires': ['PIL'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'forensics'
}

setup(**config)