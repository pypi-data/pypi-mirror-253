from setuptools import setup,find_packages

VERSION = "1.0.0"
DESCRIPTION = "Pacote de geração de dados de pessoas"
LONG_DESCRIPTION = "Pacote de geração de dados de pessoas, tais como nome, cpf, data de nascimento, peso, altura, telefone, cidade e estado."

#setting up

setup(
    # the name must match the folder name
    name="person-generete-br",
    version = VERSION,
    author = "Erlanny",
    author_email = "erlannyrodrigues@gmail.com",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = ["numpy", "string", "pycep", "datetime", "random", "csv"],#adiciona bibliotecas adicionais
    keywords = ['python', 'person', 'generate', 'brasil'],
    classifiers = ["Development Status :: 3 - Alpha",]

)