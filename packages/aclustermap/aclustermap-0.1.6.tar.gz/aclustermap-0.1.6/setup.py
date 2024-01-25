from setuptools import setup, find_packages
from aclustermap.version import __version__

setup(
    name='aclustermap',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'seaborn',
        'colorcet',
        'pyarrow',
        'PyYAML',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'aclustermap=aclustermap.aclustermap:main',
        ],
    },
    python_requires='>=3.6',
)
