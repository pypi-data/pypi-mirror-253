from setuptools import setup

setup(
    packages=['vkbasalt'],
    entry_points={
        'console_scripts': [
            'vkbasalt=vkbasalt.cli:vkbasalt_cli'
        ]
    },
)
