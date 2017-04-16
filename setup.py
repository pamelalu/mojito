from setuptools import setup

setup(
    name='mojito',
    version='1.0',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'validate_email',
        'requests',
        'jsonschema',
        'html2text',
        'flask_restful',
        'flask'
    ],
)