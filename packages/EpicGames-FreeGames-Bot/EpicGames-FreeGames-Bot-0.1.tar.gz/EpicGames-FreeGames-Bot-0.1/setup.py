from setuptools import setup,find_packages

setup (
    name='EpicGames-FreeGames-Bot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',

    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

)