from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'Ajuda com análise de resultados médicos e laboratoriais.'
LONG_DESCRIPTION = ('O pacote auxilia na compreensão de dados relacionados a exames biológicos, para a documentação '
                    'completa visite o repositório do projeto, via:https://github.com/DeadFall323/Health_Tools')

# Setting up
setup(
    name="Health_Tools",
    version=VERSION,
    author="Kawan S. Dias",
    author_email="<kawan.dias@ufpi.edu.br>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Medical', 'Data', 'analysis','simple','health-tools'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)