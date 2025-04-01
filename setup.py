from setuptools import setup, find_packages

setup(
    name='spacex_lab',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
    ],
    entry_points={
        'console_scripts': [
            'spacex-lab=app:app'
        ],
    },
)
