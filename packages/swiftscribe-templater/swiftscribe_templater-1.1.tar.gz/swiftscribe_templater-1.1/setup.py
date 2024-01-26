# setup.py

from setuptools import setup, find_packages

setup(
    name='swiftscribe_templater',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'python-docx',
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'swiftscribe_templater_app=swiftscribe_templater.app:main',
        ],
    },
    author='Nathan Budhu',
    author_email='nathanbudhu@gmail.com',
    description='Generate documents based on a template and populate the tokens within the document.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MrNate592/docscribe-templater/tree/master',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
