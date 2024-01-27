from setuptools import find_packages, setup


def read_file(file_name: str) -> str:
    with open(file_name) as fo:
        return fo.read().strip()


setup(
    name="cloudshell-raritan",
    url="http://www.quali.com/",
    author="Quali",
    author_email="info@quali.com",
    packages=find_packages(),
    install_requires=read_file("requirements.txt"),
    tests_require=read_file("test_requirements.txt"),
    python_requires="~=3.9",
    version=read_file("version.txt"),
    package_data={"": ["*.txt"]},
    description="Quali Raritan PDU specific package",
    long_description="Raritan PDU Shell operations",
    include_package_data=True,
)
