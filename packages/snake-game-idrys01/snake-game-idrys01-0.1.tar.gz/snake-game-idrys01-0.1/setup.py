from setuptools import setup, find_packages

setup(
    name='snake-game-idrys01',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter', 
    ],
    entry_points={
        'console_scripts': [
            'snake-game-gui = snake_game.snake_game:main',
        ],
    },
)
