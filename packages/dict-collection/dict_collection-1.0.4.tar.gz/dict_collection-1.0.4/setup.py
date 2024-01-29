from setuptools import setup, find_packages

VERSION = '1.0.4'
DESCRIPTION = 'Utility data structure'
LONG_DESCRIPTION = 'Utility data structure, which extends built-in `dict` data structure.'

# Setting up
setup(
    name='dict_collection',
    version=VERSION,
    author='spwn02',
    author_email='spwn.contact@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['dict_collection', 'dict', 'collection', 'dict', 'spwn02'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)