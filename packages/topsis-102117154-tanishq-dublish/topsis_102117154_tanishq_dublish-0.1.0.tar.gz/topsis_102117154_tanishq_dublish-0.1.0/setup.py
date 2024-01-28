from setuptools import setup, find_packages

setup(
    name='topsis_102117154_tanishq_dublish',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
