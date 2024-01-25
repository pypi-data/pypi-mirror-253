from setuptools import setup, find_packages

setup(
    name='snake-game-idrys01',
    version='0.202',
    packages=find_packages(),
    install_requires=[
        'tk', 
    ],
    entry_points={
        'console_scripts': [
            'snake-game-gui = snake_game_idrys01.snake_game:main',
        ],
    },
)
