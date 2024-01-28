from setuptools import find_packages, setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = {
    "name": 'shopcloud_django_instrumenting',
    "version": '1.4.0',
    "description": 'Django tool for instrumenting',
    "long_description_content_type": "text/markdown",
    "long_description": README,
    "license": 'MIT',
    "packages": find_packages(),
    "author": 'Konstantin Stoldt',
    "author_email": 'konstantin.stoldt@talk-point.de',
    "url": 'https://github.com/Talk-Point/shopcloud-django-instrumenting',
}

install_requires = [
    'Django>=3.2,<6.0',
    'djangorestframework'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
