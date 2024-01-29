from setuptools import setup,find_packages

setup(
    name='EpicGames_FreeGames_Bot',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
    ],
    entry_points={
        "console_scripts": [
            "EpicGames_FreeGames_Bot=EpicGames_FreeGames_Bot:hello"
        ],
    },
)