from setuptools import setup, find_packages

setup(
    name='ppsrx',
    version='1.0.3',
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'ppsrx = ppsrx.main_script:main',
        ],
    },
    install_requires=[
    'clipboard==0.0.4',
    'colorama==0.4.6',
    'junos-eznc==2.6.8',
    'lxml==5.1.0',
    'pandas==2.2.0',  
    'prompt_toolkit==3.0.43',
    'setuptools==69.0.3',
    'termcolor==2.4.0',  
],

    author='Eslam',
    description='doing all configuration by one click',
    long_description=open('README.md').read(),
    license='MIT',
)
