from setuptools import setup, find_packages

setup(
    name='pywooscraper',
    version='0.1.1',
    description='Library for scraping stores with WooCommerce, extracts the total number of products it has.',
    long_description='''PyWooScraper is a Python library for scraping online stores powered by WooCommerce.
                       It extracts information such as the total number of products available in the store.
                       This library is useful for gathering data for analytics or other purposes.
                       ''',
    author='Jhon Corella',
    author_email='corella.jhonatan@gmail.com',
    url='https://https://github.com/jhonatanjavierdev',
    download_url='https://github.com/JhonatanJavierDev/PyWooScraper',
    keywords=['scraping', 'woocommerce', 'wordpress', 'scrap'],
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
