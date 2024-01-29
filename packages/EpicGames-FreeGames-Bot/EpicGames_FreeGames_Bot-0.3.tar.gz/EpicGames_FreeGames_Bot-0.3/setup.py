from setuptools import setup,find_packages

setup(
    name='EpicGames_FreeGames_Bot',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
    ],
)