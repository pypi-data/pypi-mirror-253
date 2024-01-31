from setuptools import setup

with open("README.md", "r", encoding="utf-8") as arq:
    readme = arq.read()

setup(
    name='BibFilmes',
    version='1.0.2',
    license='MIT License',
    author='Luiz Felipe',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='luiz.nogueira@ufpi.edu.br',
    keywords='BibFilmes',
    description='',
    packages=['BibFilmes'],
    install_requires=['requests', 'pandas', 'pyarrow'],
)
