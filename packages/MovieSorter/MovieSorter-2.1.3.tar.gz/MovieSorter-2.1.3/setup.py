from setuptools import setup, find_packages

setup(
    name='MovieSorter',
    version='2.1.3',
    author='Ahmadrezadl',
    author_email='ahmadrezakml@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'MovieSorter=MovieSorter.GUI:main'
        ],
    },
    url='http://pypi.python.org/pypi/MovieSorter/',
    license='LICENSE.txt',
    description='An awesome package for sorting movies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "click>=7.1.2",
        "EasySettings>=4.0.0"
    ],
)
