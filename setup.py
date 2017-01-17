from setuptools import find_packages, setup

# Check and install dependencies using setup tools
setup(
    name="Pluggy",
    version="0.0.1",

    description="Energenie Mi|Home Pi Plug controller",

    url='https://github.com/drinkataco/pluggy',
    download_url='https://github.com/drinkataco/pluggy.git',

    author='drinkataco',
    author_email='',

    license='GPLv2',

    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests'
    ],
)