from setuptools import setup, find_packages

setup(
    name='isapilib',
    version='1.5.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'templates': ['*'],
    },
    install_requires=[
        'django>=4.2',
        'djangorestframework>=3.0.0',
        'djangorestframework-simplejwt>=5.0.0',
        'Pillow>=9.4.0',
    ],
)
