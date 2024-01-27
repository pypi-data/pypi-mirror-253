from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='TempoSinc',
    version='0.1.2',
    license='MIT License',
    author='RaiLeal/JoseMateus',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='temposinc.gerencia@gmail.com',
    keywords='Tempo',
    description=u'Previsão de tempo',
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'geopy', 'matplotlib'],)