from setuptools import setup, find_packages

setup(
    name='test_linemate_scraper',
    version='0.1.0',
    author='Stats By Zach',
    author_email='ztandrews18@sbcglobal.net',
    description='A simple example package for scraping linemate data',
    long_description=open('README.md').read(),
    long_description_content_type='markdown',
    url='https://github.com/ztandrews/nhl-linemate-scraper',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>4.0',
        'numpy>1.0',
        'pandas>2.0',
        'requests>2.0'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

