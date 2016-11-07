"""\
Greeting
"""

from setuptools import setup, find_packages


setup(
    name='greeting',
    version='1.0.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'greeting=greeting.greeting:greeting',
        ],
    },
)
