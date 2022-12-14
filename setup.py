from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

#with open("requirements.txt", "r") as f:
#    requirements = f.read().splitlines()

setup(
    name="escrutinar_jp",
    version="0.0.1",
    author="Jorge Paulo",
    author_email="jorgepsan7@gmail.com",
    description="pegar o IP de um determinado site, coletar dados de um determinado IP.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JP-Linux/projeto_escrutinar",
    packages=find_packages(),
    install_requires="requests",
    python_requires='>=3.7',
)
