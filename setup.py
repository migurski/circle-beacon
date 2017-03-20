from setuptools import setup, find_packages

setup(
    name = 'Circle-Beacon',
    version = '2.0.0',
    url = 'https://github.com/migurski/circle-beacon',
    author = 'Michal Migurski',
    author_email = 'mike-github@teczno.com',
    description = '...',
    packages = find_packages(),
    entry_points = dict(
        console_scripts = [
            'alert-circle=alert_circle:main',
        ]
    ),
    package_data = {},
    install_requires = [
        'requests == 2.11.1',
        'uritemplate == 3.0.0',
        ]
)
