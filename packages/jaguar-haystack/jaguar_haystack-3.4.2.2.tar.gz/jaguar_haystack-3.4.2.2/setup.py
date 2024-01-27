from setuptools import setup, find_packages
setup(
    name='jaguar_haystack',
    version='3.4.2.2',
    author = 'JaguarDB',
    description = 'Jaguar document store for Haystack framework',
    url = 'http://www.jaguardb.com',
    license = 'Apache 2.0',
    python_requires = '>=3.0',
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('jaguardb', ['jaguar_haystack/LICENSE', 'jaguar_haystack/README.md', 'jaguar_haystack/jaguar.py', 'jaguar_haystack/retriever.py'])
    ],
)
