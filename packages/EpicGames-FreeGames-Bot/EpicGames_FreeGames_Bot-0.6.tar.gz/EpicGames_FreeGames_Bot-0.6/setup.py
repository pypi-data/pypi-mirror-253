from setuptools import setup,find_packages

with open("README.md","r") as f:
    description=f.read()
setup(
    name='EpicGames_FreeGames_Bot',
    version='0.6',
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
    long_description=description,
    long_description_content_type="text/markdown",
)