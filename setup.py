from setuptools import setup, find_packages

setup(
    name='stopwordstr',
    version='1.0.0',
    author="Metin Oktay DENIZ",
    author_email='metinoktaydenizz@gmail.com',
    description="Stopwords filter for Turkish languages",
    packages= find_packages(),
    url='https://github.com/metinoktayd/StopWords-Turkish-Language',
    package_dir={'stopwords':'stopwords'},
    include_package_data=True,
    keywords=['stopwords','language processing','nlp','filter',"turkish stopwords"],
)