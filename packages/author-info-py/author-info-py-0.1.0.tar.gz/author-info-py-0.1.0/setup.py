from setuptools import setup, find_packages

setup(
    name='author-info-py',
    version='0.1.0',
    description='A package to add author information to Python files',
    author='Nemtyrev Aleksey',
    author_email='art.net82@gmail.com',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'author-info-py = author_info_py.cli:main',
        ],
    },
)
