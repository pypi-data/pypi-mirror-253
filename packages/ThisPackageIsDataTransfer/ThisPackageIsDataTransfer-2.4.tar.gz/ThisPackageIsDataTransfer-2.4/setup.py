from setuptools import setup

setup(
    name='ThisPackageIsDataTransfer',
    version='2.4',
    packages=[
        'DataTransfer',
        'DataTransfer/network',
        'DataTransfer/transferer'
    ],
    entry_points={
        'console_scripts': [
            'transfer=DataTransfer.main:main'
        ]
    }
)