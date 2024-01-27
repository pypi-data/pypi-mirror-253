import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sagace_sdk",
    version="0.1.0.2",
    author="Diego Isaac Haruwo Yosiura",
    author_email="diego@ampereconsultoria.com.br",
    description="Pacote de métodos usados para implementação da API de acesso ao SAGACE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ampere.consultoria/sagace-python-sdk.git",
    project_urls={
        "Bug Tracker": "https://gitlab.com/ampere.consultoria/sagace-python-sdk/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    scripts=[],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests', 'requests-toolbelt']
)
