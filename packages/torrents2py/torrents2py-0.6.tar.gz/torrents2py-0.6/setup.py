from setuptools import setup, find_packages

setup(
    name='torrents2py',
    packages=find_packages(exclude=['tests']),  # esclude la cartella 'tests'
    version='0.6',
    license='MIT',
    description='Torrents2py is a simple Python package for searching and retrieving torrent details from Torrentz2.nz',
    readme="README.md",
    author='Gianpaolo',
    url='https://github.com/Gianpi612/torrents2py',
    download_url='https://github.com/Gianpi612/torrents2py/archive/refs/tags/v_0.6.tar.gz',
    keywords=['scraping', 'torrents', 'search engine', 'website', 'links'],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
