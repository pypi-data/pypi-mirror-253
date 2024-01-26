from setuptools import setup, find_packages

setup(
    name='NetGuards',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scapy',
    ],
    author='Sxmpl3',
    description='Network Traffic Analyzer Library',
    url='https://github.com/Sxmpl3/NetGuard',
)