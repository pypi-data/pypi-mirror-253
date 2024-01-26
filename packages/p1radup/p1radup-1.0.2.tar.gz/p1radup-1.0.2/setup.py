from setuptools import setup

setup(
    name='p1radup',
    version='1.0.2',
    entry_points={
        'console_scripts': [
            'p1radup = p1radup.p1radup:main',
        ],
    },
    install_requires=[
        'termcolor',
    ],
    author='Tarek Bouali',
    author_email='contact@tarekbouali.com',
    description='This script identifies duplicate query parameters within each URL and retains only the first occurrence of each parameter for a given hostname.',
    url='https://github.com/iambouali/p1radup',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
