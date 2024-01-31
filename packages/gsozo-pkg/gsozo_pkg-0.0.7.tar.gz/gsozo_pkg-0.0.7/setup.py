from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='gsozo-pkg',
    version='0.0.1',
    author="Tecnologia Grupo SOZO",
    author_email="tecnologia@gruposozo.com.br",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'pipedrive-python-lib',
        'loguru',
        'numpy',
        'pandas',
        'sqlalchemy',
        'tqdm',
        'jinja2',
        'pywin32 ; platform_system=="Windows"'
    ],
    include_package_data=True,
    python_requires='>=3.8',
)
