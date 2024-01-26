from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    README = fh.read()

setup(
    author="Sanghoon Lee (DSsoli)",
    author_email="solisoli3197@gmail.com",
    name="esa-2scm",
    version="0.0.7",
    description="ESA-2SCM Python Package for Causal Discovery",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["numpy", "pandas", "scipy", "scikit-learn"],
    url="https://github.com/DSsoli/esa-2scm.git",
    packages=find_packages(include=['esa_2scm', 'esa_2scm.*']),
    package_data={"esa_2scm": ['LICENSE', 'examples/*']},
    include_package_data=True
)