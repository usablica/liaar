from distutils.core import setup
import setuptools


setup(
    name='Liaar',
    version='0.2.0',
    packages=['liaar', 'liaar.lib'],
    license='LICENSE',
    url='https://github.com/usablica/liaar',
    description='Create fake REST API in a minute',
    author='Afshin Mehrabani',
    author_email='afshin.meh@gmail.com',
    install_requires=['Twisted', 'fake-factory'],
    entry_points={
        'console_scripts': [
            'liaar = liaar.liaar:main',
        ]
    }
)
