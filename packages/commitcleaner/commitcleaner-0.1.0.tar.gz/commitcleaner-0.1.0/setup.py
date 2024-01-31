from setuptools import setup, find_packages

setup(
    name='commitcleaner',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'commitcleaner=commitcleaner.cleaner:main',
        ],
    },
    author='Yonghye Kwon',
    author_email='developer.0hye@gmail.com',
    description='A tool to clean Git commit history.',
    keywords='git commit clean',
    url='https://github.com/developer0hye/commitcleaner',
)
