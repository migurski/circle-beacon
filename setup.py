from setuptools import setup, find_packages

setup(
    name = 'Circle-Tickler',
    version = '1.0.1',
    url = 'https://github.com/migurski/circle-tickler',
    author = 'Michal Migurski',
    author_email = 'mike-github@teczno.com',
    description = '...',
    packages = find_packages(),
    entry_points = dict(
        console_scripts = [
            'tickle-circle=tickle_circle:main',
        ]
    ),
    package_data = {},
    install_requires = [
        'requests == 2.11.1',
        'uritemplate == 3.0.0',
        ]
)
