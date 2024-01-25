from setuptools import setup, find_packages

setup(
    name='snake-game-idrys01',
    version='0.201',
    packages=find_packages(),
    install_requires=[
        'tk', 
    ],
    entry_points={
        'console_scripts': [
            'snake-game-gui = snake_game:main',
        ],
    },
)
