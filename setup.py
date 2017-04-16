from setuptools import setup

setup(
    name='mojito',
    version='1.0',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful',
        'requests',
        'jsonschema',
        'html2text'
    ],
)