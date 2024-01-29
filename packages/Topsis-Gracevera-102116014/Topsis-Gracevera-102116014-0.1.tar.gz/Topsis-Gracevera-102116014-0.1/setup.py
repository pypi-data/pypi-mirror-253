from setuptools import setup, find_packages

setup(
    name='Topsis-Gracevera-102116014',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=Topsis_Gracevera_102116014.102116014:main',
        ],
    },
)
