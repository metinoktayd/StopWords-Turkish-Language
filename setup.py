#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name= 'stopwords_tr',
    version='2.0.0',
    license='MIT',
    author="Metin Oktay DENIZ",
    author_email='metinoktaydenizz@gmail.com',
    description="Stopwords filter for Turkish languages",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/metinoktayd/StopWords-Turkish-Language',
    include_package_data=True,
    keywords=['stopwords, language processing, nlp, filter, turkish stopwords, stopwords for tr, stop for tr, Türkçe Stopwords, Turkish stop, Türkçe Stop'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    #py_modules=["stopwords_tr"]
    package_dir={'':'src'},
    packages= find_packages('src')
)
