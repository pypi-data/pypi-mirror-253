from setuptools import setup, find_packages

setup(
    name='tacrpy',
    version='0.2.11',
    description='Analytická knihovna pro potřeby TA ČR',
    long_description='Knihovna, která slouží pro práci s daty a vypracování analýz TA ČR.',
    author='david.sulc',
    author_email='sulda.str@gmail.com',
    packages=find_packages(),
    project_urls={
        'Documentation': 'https://data.tacr.cz/tacrpy/docs/index.html'
    },
    install_requires=[
        'pandas',
        'gspread',
        'numpy',
        'sentence-transformers',
        'nltk',
        'requests',
        ]
)
