import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    long_description=README,
    long_description_content_type='text/markdown',
    name='topsis_Pulkit_102103239',
    version='1.0.0',
    license='MIT',
    description='A Python package to find TOPSIS for MCDM (Multi-Criteria Decision Analysis Method)',
    author='Pulkit Sanan',
    author_email='pulkitsanan2@gmail.com',
    keywords=['TOPSIS', 'MCDM'],
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'topsis_Pulkit_102103279=topsis:main',
        ],
    },
)
